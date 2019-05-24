from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime
from ppapp.rsop.ca_rsop import CertAuthorityRSoP
from ppapp.models import ClientCert


def create_cert(cert_authority, private_key):
    one_day = datetime.timedelta(1, 0, 0)
    # Use our private key to generate a public key
    root_key = serialization.load_pem_private_key(
        private_key.encode("ascii"), password=None, backend=default_backend()
    )

    root_cert = x509.load_pem_x509_certificate(
        cert_authority.encode("ascii"), default_backend()
    )

    # Now we want to generate a cert from that root
    cert_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    new_subject = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Glendale"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Org Name"),
        ]
    )

    crl_distribution_point = x509.DistributionPoint(full_name=[x509.UniformResourceIdentifier(value='https://fq.dn')], relative_name=None, crl_issuer=None, reasons=None)

    cert = (
        x509.CertificateBuilder()
        .subject_name(new_subject)
        .issuer_name(root_cert.issuer)
        .public_key(cert_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=30))
        .add_extension(
            x509.CRLDistributionPoints([crl_distribution_point]), critical=True
        )
        .sign(root_key, hashes.SHA256(), default_backend())
    )

    # Dump to scratch
    with open("scratch/phone_cert.crt", "wb") as f:
        f.write(cert.public_bytes(encoding=serialization.Encoding.PEM))

    # Return PEM
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

    cert_key_pem = cert_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return cert_pem, cert_key_pem


def issue_client_cert(phone):
    # Get our phone's CA from RSoP data
    cert_authority_rsop = CertAuthorityRSoP(phone)
    cert_authority = cert_authority_rsop.current_cert_authority.cert_authority
    # Get client cert in PEM to add to DB
    client_cert_pem, client_key_pem = create_cert(cert_authority.cert, cert_authority.private_key)
    # Create the client cert in DB
    client_cert = ClientCert.create(
        cert=client_cert_pem,
        private_key=client_key_pem,
        cert_authority=cert_authority,
        phone=phone,
    )
    # Set it as the phone's current
    phone.active_client_cert = client_cert


# Create the cert, assign it to the phone
# Mark the previous as cert needing to revoked
# When the phone next checks in revoke it
def reissue_client_cert(phone):
    issue_client_cert(phone)
    pass

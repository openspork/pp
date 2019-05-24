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
    private_key = serialization.load_pem_private_key(
        private_key.encode("ascii"), password=None, backend=default_backend()
    )
    public_key = private_key.public_key()

    ca = x509.load_pem_x509_certificate(
        cert_authority.encode("ascii"), default_backend()
    )

    builder = x509.CertificateBuilder()
    builder = builder.subject_name(
        x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"cryptography.io")])
    )
    builder = builder.issuer_name(ca.issuer)
    builder = builder.not_valid_before(datetime.datetime.today() - one_day)
    builder = builder.not_valid_after(datetime.datetime.today() + (one_day * 30))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(public_key)

    builder = builder.add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"cryptography.io")]), critical=False
    )
    builder = builder.add_extension(
        x509.BasicConstraints(ca=False, path_length=None), critical=True
    )

    cert = builder.sign(
        private_key=private_key, algorithm=hashes.SHA256(), backend=default_backend()
    )
    # Dump to scratch
    # with open("scratch/phone_cert.pem", "wb") as f:
    #     f.write(cert.public_bytes(
    #         encoding=serialization.Encoding.PEM
    #     ))

    # Return PEM
    return cert.public_bytes(encoding=serialization.Encoding.PEM)


def issue_client_cert(phone):
    # Get our phone's CA from RSoP data
    cert_authority_rsop = CertAuthorityRSoP(phone)
    cert_authority = cert_authority_rsop.current_cert_authority.cert_authority

    client_cert = create_cert(cert_authority.cert, cert_authority.private_key)

    ClientCert.create(cert = client_cert, cert_authority = cert_authority, phone = phone)

# Create the cert, assign it to the phone
# Mark the previous as cert needing to revoked
# When the phone next checks in revoke it
def reissue_client_cert(phone):
    issue_client_cert(phone)
    pass

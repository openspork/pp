from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from datetime import datetime, timedelta



def revoke_cert(cert_revocation_list_pem, cert):
    cert_revocation_list = x509.load_pem_x509_crl(cert_revocation_list_pem, default_backend)

    builder = x509.RevokedCertificateBuilder()
    builder.revocation_date(datetime.today)
    builder.serial_number(serial)
    revoked_cert = builder.build(default_backend())

    cert_revocation_list.append(revoked_cert)

    return cert_revocation_list.public_bytes(encoding=serialization.Encoding.PEM)

def revoke_client_cert(phone):
    # Assess RSoP
    cert_revocation_list = phone.active_client_cert.cert_authority.cert_revocation_list















def build_crl(cert_authority, private_key):
    # Load our root cert
    root_cert = x509.load_pem_x509_certificate(
        cert_authority.encode("ascii"), default_backend()
    )

    # Load our root key
    root_key = serialization.load_pem_private_key(
        private_key.encode("ascii"), password=None, backend=default_backend()
    )

    builder = x509.CertificateRevocationListBuilder()
    builder = builder.last_update(datetime.today())
    builder = builder.next_update(datetime.today() + timedelta(0, 6, 0))
    builder = builder.issuer_name(root_cert.issuer)
    cert_revocation_list = builder.sign(
        private_key=root_key,
        algorithm=hashes.SHA256(),
        backend=default_backend()
        )
    return cert_revocation_list.public_bytes(encoding=serialization.Encoding.PEM)

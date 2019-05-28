from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from datetime import datetime, timedelta
from ppapp.models import (
    ClientCert,
    BaseParam,
    AvailParam,
    PhoneAvailParams,
    PhoneActiveClientCert,
)


def build_crl(cert_authority_pem, private_key_pem, certs_to_revoke=None):
    # Load our root cert
    root_cert = x509.load_pem_x509_certificate(
        cert_authority_pem.encode("ascii"), default_backend()
    )

    # Load our root key
    root_key = serialization.load_pem_private_key(
        private_key_pem.encode("ascii"), password=None, backend=default_backend()
    )

    builder = x509.CertificateRevocationListBuilder()
    builder = builder.last_update(datetime.today())
    builder = builder.next_update(datetime.today() + timedelta(1, 0, 0))
    builder = builder.issuer_name(root_cert.issuer)
    if certs_to_revoke:
        for revoked_cert in certs_to_revoke:
            builder = builder.add_revoked_certificate(revoked_cert)
    cert_revocation_list = builder.sign(
        private_key=root_key, algorithm=hashes.SHA256(), backend=default_backend()
    )
    return cert_revocation_list.public_bytes(encoding=serialization.Encoding.PEM)


def revoke_cert(cert_authority_pem, private_key_pem, cert_revocation_list_pem, cert_pem):
    revoked_certs = []
    # Load CRL
    cert_revocation_list = x509.load_pem_x509_crl(
        cert_revocation_list_pem.encode("ascii"), default_backend()
    )

    for revoked_cert in cert_revocation_list:
        revoked_certs.append(revoked_cert)

    # Load cert
    cert = x509.load_pem_x509_certificate(cert_pem.encode("ascii"), default_backend())
    # print('revoking cert', cert.fingerprint(hashes.SHA256()))
    # Create a revoked cert
    builder = x509.RevokedCertificateBuilder()
    builder = builder.revocation_date(datetime.today())
    builder = builder.serial_number(cert.serial_number)
    revoked_cert = builder.build(default_backend())

    revoked_certs.append(revoked_cert)

    return build_crl(cert_authority_pem, private_key_pem, revoked_certs)


def revoke_client_cert(phone):
    # Get the current cert
    active_client_cert = PhoneActiveClientCert.get(
        PhoneActiveClientCert.phone == phone
    ).active_client_cert

    # Get current cert PEM
    client_cert_pem = active_client_cert.cert

    cert_authority = active_client_cert.cert_authority

    # Get CA PEM
    cert_authority_pem = cert_authority.cert
    private_key_pem = cert_authority.private_key

    # Get CRL PEM
    cert_revocation_list_pem = cert_authority.cert_revocation_list

    # Save our new CRL to our CA
    cert_authority.cert_revocation_list = revoke_cert(
        cert_authority_pem, private_key_pem, cert_revocation_list_pem, client_cert_pem
    )
    cert_authority.save()

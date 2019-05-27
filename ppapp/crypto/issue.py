from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import padding
import datetime
from flask import url_for
from ppapp.rsop.ca_rsop import CertAuthorityRSoP
from ppapp.models import (
    ClientCert,
    BaseParam,
    AvailParam,
    PhoneAvailParams,
    PhoneActiveClientCert,
)
from ppapp.util.param_ops import get_phone_params
from .revoke import revoke_client_cert


def create_cert(cert_authority_pem, private_key_pem, cert_revocation_list_uri=None):
    one_day = datetime.timedelta(1, 0, 0)
    # Load our root cert
    root_cert = x509.load_pem_x509_certificate(
        cert_authority_pem.encode("ascii"), default_backend()
    )

    root_cert_thumbprint = root_cert.fingerprint(hashes.SHA1()).hex()

    # Load our root key
    root_key = serialization.load_pem_private_key(
        private_key_pem.encode("ascii"), password=None, backend=default_backend()
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

    crl_distribution_point = x509.DistributionPoint(
        full_name=[
            x509.UniformResourceIdentifier(
                value=url_for(
                    "get_cert_revocation_list",
                    thumbprint=root_cert_thumbprint,
                    _external=True,
                )
            )
        ],
        relative_name=None,
        crl_issuer=[x509.DirectoryName(value=root_cert.subject)],
        reasons=frozenset(
            (
                x509.ReasonFlags.key_compromise,
                x509.ReasonFlags.ca_compromise,
                x509.ReasonFlags.affiliation_changed,
                x509.ReasonFlags.superseded,
                x509.ReasonFlags.cessation_of_operation,
                x509.ReasonFlags.certificate_hold,
                x509.ReasonFlags.privilege_withdrawn,
                x509.ReasonFlags.privilege_withdrawn,
                x509.ReasonFlags.aa_compromise,
            )
        ),
    )

    cert = (
        x509.CertificateBuilder()
        .subject_name(new_subject)
        .issuer_name(root_cert.subject)
        .public_key(cert_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=30))
        .add_extension(
            x509.CRLDistributionPoints([crl_distribution_point]), critical=True
        )
        .sign(root_key, hashes.SHA256(), default_backend())
    )

    # print('new cert', cert.fingerprint(hashes.SHA256()))
    # Dump to scratch
    with open("scratch/new_cert.pem", "wb") as f:
        f.write(cert.public_bytes(encoding=serialization.Encoding.PEM))

    # Return PEM
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

    cert_key_pem = cert_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return cert_pem, cert_key_pem, cert.fingerprint(hashes.SHA1()).hex()


def apply_client_cert(phone, param, value):

    query = (
        AvailParam.select()
        .join(PhoneAvailParams)
        .where(PhoneAvailParams.phone == phone)
        .switch(AvailParam)
        .join(BaseParam, on=BaseParam.id == AvailParam.base_param)
        .where(BaseParam.name == param)
    )
    if query.exists():
        avail_param = query.get()
        avail_param.value = value
        avail_param.save()
    else:
        base_param = BaseParam.get(BaseParam.name == param)
        avail_param = AvailParam.create(
            base_param=base_param,
            value=value,
            note="Auto-generated due to inherited CA",
        )
        PhoneAvailParams.create(
            phone=phone,
            avail_param=avail_param,
            note="Auto-generated due to inherited CA",
        )


def issue_client_cert(phone):
    # Get our phone's CA from RSoP data

    query = PhoneActiveClientCert.select().where(PhoneActiveClientCert.phone == phone)

    # If phone has no active client cert, it is new so use RSoP
    if not query.exists():
        # Needs to be revisted once new phones can already be group members
        # Until then bypass
        cert_authority_rsop = CertAuthorityRSoP(phone)
        if cert_authority_rsop.current_cert_authority:
            cert_authority = cert_authority_rsop.current_cert_authority.cert_authority
    else:  # Use the currently active cert
        phone_active_client_cert = query.get()
        cert_authority = phone_active_client_cert.active_client_cert.cert_authority

    # Get client cert in PEM to add to DB
    client_cert_pem, client_key_pem, thumbprint = create_cert(
        cert_authority.cert,
        cert_authority.private_key,
        "fq.dn",  # url_for('get_certificate_revocation_list', thumbprint=cert_authority.thumbprint, _external=True)
    )
    # Create the client cert in DB
    client_cert = ClientCert.create(
        cert=client_cert_pem,
        private_key=client_key_pem,
        cert_authority=cert_authority,
        phone=phone,
    )
    # If query exists, update
    if query.exists():
        phone_active_client_cert = query.get()
        phone_active_client_cert.active_client_cert = client_cert
        phone_active_client_cert.save()
    # Else create
    else:
        PhoneActiveClientCert.create(phone=phone, active_client_cert=client_cert)

    # Determine if custom device cert already set

    param_values = [
        ("@device.sec.TLS.customDeviceCert1.set", 1),
        ("@device.sec.TLS.customDeviceCert1.publicCert", client_cert_pem),
        ("@device.sec.TLS.customDeviceCert1.privateKey", client_key_pem),
        ("@device.sec.TLS.profile.deviceCert1", 1),
    ]

    for param in param_values:
        apply_client_cert(phone, param[0], param[1])


# Need to add phase logic to revoke > reissue
# 1 - new cert has been sent
# 2 - phone has checked back in
# 3 - previous cert has been revoked
def reissue_client_cert(phone):

    revoke_client_cert(phone)
    issue_client_cert(phone)

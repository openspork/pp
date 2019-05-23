from OpenSSL import crypto
from ppapp.rsop.ca_rsop import CertAuthorityRSoP


def create_cert(public_key, private_key):
    ca = crypto.load_certificate(FILETYPE_PEM, public_key)
    print(vars(ca))


    pass




def issue_client_cert(phone):
    # Get our phone's CA from RSoP data
    cert_authority_rsop = CertAuthorityRSoP(phone)
    create_cert(
            cert_authority_rsop.current_cert_authority.public_key,
            cert_authority_rsop.current_cert_authority.private_key
        )

# Create the cert, assign it to the phone
# Mark the previous as cert needing to revoked
# When the phone next checks in revoke it
def reissue_client_cert(phone):
    issue_client_cert(phone)
    print(asdfasdfas)
    pass
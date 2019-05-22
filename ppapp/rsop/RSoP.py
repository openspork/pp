from ppapp.models import Phone, Group
from ppapp.util.group_ops import get_phone_groups, get_group_groups


class FoundCertAuthority:
    def __init__(self, cert_authority, group, depth):
        self.cert_authority = cert_authority
        self.group = group
        self.depth = depth

class CertAuthorityRSoP:
    def drill(self, group, depth):
        depth += 1
        if depth == 20:
            raise Exception("CA depth of %s reached!  Most likely a we have a loop!" % depth)
        # If this group is a CA
        if group.cert_authority:
            # Create the discovered CA
            found_cert_authority = FoundCertAuthority(group.cert_authority, group, depth)
            # If CA is not yet defined
            if not self.current_cert_authority:
                # Assign the CA to us
                self.current_cert_authority = found_cert_authority
            else:
                prev_depth = self.current_cert_authority.depth
                # If deeper, add to overrides
                if depth > prev_depth:
                    self.cert_authority_overrides.append(found_cert_authority)
                elif depth < prev_depth:
                    # If shallower, add current to overrides, set to us
                    self.cert_authority_overrides.append(self.current_cert_authority)
                    self.current_cert_authority = found_cert_authority
                elif depth == prev_depth:
                    precedence = group.type.precedence
                    curr_precedence = self.current_cert_authority.group.type.precedence
                    # Check by group priorities
                    if precedence > curr_precedence:
                        print('updating current ca')
                        # If higher, add current to overrides, set to us
                        self.cert_authority_overrides.append(self.current_cert_authority)
                        self.current_cert_authority = found_cert_authority
                    elif precedence < curr_precedence:
                        # If lower, add to overrides
                        self.cert_authority_overrides.append(found_cert_authority)
                    elif precedence == curr_precedence:
                        raise Exception(
                            "Duplicate CA of equal depth!  Cannot resolve!  CAs: %s, %s" % 
                            ( found_cert_authority.cert_authority.name, self.current_cert_authority.cert_authority.name )
                        )

        groups = get_group_groups(group, "parents")[1]
        if len(groups) > 0:
            for group in groups:
                self.drill(group, depth)


    def resolve_ca(self, groups):
        for group in groups:
            ca = self.drill(group, depth = 0)

    def __init__(self, phone):
        self.current_cert_authority = None
        self.cert_authority_overrides = []
        self.resolve_ca(get_phone_groups(phone)[1])

# Stub, TODO
class EffectiveParam():
    param = None
    owner = None
    depth = None
    overrides = []

class ParamRSoP:
    effective_params = [] # Keep an array of EffectiveParams

# Define an RSoP object that will be extensible for additional future RSoPs
class RSoP:
    def __init__(self, phone, certauthority_rsop, param, rsop):
        self.phone = phone
        self.certauthority_rsop = certauthority_rsop
        self.param_rsop = param_rsop








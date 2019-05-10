from peewee import *

database = MySQLDatabase('pp', **{'user': 'pp', 'use_unicode': True, 'password': 'password', 'charset': 'utf8', 'host': 'localhost', 'port': 3306})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Client(BaseModel):
    id = AutoField(column_name='ID')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'Client'

class Expansion(BaseModel):
    id = AutoField(column_name='ID')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'Expansion'

class Model(BaseModel):
    id = AutoField(column_name='ID')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'Model'

class Phone(BaseModel):
    id = AutoField(column_name='ID')
    mac_address = CharField(column_name='MACAddress')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'Phone'

class Site(BaseModel):
    id = AutoField(column_name='ID')
    name = CharField(column_name='Name')

    class Meta:
        table_name = 'Site'

class Vvxd60Handset(BaseModel):
    _vvxd60_handset_max_count = TextField(column_name='@VVXD60.handset.maxCount', null=True)
    _vvxd60_handset_max_count_vvx101 = TextField(column_name='@VVXD60.handset.maxCount.VVX101', null=True)
    _vvxd60_handset_max_count_vvx150 = TextField(column_name='@VVXD60.handset.maxCount.VVX150', null=True)
    _vvxd60_handset_max_count_vvx201 = TextField(column_name='@VVXD60.handset.maxCount.VVX201', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'VVXD60.handset'

class Call(BaseModel):
    _call_directed_call_pickup_string = TextField(column_name='@call.directedCallPickupString', null=True)
    _call_disable_mobile_calls = TextField(column_name='@call.disableMobileCalls', null=True)
    _call_parked_call_retrieve_string = TextField(column_name='@call.parkedCallRetrieveString', null=True)
    _call_parked_call_string = TextField(column_name='@call.parkedCallString', null=True)
    _call_sticky_auto_line_seize = TextField(column_name='@call.stickyAutoLineSeize', null=True)
    _call_url_number_mode_toggling = TextField(column_name='@call.urlNumberModeToggling', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call'

class CallinternationalDialing(BaseModel):
    _call_international_dialing_enabled = TextField(column_name='@call.internationalDialing.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call.internationalDialing'

class CallinternationalPrefix(BaseModel):
    _call_international_prefix_key = TextField(column_name='@call.internationalPrefix.key', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call.internationalPrefix'

class Callshared(BaseModel):
    _call_shared_remote_active_hold_as_active = TextField(column_name='@call.shared.remoteActiveHoldAsActive', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call.shared'

class CallstickyAutoLineSeize(BaseModel):
    _call_sticky_auto_line_seize_on_hook_dialing = TextField(column_name='@call.stickyAutoLineSeize.onHookDialing', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call.stickyAutoLineSeize'

class Callteluri(BaseModel):
    _call_teluri_show_prompt = TextField(column_name='@call.teluri.showPrompt', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'call.teluri'

class CallLists(BaseModel):
    _call_lists_collapse_duplicates = TextField(column_name='@callLists.collapseDuplicates', null=True)
    _call_lists_filter_all = TextField(column_name='@callLists.filterAll', null=True)
    _call_lists_filter_enabled = TextField(column_name='@callLists.filterEnabled', null=True)
    _call_lists_grouping = TextField(column_name='@callLists.grouping', null=True)
    _call_lists_log_consultation_calls = TextField(column_name='@callLists.logConsultationCalls', null=True)
    _call_lists_size = TextField(column_name='@callLists.size', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'callLists'

class CallListswriteDelay(BaseModel):
    _call_lists_write_delay_journal = TextField(column_name='@callLists.writeDelay.journal', null=True)
    _call_lists_write_delay_terminated = TextField(column_name='@callLists.writeDelay.terminated', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'callLists.writeDelay'

class Device(BaseModel):
    _device_hostname = TextField(column_name='@device.hostname', null=True)
    _device_set = TextField(column_name='@device.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device'

class Deviceauth(BaseModel):
    _device_auth_local_admin_password = TextField(column_name='@device.auth.localAdminPassword', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.auth'

class DeviceauthlocalAdminPassword(BaseModel):
    _device_auth_local_admin_password_set = TextField(column_name='@device.auth.localAdminPassword.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.auth.localAdminPassword'

class Devicedhcp(BaseModel):
    _device_dhcp_boot_srv_opt = TextField(column_name='@device.dhcp.bootSrvOpt', null=True)
    _device_dhcp_boot_srv_opt_type = TextField(column_name='@device.dhcp.bootSrvOptType', null=True)
    _device_dhcp_boot_srv_use_opt = TextField(column_name='@device.dhcp.bootSrvUseOpt', null=True)
    _device_dhcp_dhcp_vlan_disc_opt = TextField(column_name='@device.dhcp.dhcpVlanDiscOpt', null=True)
    _device_dhcp_dhcp_vlan_disc_use_opt = TextField(column_name='@device.dhcp.dhcpVlanDiscUseOpt', null=True)
    _device_dhcp_dhcpv6_vlan_disc_opt = TextField(column_name='@device.dhcp.dhcpv6VlanDiscOpt', null=True)
    _device_dhcp_enabled = TextField(column_name='@device.dhcp.enabled', null=True)
    _device_dhcp_option60_type = TextField(column_name='@device.dhcp.option60Type', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp'

class DevicedhcpbootSrvOpt(BaseModel):
    _device_dhcp_boot_srv_opt_set = TextField(column_name='@device.dhcp.bootSrvOpt.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.bootSrvOpt'

class DevicedhcpbootSrvOptType(BaseModel):
    _device_dhcp_boot_srv_opt_type_set = TextField(column_name='@device.dhcp.bootSrvOptType.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.bootSrvOptType'

class DevicedhcpbootSrvUseOpt(BaseModel):
    _device_dhcp_boot_srv_use_opt_set = TextField(column_name='@device.dhcp.bootSrvUseOpt.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.bootSrvUseOpt'

class DevicedhcpdhcpVlanDiscOpt(BaseModel):
    _device_dhcp_dhcp_vlan_disc_opt_set = TextField(column_name='@device.dhcp.dhcpVlanDiscOpt.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.dhcpVlanDiscOpt'

class DevicedhcpdhcpVlanDiscUseOpt(BaseModel):
    _device_dhcp_dhcp_vlan_disc_use_opt_set = TextField(column_name='@device.dhcp.dhcpVlanDiscUseOpt.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.dhcpVlanDiscUseOpt'

class Devicedhcpdhcpv6VlanDiscOpt(BaseModel):
    _device_dhcp_dhcpv6_vlan_disc_opt_set = TextField(column_name='@device.dhcp.dhcpv6VlanDiscOpt.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.dhcpv6VlanDiscOpt'

class Devicedhcpenabled(BaseModel):
    _device_dhcp_enabled_set = TextField(column_name='@device.dhcp.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.enabled'

class Devicedhcpoption60Type(BaseModel):
    _device_dhcp_option60_type_set = TextField(column_name='@device.dhcp.option60Type.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dhcp.option60Type'

class Devicedns(BaseModel):
    _device_dns_alt_srv_address = TextField(column_name='@device.dns.altSrvAddress', null=True)
    _device_dns_domain = TextField(column_name='@device.dns.domain', null=True)
    _device_dns_server_address = TextField(column_name='@device.dns.serverAddress', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dns'

class DevicednsaltSrvAddress(BaseModel):
    _device_dns_alt_srv_address_set = TextField(column_name='@device.dns.altSrvAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dns.altSrvAddress'

class Devicednsdomain(BaseModel):
    _device_dns_domain_set = TextField(column_name='@device.dns.domain.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dns.domain'

class DevicednsserverAddress(BaseModel):
    _device_dns_server_address_set = TextField(column_name='@device.dns.serverAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.dns.serverAddress'

class Devicehostname(BaseModel):
    _device_hostname_set = TextField(column_name='@device.hostname.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.hostname'

class Deviceicmp(BaseModel):
    _device_icmp_ipv4_icmp_ignore_redirect = TextField(column_name='@device.icmp.ipv4IcmpIgnoreRedirect', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.icmp'

class Deviceicmpipv4IcmpIgnoreRedirect(BaseModel):
    _device_icmp_ipv4_icmp_ignore_redirect_set = TextField(column_name='@device.icmp.ipv4IcmpIgnoreRedirect.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.icmp.ipv4IcmpIgnoreRedirect'

class Devicemac(BaseModel):
    _device_mac_hide = TextField(column_name='@device.mac.hide', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.mac'

class Devicemachide(BaseModel):
    _device_mac_hide_set = TextField(column_name='@device.mac.hide.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.mac.hide'

class Devicenet(BaseModel):
    _device_net_i_pgateway = TextField(column_name='@device.net.IPgateway', null=True)
    _device_net_cached_ip_address = TextField(column_name='@device.net.cachedIPAddress', null=True)
    _device_net_cached_ip_address_retry_time = TextField(column_name='@device.net.cachedIPAddressRetryTime', null=True)
    _device_net_cdp_enabled = TextField(column_name='@device.net.cdpEnabled', null=True)
    _device_net_enabled = TextField(column_name='@device.net.enabled', null=True)
    _device_net_ether_mode_lan = TextField(column_name='@device.net.etherModeLAN', null=True)
    _device_net_ether_mode_pc = TextField(column_name='@device.net.etherModePC', null=True)
    _device_net_ether_storm_filter = TextField(column_name='@device.net.etherStormFilter', null=True)
    _device_net_ether_storm_filter_pps_value = TextField(column_name='@device.net.etherStormFilterPpsValue', null=True)
    _device_net_ether_vlan_filter = TextField(column_name='@device.net.etherVlanFilter', null=True)
    _device_net_ip_stack = TextField(column_name='@device.net.ipStack', null=True)
    _device_net_ipv6_addr_disc = TextField(column_name='@device.net.ipv6AddrDisc', null=True)
    _device_net_ipv6_address = TextField(column_name='@device.net.ipv6Address', null=True)
    _device_net_ipv6_gateway = TextField(column_name='@device.net.ipv6Gateway', null=True)
    _device_net_ipv6_link_address = TextField(column_name='@device.net.ipv6LinkAddress', null=True)
    _device_net_ipv6_privacy_extension = TextField(column_name='@device.net.ipv6PrivacyExtension', null=True)
    _device_net_ipv6_ula_address = TextField(column_name='@device.net.ipv6ULAAddress', null=True)
    _device_net_lldp_capabilities_required = TextField(column_name='@device.net.lldpCapabilitiesRequired', null=True)
    _device_net_lldp_enabled = TextField(column_name='@device.net.lldpEnabled', null=True)
    _device_net_lldp_fast_start_count = TextField(column_name='@device.net.lldpFastStartCount', null=True)
    _device_net_preferred_network = TextField(column_name='@device.net.preferredNetwork', null=True)
    _device_net_subnet_mask = TextField(column_name='@device.net.subnetMask', null=True)
    _device_net_vlan_id = TextField(column_name='@device.net.vlanId', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net'

class DevicenetiPgateway(BaseModel):
    _device_net_i_pgateway_set = TextField(column_name='@device.net.IPgateway.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.IPgateway'

class DevicenetcachedIpAddress(BaseModel):
    _device_net_cached_ip_address_set = TextField(column_name='@device.net.cachedIPAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.cachedIPAddress'

class DevicenetcachedIpAddressRetryTime(BaseModel):
    _device_net_cached_ip_address_retry_time_set = TextField(column_name='@device.net.cachedIPAddressRetryTime.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.cachedIPAddressRetryTime'

class DevicenetcdpEnabled(BaseModel):
    _device_net_cdp_enabled_set = TextField(column_name='@device.net.cdpEnabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.cdpEnabled'

class Devicenetdot1X(BaseModel):
    _device_net_dot1x_anonid = TextField(column_name='@device.net.dot1x.anonid', null=True)
    _device_net_dot1x_eap_fast_in_band_prov = TextField(column_name='@device.net.dot1x.eapFastInBandProv', null=True)
    _device_net_dot1x_enabled = TextField(column_name='@device.net.dot1x.enabled', null=True)
    _device_net_dot1x_identity = TextField(column_name='@device.net.dot1x.identity', null=True)
    _device_net_dot1x_method = TextField(column_name='@device.net.dot1x.method', null=True)
    _device_net_dot1x_password = TextField(column_name='@device.net.dot1x.password', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x'

class Devicenetdot1Xanonid(BaseModel):
    _device_net_dot1x_anonid_set = TextField(column_name='@device.net.dot1x.anonid.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.anonid'

class Devicenetdot1XeapFastInBandProv(BaseModel):
    _device_net_dot1x_eap_fast_in_band_prov_set = TextField(column_name='@device.net.dot1x.eapFastInBandProv.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.eapFastInBandProv'

class Devicenetdot1Xenabled(BaseModel):
    _device_net_dot1x_enabled_set = TextField(column_name='@device.net.dot1x.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.enabled'

class Devicenetdot1Xidentity(BaseModel):
    _device_net_dot1x_identity_set = TextField(column_name='@device.net.dot1x.identity.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.identity'

class Devicenetdot1Xmethod(BaseModel):
    _device_net_dot1x_method_set = TextField(column_name='@device.net.dot1x.method.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.method'

class Devicenetdot1Xpassword(BaseModel):
    _device_net_dot1x_password_set = TextField(column_name='@device.net.dot1x.password.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.dot1x.password'

class Devicenetenabled(BaseModel):
    _device_net_enabled_set = TextField(column_name='@device.net.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.enabled'

class DevicenetetherModeLan(BaseModel):
    _device_net_ether_mode_lan_set = TextField(column_name='@device.net.etherModeLAN.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.etherModeLAN'

class DevicenetetherModePc(BaseModel):
    _device_net_ether_mode_pc_set = TextField(column_name='@device.net.etherModePC.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.etherModePC'

class DevicenetetherStormFilter(BaseModel):
    _device_net_ether_storm_filter_set = TextField(column_name='@device.net.etherStormFilter.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.etherStormFilter'

class DevicenetetherStormFilterPpsValue(BaseModel):
    _device_net_ether_storm_filter_pps_value_set = TextField(column_name='@device.net.etherStormFilterPpsValue.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.etherStormFilterPpsValue'

class DevicenetetherVlanFilter(BaseModel):
    _device_net_ether_vlan_filter_set = TextField(column_name='@device.net.etherVlanFilter.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.etherVlanFilter'

class Deviceneticmp(BaseModel):
    _device_net_icmp_echo_replies_mask = TextField(column_name='@device.net.icmp.echoRepliesMask', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.icmp'

class DeviceneticmpechoRepliesMask(BaseModel):
    _device_net_icmp_echo_replies_mask_set = TextField(column_name='@device.net.icmp.echoRepliesMask.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.icmp.echoRepliesMask'

class DevicenetipStack(BaseModel):
    _device_net_ip_stack_set = TextField(column_name='@device.net.ipStack.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipStack'

class Devicenetipv6AddrDisc(BaseModel):
    _device_net_ipv6_addr_disc_set = TextField(column_name='@device.net.ipv6AddrDisc.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6AddrDisc'

class Devicenetipv6Address(BaseModel):
    _device_net_ipv6_address_set = TextField(column_name='@device.net.ipv6Address.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6Address'

class Devicenetipv6Gateway(BaseModel):
    _device_net_ipv6_gateway_set = TextField(column_name='@device.net.ipv6Gateway.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6Gateway'

class Devicenetipv6LinkAddress(BaseModel):
    _device_net_ipv6_link_address_set = TextField(column_name='@device.net.ipv6LinkAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6LinkAddress'

class Devicenetipv6PrivacyExtension(BaseModel):
    _device_net_ipv6_privacy_extension_set = TextField(column_name='@device.net.ipv6PrivacyExtension.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6PrivacyExtension'

class Devicenetipv6UlaAddress(BaseModel):
    _device_net_ipv6_ula_address_set = TextField(column_name='@device.net.ipv6ULAAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.ipv6ULAAddress'

class DevicenetlldpCapabilitiesRequired(BaseModel):
    _device_net_lldp_capabilities_required_set = TextField(column_name='@device.net.lldpCapabilitiesRequired.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.lldpCapabilitiesRequired'

class DevicenetlldpEnabled(BaseModel):
    _device_net_lldp_enabled_set = TextField(column_name='@device.net.lldpEnabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.lldpEnabled'

class DevicenetlldpFastStartCount(BaseModel):
    _device_net_lldp_fast_start_count_set = TextField(column_name='@device.net.lldpFastStartCount.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.lldpFastStartCount'

class DevicenetpreferredNetwork(BaseModel):
    _device_net_preferred_network_set = TextField(column_name='@device.net.preferredNetwork.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.preferredNetwork'

class DevicenetsubnetMask(BaseModel):
    _device_net_subnet_mask_set = TextField(column_name='@device.net.subnetMask.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.subnetMask'

class DevicenetvlanId(BaseModel):
    _device_net_vlan_id_set = TextField(column_name='@device.net.vlanId.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.net.vlanId'

class Devicepacfile(BaseModel):
    _device_pacfile_data = TextField(column_name='@device.pacfile.data', null=True)
    _device_pacfile_password = TextField(column_name='@device.pacfile.password', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.pacfile'

class Devicepacfiledata(BaseModel):
    _device_pacfile_data_set = TextField(column_name='@device.pacfile.data.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.pacfile.data'

class Devicepacfilepassword(BaseModel):
    _device_pacfile_password_set = TextField(column_name='@device.pacfile.password.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.pacfile.password'

class Deviceprov(BaseModel):
    _device_prov_clink_enabled = TextField(column_name='@device.prov.clinkEnabled', null=True)
    _device_prov_lync_device_update_enabled = TextField(column_name='@device.prov.lyncDeviceUpdateEnabled', null=True)
    _device_prov_max_redun_servers = TextField(column_name='@device.prov.maxRedunServers', null=True)
    _device_prov_password = TextField(column_name='@device.prov.password', null=True)
    _device_prov_redun_attempt_limit = TextField(column_name='@device.prov.redunAttemptLimit', null=True)
    _device_prov_redun_inter_attempt_delay = TextField(column_name='@device.prov.redunInterAttemptDelay', null=True)
    _device_prov_server_name = TextField(column_name='@device.prov.serverName', null=True)
    _device_prov_server_type = TextField(column_name='@device.prov.serverType', null=True)
    _device_prov_tag_serial_no = TextField(column_name='@device.prov.tagSerialNo', null=True)
    _device_prov_upgrade_server = TextField(column_name='@device.prov.upgradeServer', null=True)
    _device_prov_user = TextField(column_name='@device.prov.user', null=True)
    _device_prov_ztp_enabled = TextField(column_name='@device.prov.ztpEnabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov'

class DeviceprovclinkEnabled(BaseModel):
    _device_prov_clink_enabled_set = TextField(column_name='@device.prov.clinkEnabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.clinkEnabled'

class DeviceprovcurlPartialFileError(BaseModel):
    _device_prov_curl_partial_file_error_enabled = TextField(column_name='@device.prov.curlPartialFileError.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.curlPartialFileError'

class DeviceprovcurlPartialFileErrorenabled(BaseModel):
    _device_prov_curl_partial_file_error_enabled_set = TextField(column_name='@device.prov.curlPartialFileError.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.curlPartialFileError.enabled'

class DeviceprovlyncDeviceUpdateEnabled(BaseModel):
    _device_prov_lync_device_update_enabled_set = TextField(column_name='@device.prov.lyncDeviceUpdateEnabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.lyncDeviceUpdateEnabled'

class DeviceprovmaxRedunServers(BaseModel):
    _device_prov_max_redun_servers_set = TextField(column_name='@device.prov.maxRedunServers.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.maxRedunServers'

class Deviceprovpassword(BaseModel):
    _device_prov_password_set = TextField(column_name='@device.prov.password.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.password'

class DeviceprovredunAttemptLimit(BaseModel):
    _device_prov_redun_attempt_limit_set = TextField(column_name='@device.prov.redunAttemptLimit.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.redunAttemptLimit'

class DeviceprovredunInterAttemptDelay(BaseModel):
    _device_prov_redun_inter_attempt_delay_set = TextField(column_name='@device.prov.redunInterAttemptDelay.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.redunInterAttemptDelay'

class DeviceprovserverName(BaseModel):
    _device_prov_server_name_set = TextField(column_name='@device.prov.serverName.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.serverName'

class DeviceprovserverType(BaseModel):
    _device_prov_server_type_set = TextField(column_name='@device.prov.serverType.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.serverType'

class DeviceprovtagSerialNo(BaseModel):
    _device_prov_tag_serial_no_set = TextField(column_name='@device.prov.tagSerialNo.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.tagSerialNo'

class DeviceprovupgradeServer(BaseModel):
    _device_prov_upgrade_server_set = TextField(column_name='@device.prov.upgradeServer.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.upgradeServer'

class Deviceprovuser(BaseModel):
    _device_prov_user_set = TextField(column_name='@device.prov.user.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.user'

class DeviceprovztpEnabled(BaseModel):
    _device_prov_ztp_enabled_set = TextField(column_name='@device.prov.ztpEnabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.prov.ztpEnabled'

class Devicesectls(BaseModel):
    _device_sec_tls_custom_ca_cert1 = TextField(column_name='@device.sec.TLS.customCaCert1', null=True)
    _device_sec_tls_custom_ca_cert2 = TextField(column_name='@device.sec.TLS.customCaCert2', null=True)
    _device_sec_tls_custom_ca_cert3 = TextField(column_name='@device.sec.TLS.customCaCert3', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS'

class Devicesectlsfips(BaseModel):
    _device_sec_tls_fips_enabled = TextField(column_name='@device.sec.TLS.FIPS.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.FIPS'

class Devicesectlsfipsenabled(BaseModel):
    _device_sec_tls_fips_enabled_set = TextField(column_name='@device.sec.TLS.FIPS.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.FIPS.enabled'

class Devicesectlsocsp(BaseModel):
    _device_sec_tls_ocsp_enabled = TextField(column_name='@device.sec.TLS.OCSP.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.OCSP'

class Devicesectlsocspenabled(BaseModel):
    _device_sec_tls_ocsp_enabled_set = TextField(column_name='@device.sec.TLS.OCSP.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.OCSP.enabled'

class DevicesectlscustomCaCert1(BaseModel):
    _device_sec_tls_custom_ca_cert1_set = TextField(column_name='@device.sec.TLS.customCaCert1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customCaCert1'

class DevicesectlscustomCaCert2(BaseModel):
    _device_sec_tls_custom_ca_cert2_set = TextField(column_name='@device.sec.TLS.customCaCert2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customCaCert2'

class DevicesectlscustomCaCert3(BaseModel):
    _device_sec_tls_custom_ca_cert3_set = TextField(column_name='@device.sec.TLS.customCaCert3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customCaCert3'

class DevicesectlscustomDeviceCert1(BaseModel):
    _device_sec_tls_custom_device_cert1_set = TextField(column_name='@device.sec.TLS.customDeviceCert1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customDeviceCert1'

class DevicesectlscustomDeviceCert2(BaseModel):
    _device_sec_tls_custom_device_cert2_set = TextField(column_name='@device.sec.TLS.customDeviceCert2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customDeviceCert2'

class DevicesectlscustomDeviceCert3(BaseModel):
    _device_sec_tls_custom_device_cert3_set = TextField(column_name='@device.sec.TLS.customDeviceCert3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.customDeviceCert3'

class Devicesectlsdot1X(BaseModel):
    _device_sec_tls_dot1x_strict_cert_common_name_validation = TextField(column_name='@device.sec.TLS.dot1x.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.dot1x'

class Devicesectlsdot1XstrictCertCommonNameValidation(BaseModel):
    _device_sec_tls_dot1x_strict_cert_common_name_validation_set = TextField(column_name='@device.sec.TLS.dot1x.strictCertCommonNameValidation.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.dot1x.strictCertCommonNameValidation'

class Devicesectlsprofile(BaseModel):
    _device_sec_tls_profile_ca_cert_list1 = TextField(column_name='@device.sec.TLS.profile.caCertList1', null=True)
    _device_sec_tls_profile_ca_cert_list2 = TextField(column_name='@device.sec.TLS.profile.caCertList2', null=True)
    _device_sec_tls_profile_ca_cert_list3 = TextField(column_name='@device.sec.TLS.profile.caCertList3', null=True)
    _device_sec_tls_profile_cipher_suite1 = TextField(column_name='@device.sec.TLS.profile.cipherSuite1', null=True)
    _device_sec_tls_profile_cipher_suite2 = TextField(column_name='@device.sec.TLS.profile.cipherSuite2', null=True)
    _device_sec_tls_profile_cipher_suite3 = TextField(column_name='@device.sec.TLS.profile.cipherSuite3', null=True)
    _device_sec_tls_profile_cipher_suite_default1 = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault1', null=True)
    _device_sec_tls_profile_cipher_suite_default2 = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault2', null=True)
    _device_sec_tls_profile_cipher_suite_default3 = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault3', null=True)
    _device_sec_tls_profile_device_cert1 = TextField(column_name='@device.sec.TLS.profile.deviceCert1', null=True)
    _device_sec_tls_profile_device_cert2 = TextField(column_name='@device.sec.TLS.profile.deviceCert2', null=True)
    _device_sec_tls_profile_device_cert3 = TextField(column_name='@device.sec.TLS.profile.deviceCert3', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile'

class DevicesectlsprofilecaCertList1(BaseModel):
    _device_sec_tls_profile_ca_cert_list1_set = TextField(column_name='@device.sec.TLS.profile.caCertList1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.caCertList1'

class DevicesectlsprofilecaCertList2(BaseModel):
    _device_sec_tls_profile_ca_cert_list2_set = TextField(column_name='@device.sec.TLS.profile.caCertList2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.caCertList2'

class DevicesectlsprofilecaCertList3(BaseModel):
    _device_sec_tls_profile_ca_cert_list3_set = TextField(column_name='@device.sec.TLS.profile.caCertList3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.caCertList3'

class DevicesectlsprofilecipherSuite1(BaseModel):
    _device_sec_tls_profile_cipher_suite1_set = TextField(column_name='@device.sec.TLS.profile.cipherSuite1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuite1'

class DevicesectlsprofilecipherSuite2(BaseModel):
    _device_sec_tls_profile_cipher_suite2_set = TextField(column_name='@device.sec.TLS.profile.cipherSuite2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuite2'

class DevicesectlsprofilecipherSuite3(BaseModel):
    _device_sec_tls_profile_cipher_suite3_set = TextField(column_name='@device.sec.TLS.profile.cipherSuite3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuite3'

class DevicesectlsprofilecipherSuiteDefault1(BaseModel):
    _device_sec_tls_profile_cipher_suite_default1_set = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuiteDefault1'

class DevicesectlsprofilecipherSuiteDefault2(BaseModel):
    _device_sec_tls_profile_cipher_suite_default2_set = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuiteDefault2'

class DevicesectlsprofilecipherSuiteDefault3(BaseModel):
    _device_sec_tls_profile_cipher_suite_default3_set = TextField(column_name='@device.sec.TLS.profile.cipherSuiteDefault3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.cipherSuiteDefault3'

class DevicesectlsprofiledeviceCert1(BaseModel):
    _device_sec_tls_profile_device_cert1_set = TextField(column_name='@device.sec.TLS.profile.deviceCert1.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.deviceCert1'

class DevicesectlsprofiledeviceCert2(BaseModel):
    _device_sec_tls_profile_device_cert2_set = TextField(column_name='@device.sec.TLS.profile.deviceCert2.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.deviceCert2'

class DevicesectlsprofiledeviceCert3(BaseModel):
    _device_sec_tls_profile_device_cert3_set = TextField(column_name='@device.sec.TLS.profile.deviceCert3.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profile.deviceCert3'

class DevicesectlsprofileSelection(BaseModel):
    _device_sec_tls_profile_selection_dot1x = TextField(column_name='@device.sec.TLS.profileSelection.dot1x', null=True)
    _device_sec_tls_profile_selection_provisioning = TextField(column_name='@device.sec.TLS.profileSelection.provisioning', null=True)
    _device_sec_tls_profile_selection_syslog = TextField(column_name='@device.sec.TLS.profileSelection.syslog', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profileSelection'

class DevicesectlsprofileSelectiondot1X(BaseModel):
    _device_sec_tls_profile_selection_dot1x_set = TextField(column_name='@device.sec.TLS.profileSelection.dot1x.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profileSelection.dot1x'

class DevicesectlsprofileSelectionprovisioning(BaseModel):
    _device_sec_tls_profile_selection_provisioning_set = TextField(column_name='@device.sec.TLS.profileSelection.provisioning.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profileSelection.provisioning'

class DevicesectlsprofileSelectionsyslog(BaseModel):
    _device_sec_tls_profile_selection_syslog_set = TextField(column_name='@device.sec.TLS.profileSelection.syslog.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.profileSelection.syslog'

class Devicesectlsprotocol(BaseModel):
    _device_sec_tls_protocol_dot1x = TextField(column_name='@device.sec.TLS.protocol.dot1x', null=True)
    _device_sec_tls_protocol_prov = TextField(column_name='@device.sec.TLS.protocol.prov', null=True)
    _device_sec_tls_protocol_syslog = TextField(column_name='@device.sec.TLS.protocol.syslog', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.protocol'

class Devicesectlsprotocoldot1X(BaseModel):
    _device_sec_tls_protocol_dot1x_set = TextField(column_name='@device.sec.TLS.protocol.dot1x.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.protocol.dot1x'

class Devicesectlsprotocolprov(BaseModel):
    _device_sec_tls_protocol_prov_set = TextField(column_name='@device.sec.TLS.protocol.prov.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.protocol.prov'

class Devicesectlsprotocolsyslog(BaseModel):
    _device_sec_tls_protocol_syslog_set = TextField(column_name='@device.sec.TLS.protocol.syslog.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.protocol.syslog'

class Devicesectlsprov(BaseModel):
    _device_sec_tls_prov_strict_cert_common_name_validation = TextField(column_name='@device.sec.TLS.prov.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.prov'

class DevicesectlsprovstrictCertCommonNameValidation(BaseModel):
    _device_sec_tls_prov_strict_cert_common_name_validation_set = TextField(column_name='@device.sec.TLS.prov.strictCertCommonNameValidation.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.prov.strictCertCommonNameValidation'

class Devicesectlssyslog(BaseModel):
    _device_sec_tls_syslog_strict_cert_common_name_validation = TextField(column_name='@device.sec.TLS.syslog.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.syslog'

class DevicesectlssyslogstrictCertCommonNameValidation(BaseModel):
    _device_sec_tls_syslog_strict_cert_common_name_validation_set = TextField(column_name='@device.sec.TLS.syslog.strictCertCommonNameValidation.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.TLS.syslog.strictCertCommonNameValidation'

class DevicesecconfigEncryption(BaseModel):
    _device_sec_config_encryption_key = TextField(column_name='@device.sec.configEncryption.key', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.configEncryption'

class DevicesecconfigEncryptionkey(BaseModel):
    _device_sec_config_encryption_key_set = TextField(column_name='@device.sec.configEncryption.key.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.configEncryption.key'

class DeviceseccoreDumpEncryption(BaseModel):
    _device_sec_core_dump_encryption_enabled = TextField(column_name='@device.sec.coreDumpEncryption.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.coreDumpEncryption'

class DeviceseccoreDumpEncryptionenabled(BaseModel):
    _device_sec_core_dump_encryption_enabled_set = TextField(column_name='@device.sec.coreDumpEncryption.enabled.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sec.coreDumpEncryption.enabled'

class Devicesntp(BaseModel):
    _device_sntp_gmt_offset = TextField(column_name='@device.sntp.gmtOffset', null=True)
    _device_sntp_gmt_offsetcity_id = TextField(column_name='@device.sntp.gmtOffsetcityID', null=True)
    _device_sntp_server_name = TextField(column_name='@device.sntp.serverName', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sntp'

class DevicesntpgmtOffset(BaseModel):
    _device_sntp_gmt_offset_set = TextField(column_name='@device.sntp.gmtOffset.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sntp.gmtOffset'

class DevicesntpgmtOffsetcityId(BaseModel):
    _device_sntp_gmt_offsetcity_id_set = TextField(column_name='@device.sntp.gmtOffsetcityID.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sntp.gmtOffsetcityID'

class DevicesntpserverName(BaseModel):
    _device_sntp_server_name_set = TextField(column_name='@device.sntp.serverName.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.sntp.serverName'

class Devicesyslog(BaseModel):
    _device_syslog_facility = TextField(column_name='@device.syslog.facility', null=True)
    _device_syslog_prepend_mac = TextField(column_name='@device.syslog.prependMac', null=True)
    _device_syslog_render_level = TextField(column_name='@device.syslog.renderLevel', null=True)
    _device_syslog_server_name = TextField(column_name='@device.syslog.serverName', null=True)
    _device_syslog_transport = TextField(column_name='@device.syslog.transport', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog'

class Devicesyslogfacility(BaseModel):
    _device_syslog_facility_set = TextField(column_name='@device.syslog.facility.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog.facility'

class DevicesyslogprependMac(BaseModel):
    _device_syslog_prepend_mac_set = TextField(column_name='@device.syslog.prependMac.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog.prependMac'

class DevicesyslogrenderLevel(BaseModel):
    _device_syslog_render_level_set = TextField(column_name='@device.syslog.renderLevel.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog.renderLevel'

class DevicesyslogserverName(BaseModel):
    _device_syslog_server_name_set = TextField(column_name='@device.syslog.serverName.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog.serverName'

class Devicesyslogtransport(BaseModel):
    _device_syslog_transport_set = TextField(column_name='@device.syslog.transport.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.syslog.transport'

class Deviceusbnet(BaseModel):
    _device_usbnet_ip_stack = TextField(column_name='@device.usbnet.ipStack', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.usbnet'

class DeviceusbnetipStack(BaseModel):
    _device_usbnet_ip_stack_set = TextField(column_name='@device.usbnet.ipStack.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.usbnet.ipStack'

class Deviceusbnetipv6AddrDisc(BaseModel):
    _device_usbnet_ipv6_addr_disc_set = TextField(column_name='@device.usbnet.ipv6AddrDisc.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.usbnet.ipv6AddrDisc'

class DeviceusbnetpreferredNetwork(BaseModel):
    _device_usbnet_preferred_network_set = TextField(column_name='@device.usbnet.preferredNetwork.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.usbnet.preferredNetwork'

class Devicewifi(BaseModel):
    _device_wifi_ip_gateway = TextField(column_name='@device.wifi.ipGateway', null=True)
    _device_wifi_ip_stack = TextField(column_name='@device.wifi.ipStack', null=True)
    _device_wifi_ipv6_addr_disc = TextField(column_name='@device.wifi.ipv6AddrDisc', null=True)
    _device_wifi_ipv6_address = TextField(column_name='@device.wifi.ipv6Address', null=True)
    _device_wifi_ipv6_gateway = TextField(column_name='@device.wifi.ipv6Gateway', null=True)
    _device_wifi_ipv6_link_address = TextField(column_name='@device.wifi.ipv6LinkAddress', null=True)
    _device_wifi_ipv6_privacy_extension = TextField(column_name='@device.wifi.ipv6PrivacyExtension', null=True)
    _device_wifi_ipv6_ula_address = TextField(column_name='@device.wifi.ipv6ULAAddress', null=True)
    _device_wifi_preferred_network = TextField(column_name='@device.wifi.preferredNetwork', null=True)
    _device_wifi_subnet_mask = TextField(column_name='@device.wifi.subnetMask', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi'

class DevicewifiipGateway(BaseModel):
    _device_wifi_ip_gateway_set = TextField(column_name='@device.wifi.ipGateway.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipGateway'

class DevicewifiipStack(BaseModel):
    _device_wifi_ip_stack_set = TextField(column_name='@device.wifi.ipStack.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipStack'

class Devicewifiipv6AddrDisc(BaseModel):
    _device_wifi_ipv6_addr_disc_set = TextField(column_name='@device.wifi.ipv6AddrDisc.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6AddrDisc'

class Devicewifiipv6Address(BaseModel):
    _device_wifi_ipv6_address_set = TextField(column_name='@device.wifi.ipv6Address.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6Address'

class Devicewifiipv6Gateway(BaseModel):
    _device_wifi_ipv6_gateway_set = TextField(column_name='@device.wifi.ipv6Gateway.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6Gateway'

class Devicewifiipv6LinkAddress(BaseModel):
    _device_wifi_ipv6_link_address_set = TextField(column_name='@device.wifi.ipv6LinkAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6LinkAddress'

class Devicewifiipv6PrivacyExtension(BaseModel):
    _device_wifi_ipv6_privacy_extension_set = TextField(column_name='@device.wifi.ipv6PrivacyExtension.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6PrivacyExtension'

class Devicewifiipv6UlaAddress(BaseModel):
    _device_wifi_ipv6_ula_address_set = TextField(column_name='@device.wifi.ipv6ULAAddress.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.ipv6ULAAddress'

class DevicewifipreferredNetwork(BaseModel):
    _device_wifi_preferred_network_set = TextField(column_name='@device.wifi.preferredNetwork.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.preferredNetwork'

class DevicewifisubnetMask(BaseModel):
    _device_wifi_subnet_mask_set = TextField(column_name='@device.wifi.subnetMask.set', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'device.wifi.subnetMask'

class DiagsserviceAssurance(BaseModel):
    _diags_service_assurance__upload_path = TextField(column_name='@diags.serviceAssurance.UploadPath', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'diags.serviceAssurance'

class Dialplan(BaseModel):
    _dialplan_1_apply_to_call_list_dial = TextField(column_name='@dialplan.1.applyToCallListDial', null=True)
    _dialplan_1_apply_to_directory_dial = TextField(column_name='@dialplan.1.applyToDirectoryDial', null=True)
    _dialplan_1_apply_to_forward = TextField(column_name='@dialplan.1.applyToForward', null=True)
    _dialplan_1_apply_to_tel_uri_dial = TextField(column_name='@dialplan.1.applyToTelUriDial', null=True)
    _dialplan_1_apply_to_user_dial = TextField(column_name='@dialplan.1.applyToUserDial', null=True)
    _dialplan_1_apply_to_user_send = TextField(column_name='@dialplan.1.applyToUserSend', null=True)
    _dialplan_1_conflict_match_handling = TextField(column_name='@dialplan.1.conflictMatchHandling', null=True)
    _dialplan_1_digitmap = TextField(column_name='@dialplan.1.digitmap', null=True)
    _dialplan_1_digitmap_time_out = TextField(column_name='@dialplan.1.digitmap.timeOut', null=True)
    _dialplan_1_e911dialmask = TextField(column_name='@dialplan.1.e911dialmask', null=True)
    _dialplan_1_e911dialstring = TextField(column_name='@dialplan.1.e911dialstring', null=True)
    _dialplan_1_impossible_match_handling = TextField(column_name='@dialplan.1.impossibleMatchHandling', null=True)
    _dialplan_1_impossible_match_handling_time_out = TextField(column_name='@dialplan.1.impossibleMatchHandling.timeOut', null=True)
    _dialplan_1_lync_digitmap_time_out = TextField(column_name='@dialplan.1.lyncDigitmap.timeOut', null=True)
    _dialplan_1_originaldigitmap = TextField(column_name='@dialplan.1.originaldigitmap', null=True)
    _dialplan_1_remove_end_of_dial = TextField(column_name='@dialplan.1.removeEndOfDial', null=True)
    _dialplan_1_routing_emergency_1_server_1 = TextField(column_name='@dialplan.1.routing.emergency.1.server.1', null=True)
    _dialplan_1_routing_emergency_1_server_2 = TextField(column_name='@dialplan.1.routing.emergency.1.server.2', null=True)
    _dialplan_1_routing_emergency_1_server_3 = TextField(column_name='@dialplan.1.routing.emergency.1.server.3', null=True)
    _dialplan_1_routing_emergency_1_value = TextField(column_name='@dialplan.1.routing.emergency.1.value', null=True)
    _dialplan_1_routing_emergency_2_server_1 = TextField(column_name='@dialplan.1.routing.emergency.2.server.1', null=True)
    _dialplan_1_routing_emergency_2_server_2 = TextField(column_name='@dialplan.1.routing.emergency.2.server.2', null=True)
    _dialplan_1_routing_emergency_2_server_3 = TextField(column_name='@dialplan.1.routing.emergency.2.server.3', null=True)
    _dialplan_1_routing_emergency_2_value = TextField(column_name='@dialplan.1.routing.emergency.2.value', null=True)
    _dialplan_1_routing_server_1_address = TextField(column_name='@dialplan.1.routing.server.1.address', null=True)
    _dialplan_1_routing_server_1_port = TextField(column_name='@dialplan.1.routing.server.1.port', null=True)
    _dialplan_1_routing_server_1_transport = TextField(column_name='@dialplan.1.routing.server.1.transport', null=True)
    _dialplan_1_routing_server_2_address = TextField(column_name='@dialplan.1.routing.server.2.address', null=True)
    _dialplan_1_routing_server_2_port = TextField(column_name='@dialplan.1.routing.server.2.port', null=True)
    _dialplan_1_routing_server_2_transport = TextField(column_name='@dialplan.1.routing.server.2.transport', null=True)
    _dialplan_2_apply_to_call_list_dial = TextField(column_name='@dialplan.2.applyToCallListDial', null=True)
    _dialplan_2_apply_to_directory_dial = TextField(column_name='@dialplan.2.applyToDirectoryDial', null=True)
    _dialplan_2_apply_to_forward = TextField(column_name='@dialplan.2.applyToForward', null=True)
    _dialplan_2_apply_to_tel_uri_dial = TextField(column_name='@dialplan.2.applyToTelUriDial', null=True)
    _dialplan_2_apply_to_user_dial = TextField(column_name='@dialplan.2.applyToUserDial', null=True)
    _dialplan_2_apply_to_user_send = TextField(column_name='@dialplan.2.applyToUserSend', null=True)
    _dialplan_2_conflict_match_handling = TextField(column_name='@dialplan.2.conflictMatchHandling', null=True)
    _dialplan_2_digitmap = TextField(column_name='@dialplan.2.digitmap', null=True)
    _dialplan_2_digitmap_time_out = TextField(column_name='@dialplan.2.digitmap.timeOut', null=True)
    _dialplan_2_e911dialmask = TextField(column_name='@dialplan.2.e911dialmask', null=True)
    _dialplan_2_e911dialstring = TextField(column_name='@dialplan.2.e911dialstring', null=True)
    _dialplan_2_impossible_match_handling = TextField(column_name='@dialplan.2.impossibleMatchHandling', null=True)
    _dialplan_2_impossible_match_handling_time_out = TextField(column_name='@dialplan.2.impossibleMatchHandling.timeOut', null=True)
    _dialplan_2_lync_digitmap_time_out = TextField(column_name='@dialplan.2.lyncDigitmap.timeOut', null=True)
    _dialplan_2_originaldigitmap = TextField(column_name='@dialplan.2.originaldigitmap', null=True)
    _dialplan_2_remove_end_of_dial = TextField(column_name='@dialplan.2.removeEndOfDial', null=True)
    _dialplan_2_routing_emergency_1_server_1 = TextField(column_name='@dialplan.2.routing.emergency.1.server.1', null=True)
    _dialplan_2_routing_emergency_1_server_2 = TextField(column_name='@dialplan.2.routing.emergency.1.server.2', null=True)
    _dialplan_2_routing_emergency_1_server_3 = TextField(column_name='@dialplan.2.routing.emergency.1.server.3', null=True)
    _dialplan_2_routing_emergency_1_value = TextField(column_name='@dialplan.2.routing.emergency.1.value', null=True)
    _dialplan_2_routing_emergency_2_server_1 = TextField(column_name='@dialplan.2.routing.emergency.2.server.1', null=True)
    _dialplan_2_routing_emergency_2_server_2 = TextField(column_name='@dialplan.2.routing.emergency.2.server.2', null=True)
    _dialplan_2_routing_emergency_2_server_3 = TextField(column_name='@dialplan.2.routing.emergency.2.server.3', null=True)
    _dialplan_2_routing_emergency_2_value = TextField(column_name='@dialplan.2.routing.emergency.2.value', null=True)
    _dialplan_2_routing_server_1_address = TextField(column_name='@dialplan.2.routing.server.1.address', null=True)
    _dialplan_2_routing_server_1_port = TextField(column_name='@dialplan.2.routing.server.1.port', null=True)
    _dialplan_2_routing_server_1_transport = TextField(column_name='@dialplan.2.routing.server.1.transport', null=True)
    _dialplan_2_routing_server_2_address = TextField(column_name='@dialplan.2.routing.server.2.address', null=True)
    _dialplan_2_routing_server_2_port = TextField(column_name='@dialplan.2.routing.server.2.port', null=True)
    _dialplan_2_routing_server_2_transport = TextField(column_name='@dialplan.2.routing.server.2.transport', null=True)
    _dialplan__translation_in_auto_comp = TextField(column_name='@dialplan.TranslationInAutoComp', null=True)
    _dialplan_apply_to_call_list_dial = TextField(column_name='@dialplan.applyToCallListDial', null=True)
    _dialplan_apply_to_directory_dial = TextField(column_name='@dialplan.applyToDirectoryDial', null=True)
    _dialplan_apply_to_forward = TextField(column_name='@dialplan.applyToForward', null=True)
    _dialplan_apply_to_pstn_dialing = TextField(column_name='@dialplan.applyToPstnDialing', null=True)
    _dialplan_apply_to_remote_dialing = TextField(column_name='@dialplan.applyToRemoteDialing', null=True)
    _dialplan_apply_to_tel_uri_dial = TextField(column_name='@dialplan.applyToTelUriDial', null=True)
    _dialplan_apply_to_user_dial = TextField(column_name='@dialplan.applyToUserDial', null=True)
    _dialplan_apply_to_user_send = TextField(column_name='@dialplan.applyToUserSend', null=True)
    _dialplan_conflict_match_handling = TextField(column_name='@dialplan.conflictMatchHandling', null=True)
    _dialplan_digitmap = TextField(column_name='@dialplan.digitmap', null=True)
    _dialplan_impossible_match_handling = TextField(column_name='@dialplan.impossibleMatchHandling', null=True)
    _dialplan_remove_end_of_dial = TextField(column_name='@dialplan.removeEndOfDial', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan'

class Dialplandigitmap(BaseModel):
    _dialplan_digitmap_count = TextField(column_name='@dialplan.digitmap.count', null=True)
    _dialplan_digitmap_time_out = TextField(column_name='@dialplan.digitmap.timeOut', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.digitmap'

class DialplandigitmaplineSwitching(BaseModel):
    _dialplan_digitmap_line_switching_enable = TextField(column_name='@dialplan.digitmap.lineSwitching.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.digitmap.lineSwitching'

class DialplanimpossibleMatchHandling(BaseModel):
    _dialplan_impossible_match_handling_time_out = TextField(column_name='@dialplan.impossibleMatchHandling.timeOut', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.impossibleMatchHandling'

class Dialplanroutingemergency(BaseModel):
    _dialplan_routing_emergency_1_description = TextField(column_name='@dialplan.routing.emergency.1.description', null=True)
    _dialplan_routing_emergency_1_server_1 = TextField(column_name='@dialplan.routing.emergency.1.server.1', null=True)
    _dialplan_routing_emergency_1_server_2 = TextField(column_name='@dialplan.routing.emergency.1.server.2', null=True)
    _dialplan_routing_emergency_1_value = TextField(column_name='@dialplan.routing.emergency.1.value', null=True)
    _dialplan_routing_emergency_2_description = TextField(column_name='@dialplan.routing.emergency.2.description', null=True)
    _dialplan_routing_emergency_2_server_1 = TextField(column_name='@dialplan.routing.emergency.2.server.1', null=True)
    _dialplan_routing_emergency_2_server_2 = TextField(column_name='@dialplan.routing.emergency.2.server.2', null=True)
    _dialplan_routing_emergency_2_value = TextField(column_name='@dialplan.routing.emergency.2.value', null=True)
    _dialplan_routing_emergency_outbound_identity = TextField(column_name='@dialplan.routing.emergency.outboundIdentity', null=True)
    _dialplan_routing_emergency_preferred_source = TextField(column_name='@dialplan.routing.emergency.preferredSource', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.routing.emergency'

class Dialplanroutingserver(BaseModel):
    _dialplan_routing_server_1_address = TextField(column_name='@dialplan.routing.server.1.address', null=True)
    _dialplan_routing_server_1_port = TextField(column_name='@dialplan.routing.server.1.port', null=True)
    _dialplan_routing_server_1_transport = TextField(column_name='@dialplan.routing.server.1.transport', null=True)
    _dialplan_routing_server_2_address = TextField(column_name='@dialplan.routing.server.2.address', null=True)
    _dialplan_routing_server_2_port = TextField(column_name='@dialplan.routing.server.2.port', null=True)
    _dialplan_routing_server_2_transport = TextField(column_name='@dialplan.routing.server.2.transport', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.routing.server'

class DialplanuserDial(BaseModel):
    _dialplan_user_dial_time_out = TextField(column_name='@dialplan.userDial.timeOut', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dialplan.userDial'

class DirlocalserverFeatureControl(BaseModel):
    _dir_local_server_feature_control_address = TextField(column_name='@dir.local.serverFeatureControl.address', null=True)
    _dir_local_server_feature_control_method = TextField(column_name='@dir.local.serverFeatureControl.method', null=True)
    _dir_local_server_feature_control_reg = TextField(column_name='@dir.local.serverFeatureControl.reg', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dir.local.serverFeatureControl'

class Divert(BaseModel):
    _divert_1_auto_on_specific_caller = TextField(column_name='@divert.1.autoOnSpecificCaller', null=True)
    _divert_1_contact = TextField(column_name='@divert.1.contact', null=True)
    _divert_1_shared_disabled = TextField(column_name='@divert.1.sharedDisabled', null=True)
    _divert_2_auto_on_specific_caller = TextField(column_name='@divert.2.autoOnSpecificCaller', null=True)
    _divert_2_contact = TextField(column_name='@divert.2.contact', null=True)
    _divert_2_shared_disabled = TextField(column_name='@divert.2.sharedDisabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'divert'

class Divertbusy(BaseModel):
    _divert_busy_1_contact = TextField(column_name='@divert.busy.1.contact', null=True)
    _divert_busy_1_enabled = TextField(column_name='@divert.busy.1.enabled', null=True)
    _divert_busy_2_contact = TextField(column_name='@divert.busy.2.contact', null=True)
    _divert_busy_2_enabled = TextField(column_name='@divert.busy.2.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'divert.busy'

class Divertdnd(BaseModel):
    _divert_dnd_1_contact = TextField(column_name='@divert.dnd.1.contact', null=True)
    _divert_dnd_1_enabled = TextField(column_name='@divert.dnd.1.enabled', null=True)
    _divert_dnd_2_contact = TextField(column_name='@divert.dnd.2.contact', null=True)
    _divert_dnd_2_enabled = TextField(column_name='@divert.dnd.2.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'divert.dnd'

class Divertfwd(BaseModel):
    _divert_fwd_1_enabled = TextField(column_name='@divert.fwd.1.enabled', null=True)
    _divert_fwd_2_enabled = TextField(column_name='@divert.fwd.2.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'divert.fwd'

class Divertnoanswer(BaseModel):
    _divert_noanswer_1_contact = TextField(column_name='@divert.noanswer.1.contact', null=True)
    _divert_noanswer_1_enabled = TextField(column_name='@divert.noanswer.1.enabled', null=True)
    _divert_noanswer_1_timeout = TextField(column_name='@divert.noanswer.1.timeout', null=True)
    _divert_noanswer_2_contact = TextField(column_name='@divert.noanswer.2.contact', null=True)
    _divert_noanswer_2_enabled = TextField(column_name='@divert.noanswer.2.enabled', null=True)
    _divert_noanswer_2_timeout = TextField(column_name='@divert.noanswer.2.timeout', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'divert.noanswer'

class Dnscachea(BaseModel):
    _dns_cache_a_1_address = TextField(column_name='@dns.cache.A.1.address', null=True)
    _dns_cache_a_1_name = TextField(column_name='@dns.cache.A.1.name', null=True)
    _dns_cache_a_1_ttl = TextField(column_name='@dns.cache.A.1.ttl', null=True)
    _dns_cache_a_2_address = TextField(column_name='@dns.cache.A.2.address', null=True)
    _dns_cache_a_2_name = TextField(column_name='@dns.cache.A.2.name', null=True)
    _dns_cache_a_2_ttl = TextField(column_name='@dns.cache.A.2.ttl', null=True)
    _dns_cache_a_network_override = TextField(column_name='@dns.cache.A.networkOverride', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dns.cache.A'

class Dnscacheaaaa(BaseModel):
    _dns_cache_aaaa_1_address = TextField(column_name='@dns.cache.AAAA.1.address', null=True)
    _dns_cache_aaaa_1_name = TextField(column_name='@dns.cache.AAAA.1.name', null=True)
    _dns_cache_aaaa_1_ttl = TextField(column_name='@dns.cache.AAAA.1.ttl', null=True)
    _dns_cache_aaaa_2_address = TextField(column_name='@dns.cache.AAAA.2.address', null=True)
    _dns_cache_aaaa_2_name = TextField(column_name='@dns.cache.AAAA.2.name', null=True)
    _dns_cache_aaaa_2_ttl = TextField(column_name='@dns.cache.AAAA.2.ttl', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dns.cache.AAAA'

class Dnscachenaptr(BaseModel):
    _dns_cache_naptr_1_flags = TextField(column_name='@dns.cache.NAPTR.1.flags', null=True)
    _dns_cache_naptr_1_name = TextField(column_name='@dns.cache.NAPTR.1.name', null=True)
    _dns_cache_naptr_1_order = TextField(column_name='@dns.cache.NAPTR.1.order', null=True)
    _dns_cache_naptr_1_preference = TextField(column_name='@dns.cache.NAPTR.1.preference', null=True)
    _dns_cache_naptr_1_regexp = TextField(column_name='@dns.cache.NAPTR.1.regexp', null=True)
    _dns_cache_naptr_1_replacement = TextField(column_name='@dns.cache.NAPTR.1.replacement', null=True)
    _dns_cache_naptr_1_service = TextField(column_name='@dns.cache.NAPTR.1.service', null=True)
    _dns_cache_naptr_1_ttl = TextField(column_name='@dns.cache.NAPTR.1.ttl', null=True)
    _dns_cache_naptr_2_flags = TextField(column_name='@dns.cache.NAPTR.2.flags', null=True)
    _dns_cache_naptr_2_name = TextField(column_name='@dns.cache.NAPTR.2.name', null=True)
    _dns_cache_naptr_2_order = TextField(column_name='@dns.cache.NAPTR.2.order', null=True)
    _dns_cache_naptr_2_preference = TextField(column_name='@dns.cache.NAPTR.2.preference', null=True)
    _dns_cache_naptr_2_regexp = TextField(column_name='@dns.cache.NAPTR.2.regexp', null=True)
    _dns_cache_naptr_2_replacement = TextField(column_name='@dns.cache.NAPTR.2.replacement', null=True)
    _dns_cache_naptr_2_service = TextField(column_name='@dns.cache.NAPTR.2.service', null=True)
    _dns_cache_naptr_2_ttl = TextField(column_name='@dns.cache.NAPTR.2.ttl', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dns.cache.NAPTR'

class Dnscachesrv(BaseModel):
    _dns_cache_srv_1_name = TextField(column_name='@dns.cache.SRV.1.name', null=True)
    _dns_cache_srv_1_port = TextField(column_name='@dns.cache.SRV.1.port', null=True)
    _dns_cache_srv_1_priority = TextField(column_name='@dns.cache.SRV.1.priority', null=True)
    _dns_cache_srv_1_target = TextField(column_name='@dns.cache.SRV.1.target', null=True)
    _dns_cache_srv_1_ttl = TextField(column_name='@dns.cache.SRV.1.ttl', null=True)
    _dns_cache_srv_1_weight = TextField(column_name='@dns.cache.SRV.1.weight', null=True)
    _dns_cache_srv_2_name = TextField(column_name='@dns.cache.SRV.2.name', null=True)
    _dns_cache_srv_2_port = TextField(column_name='@dns.cache.SRV.2.port', null=True)
    _dns_cache_srv_2_priority = TextField(column_name='@dns.cache.SRV.2.priority', null=True)
    _dns_cache_srv_2_target = TextField(column_name='@dns.cache.SRV.2.target', null=True)
    _dns_cache_srv_2_ttl = TextField(column_name='@dns.cache.SRV.2.ttl', null=True)
    _dns_cache_srv_2_weight = TextField(column_name='@dns.cache.SRV.2.weight', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'dns.cache.SRV'

class Ethernetarpstormfilter(BaseModel):
    _ethernet_arp_stormfilter_level = TextField(column_name='@ethernet.arp.stormfilter.level', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ethernet.arp.stormfilter'

class Featuree911(BaseModel):
    _feature_e911_location_retry_timer = TextField(column_name='@feature.E911.locationRetryTimer', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.E911'

class Featuree911Held(BaseModel):
    _feature_e911_held_identity = TextField(column_name='@feature.E911.HELD.identity', null=True)
    _feature_e911_held_identity_value = TextField(column_name='@feature.E911.HELD.identityValue', null=True)
    _feature_e911_held_password = TextField(column_name='@feature.E911.HELD.password', null=True)
    _feature_e911_held_request_type = TextField(column_name='@feature.E911.HELD.requestType', null=True)
    _feature_e911_held_server = TextField(column_name='@feature.E911.HELD.server', null=True)
    _feature_e911_held_username = TextField(column_name='@feature.E911.HELD.username', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.E911.HELD'

class Featuree911Heldnai(BaseModel):
    _feature_e911_held_nai_enable = TextField(column_name='@feature.E911.HELD.nai.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.E911.HELD.nai'

class Featuree911Heldsecondary(BaseModel):
    _feature_e911_held_secondary_password = TextField(column_name='@feature.E911.HELD.secondary.password', null=True)
    _feature_e911_held_secondary_server = TextField(column_name='@feature.E911.HELD.secondary.server', null=True)
    _feature_e911_held_secondary_username = TextField(column_name='@feature.E911.HELD.secondary.username', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.E911.HELD.secondary'

class Featuree911Usagerule(BaseModel):
    _feature_e911_usagerule_retransmission = TextField(column_name='@feature.E911.usagerule.retransmission', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.E911.usagerule'

class FeaturenonVolatileRingerVolume(BaseModel):
    _feature_non_volatile_ringer_volume_enabled = TextField(column_name='@feature.nonVolatileRingerVolume.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.nonVolatileRingerVolume'

class Featuretwamp(BaseModel):
    _feature_twamp_enabled = TextField(column_name='@feature.twamp.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.twamp'

class FeaturewebSecurityBanner(BaseModel):
    _feature_web_security_banner_enabled = TextField(column_name='@feature.webSecurityBanner.enabled', null=True)
    _feature_web_security_banner_msg = TextField(column_name='@feature.webSecurityBanner.msg', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'feature.webSecurityBanner'

class Httpd(BaseModel):
    _httpd_enabled = TextField(column_name='@httpd.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'httpd'

class Httpdcfg(BaseModel):
    _httpd_cfg_enabled = TextField(column_name='@httpd.cfg.enabled', null=True)
    _httpd_cfg_port = TextField(column_name='@httpd.cfg.port', null=True)
    _httpd_cfg_secure_tunnel_enabled = TextField(column_name='@httpd.cfg.secureTunnelEnabled', null=True)
    _httpd_cfg_secure_tunnel_port = TextField(column_name='@httpd.cfg.secureTunnelPort', null=True)
    _httpd_cfg_secure_tunnel_required = TextField(column_name='@httpd.cfg.secureTunnelRequired', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'httpd.cfg'

class HttpdcfglockWebUi(BaseModel):
    _httpd_cfg_lock_web_ui_enable = TextField(column_name='@httpd.cfg.lockWebUI.enable', null=True)
    _httpd_cfg_lock_web_ui_lock_out_duration = TextField(column_name='@httpd.cfg.lockWebUI.lockOutDuration', null=True)
    _httpd_cfg_lock_web_ui_no_of_invalid_attempts = TextField(column_name='@httpd.cfg.lockWebUI.noOfInvalidAttempts', null=True)
    _httpd_cfg_lock_web_ui_no_of_invalid_attempts_duration = TextField(column_name='@httpd.cfg.lockWebUI.noOfInvalidAttemptsDuration', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'httpd.cfg.lockWebUI'

class Ipv6(BaseModel):
    _ipv6_mld_version = TextField(column_name='@ipv6.mldVersion', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ipv6'

class Lcldatetimedate(BaseModel):
    _lcl_datetime_date_date_top = TextField(column_name='@lcl.datetime.date.dateTop', null=True)
    _lcl_datetime_date_date_top_cx5500 = TextField(column_name='@lcl.datetime.date.dateTop.CX5500', null=True)
    _lcl_datetime_date_date_top_vvx101 = TextField(column_name='@lcl.datetime.date.dateTop.VVX101', null=True)
    _lcl_datetime_date_date_top_vvx150 = TextField(column_name='@lcl.datetime.date.dateTop.VVX150', null=True)
    _lcl_datetime_date_date_top_vvx201 = TextField(column_name='@lcl.datetime.date.dateTop.VVX201', null=True)
    _lcl_datetime_date_date_top_vvx250 = TextField(column_name='@lcl.datetime.date.dateTop.VVX250', null=True)
    _lcl_datetime_date_date_top_vvx300 = TextField(column_name='@lcl.datetime.date.dateTop.VVX300', null=True)
    _lcl_datetime_date_date_top_vvx301 = TextField(column_name='@lcl.datetime.date.dateTop.VVX301', null=True)
    _lcl_datetime_date_date_top_vvx310 = TextField(column_name='@lcl.datetime.date.dateTop.VVX310', null=True)
    _lcl_datetime_date_date_top_vvx311 = TextField(column_name='@lcl.datetime.date.dateTop.VVX311', null=True)
    _lcl_datetime_date_date_top_vvx350 = TextField(column_name='@lcl.datetime.date.dateTop.VVX350', null=True)
    _lcl_datetime_date_date_top_vvx400 = TextField(column_name='@lcl.datetime.date.dateTop.VVX400', null=True)
    _lcl_datetime_date_date_top_vvx401 = TextField(column_name='@lcl.datetime.date.dateTop.VVX401', null=True)
    _lcl_datetime_date_date_top_vvx410 = TextField(column_name='@lcl.datetime.date.dateTop.VVX410', null=True)
    _lcl_datetime_date_date_top_vvx411 = TextField(column_name='@lcl.datetime.date.dateTop.VVX411', null=True)
    _lcl_datetime_date_date_top_vvx450 = TextField(column_name='@lcl.datetime.date.dateTop.VVX450', null=True)
    _lcl_datetime_date_date_top_vvx500 = TextField(column_name='@lcl.datetime.date.dateTop.VVX500', null=True)
    _lcl_datetime_date_date_top_vvx501 = TextField(column_name='@lcl.datetime.date.dateTop.VVX501', null=True)
    _lcl_datetime_date_date_top_vvx600 = TextField(column_name='@lcl.datetime.date.dateTop.VVX600', null=True)
    _lcl_datetime_date_date_top_vvx601 = TextField(column_name='@lcl.datetime.date.dateTop.VVX601', null=True)
    _lcl_datetime_date_format = TextField(column_name='@lcl.datetime.date.format', null=True)
    _lcl_datetime_date_long_format = TextField(column_name='@lcl.datetime.date.longFormat', null=True)
    _lcl_datetime_date_long_format_vvx101 = TextField(column_name='@lcl.datetime.date.longFormat.VVX101', null=True)
    _lcl_datetime_date_long_format_vvx150 = TextField(column_name='@lcl.datetime.date.longFormat.VVX150', null=True)
    _lcl_datetime_date_long_format_vvx201 = TextField(column_name='@lcl.datetime.date.longFormat.VVX201', null=True)
    _lcl_datetime_date_long_format_vvx250 = TextField(column_name='@lcl.datetime.date.longFormat.VVX250', null=True)
    _lcl_datetime_date_long_format_vvx300 = TextField(column_name='@lcl.datetime.date.longFormat.VVX300', null=True)
    _lcl_datetime_date_long_format_vvx301 = TextField(column_name='@lcl.datetime.date.longFormat.VVX301', null=True)
    _lcl_datetime_date_long_format_vvx310 = TextField(column_name='@lcl.datetime.date.longFormat.VVX310', null=True)
    _lcl_datetime_date_long_format_vvx311 = TextField(column_name='@lcl.datetime.date.longFormat.VVX311', null=True)
    _lcl_datetime_date_long_format_vvx350 = TextField(column_name='@lcl.datetime.date.longFormat.VVX350', null=True)
    _lcl_datetime_date_long_format_vvx400 = TextField(column_name='@lcl.datetime.date.longFormat.VVX400', null=True)
    _lcl_datetime_date_long_format_vvx401 = TextField(column_name='@lcl.datetime.date.longFormat.VVX401', null=True)
    _lcl_datetime_date_long_format_vvx410 = TextField(column_name='@lcl.datetime.date.longFormat.VVX410', null=True)
    _lcl_datetime_date_long_format_vvx411 = TextField(column_name='@lcl.datetime.date.longFormat.VVX411', null=True)
    _lcl_datetime_date_long_format_vvx450 = TextField(column_name='@lcl.datetime.date.longFormat.VVX450', null=True)
    _lcl_datetime_date_long_format_vvx500 = TextField(column_name='@lcl.datetime.date.longFormat.VVX500', null=True)
    _lcl_datetime_date_long_format_vvx501 = TextField(column_name='@lcl.datetime.date.longFormat.VVX501', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.datetime.date'

class Lcldatetimetime(BaseModel):
    _lcl_datetime_time_24_hour_clock = TextField(column_name='@lcl.datetime.time.24HourClock', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.datetime.time'

class Lclml(BaseModel):
    _lcl_ml_lang = TextField(column_name='@lcl.ml.lang', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.ml'

class Lclmllang(BaseModel):
    _lcl_ml_lang_charset = TextField(column_name='@lcl.ml.lang.charset', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.ml.lang'

class Lclmllangclock(BaseModel):
    _lcl_ml_lang_clock_1_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.1.24HourClock', null=True)
    _lcl_ml_lang_clock_1_date_top = TextField(column_name='@lcl.ml.lang.clock.1.dateTop', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx300 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX300', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx301 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX301', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx310 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX310', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx311 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX311', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx500 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX500', null=True)
    _lcl_ml_lang_clock_1_date_top_vvx501 = TextField(column_name='@lcl.ml.lang.clock.1.dateTop.VVX501', null=True)
    _lcl_ml_lang_clock_1_format = TextField(column_name='@lcl.ml.lang.clock.1.format', null=True)
    _lcl_ml_lang_clock_1_long_format = TextField(column_name='@lcl.ml.lang.clock.1.longFormat', null=True)
    _lcl_ml_lang_clock_10_format = TextField(column_name='@lcl.ml.lang.clock.10.format', null=True)
    _lcl_ml_lang_clock_11_format = TextField(column_name='@lcl.ml.lang.clock.11.format', null=True)
    _lcl_ml_lang_clock_12_format = TextField(column_name='@lcl.ml.lang.clock.12.format', null=True)
    _lcl_ml_lang_clock_13_format = TextField(column_name='@lcl.ml.lang.clock.13.format', null=True)
    _lcl_ml_lang_clock_14_format = TextField(column_name='@lcl.ml.lang.clock.14.format', null=True)
    _lcl_ml_lang_clock_15_format = TextField(column_name='@lcl.ml.lang.clock.15.format', null=True)
    _lcl_ml_lang_clock_16_format = TextField(column_name='@lcl.ml.lang.clock.16.format', null=True)
    _lcl_ml_lang_clock_17_format = TextField(column_name='@lcl.ml.lang.clock.17.format', null=True)
    _lcl_ml_lang_clock_18_format = TextField(column_name='@lcl.ml.lang.clock.18.format', null=True)
    _lcl_ml_lang_clock_19_format = TextField(column_name='@lcl.ml.lang.clock.19.format', null=True)
    _lcl_ml_lang_clock_2_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.2.24HourClock', null=True)
    _lcl_ml_lang_clock_2_date_top = TextField(column_name='@lcl.ml.lang.clock.2.dateTop', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx300 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX300', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx301 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX301', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx310 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX310', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx311 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX311', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx500 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX500', null=True)
    _lcl_ml_lang_clock_2_date_top_vvx501 = TextField(column_name='@lcl.ml.lang.clock.2.dateTop.VVX501', null=True)
    _lcl_ml_lang_clock_2_format = TextField(column_name='@lcl.ml.lang.clock.2.format', null=True)
    _lcl_ml_lang_clock_2_long_format = TextField(column_name='@lcl.ml.lang.clock.2.longFormat', null=True)
    _lcl_ml_lang_clock_20_format = TextField(column_name='@lcl.ml.lang.clock.20.format', null=True)
    _lcl_ml_lang_clock_3_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.3.24HourClock', null=True)
    _lcl_ml_lang_clock_3_format = TextField(column_name='@lcl.ml.lang.clock.3.format', null=True)
    _lcl_ml_lang_clock_4_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.4.24HourClock', null=True)
    _lcl_ml_lang_clock_4_format = TextField(column_name='@lcl.ml.lang.clock.4.format', null=True)
    _lcl_ml_lang_clock_5_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.5.24HourClock', null=True)
    _lcl_ml_lang_clock_5_format = TextField(column_name='@lcl.ml.lang.clock.5.format', null=True)
    _lcl_ml_lang_clock_6_24_hour_clock = TextField(column_name='@lcl.ml.lang.clock.6.24HourClock', null=True)
    _lcl_ml_lang_clock_6_format = TextField(column_name='@lcl.ml.lang.clock.6.format', null=True)
    _lcl_ml_lang_clock_7_format = TextField(column_name='@lcl.ml.lang.clock.7.format', null=True)
    _lcl_ml_lang_clock_8_format = TextField(column_name='@lcl.ml.lang.clock.8.format', null=True)
    _lcl_ml_lang_clock_9_format = TextField(column_name='@lcl.ml.lang.clock.9.format', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.ml.lang.clock'

class Lclmllangjapanesefont(BaseModel):
    _lcl_ml_lang_japanese_font_enabled = TextField(column_name='@lcl.ml.lang.japanese.font.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.ml.lang.japanese.font'

class Lclmllangmenu(BaseModel):
    _lcl_ml_lang_menu_1 = TextField(column_name='@lcl.ml.lang.menu.1', null=True)
    _lcl_ml_lang_menu_1_label = TextField(column_name='@lcl.ml.lang.menu.1.label', null=True)
    _lcl_ml_lang_menu_10 = TextField(column_name='@lcl.ml.lang.menu.10', null=True)
    _lcl_ml_lang_menu_10_label = TextField(column_name='@lcl.ml.lang.menu.10.label', null=True)
    _lcl_ml_lang_menu_11 = TextField(column_name='@lcl.ml.lang.menu.11', null=True)
    _lcl_ml_lang_menu_11_label = TextField(column_name='@lcl.ml.lang.menu.11.label', null=True)
    _lcl_ml_lang_menu_12 = TextField(column_name='@lcl.ml.lang.menu.12', null=True)
    _lcl_ml_lang_menu_12_label = TextField(column_name='@lcl.ml.lang.menu.12.label', null=True)
    _lcl_ml_lang_menu_13 = TextField(column_name='@lcl.ml.lang.menu.13', null=True)
    _lcl_ml_lang_menu_13_label = TextField(column_name='@lcl.ml.lang.menu.13.label', null=True)
    _lcl_ml_lang_menu_14 = TextField(column_name='@lcl.ml.lang.menu.14', null=True)
    _lcl_ml_lang_menu_14_label = TextField(column_name='@lcl.ml.lang.menu.14.label', null=True)
    _lcl_ml_lang_menu_15 = TextField(column_name='@lcl.ml.lang.menu.15', null=True)
    _lcl_ml_lang_menu_15_label = TextField(column_name='@lcl.ml.lang.menu.15.label', null=True)
    _lcl_ml_lang_menu_16 = TextField(column_name='@lcl.ml.lang.menu.16', null=True)
    _lcl_ml_lang_menu_16_label = TextField(column_name='@lcl.ml.lang.menu.16.label', null=True)
    _lcl_ml_lang_menu_17 = TextField(column_name='@lcl.ml.lang.menu.17', null=True)
    _lcl_ml_lang_menu_17_label = TextField(column_name='@lcl.ml.lang.menu.17.label', null=True)
    _lcl_ml_lang_menu_18 = TextField(column_name='@lcl.ml.lang.menu.18', null=True)
    _lcl_ml_lang_menu_18_label = TextField(column_name='@lcl.ml.lang.menu.18.label', null=True)
    _lcl_ml_lang_menu_19 = TextField(column_name='@lcl.ml.lang.menu.19', null=True)
    _lcl_ml_lang_menu_19_label = TextField(column_name='@lcl.ml.lang.menu.19.label', null=True)
    _lcl_ml_lang_menu_2 = TextField(column_name='@lcl.ml.lang.menu.2', null=True)
    _lcl_ml_lang_menu_2_label = TextField(column_name='@lcl.ml.lang.menu.2.label', null=True)
    _lcl_ml_lang_menu_20 = TextField(column_name='@lcl.ml.lang.menu.20', null=True)
    _lcl_ml_lang_menu_20_label = TextField(column_name='@lcl.ml.lang.menu.20.label', null=True)
    _lcl_ml_lang_menu_21 = TextField(column_name='@lcl.ml.lang.menu.21', null=True)
    _lcl_ml_lang_menu_21_label = TextField(column_name='@lcl.ml.lang.menu.21.label', null=True)
    _lcl_ml_lang_menu_22 = TextField(column_name='@lcl.ml.lang.menu.22', null=True)
    _lcl_ml_lang_menu_22_label = TextField(column_name='@lcl.ml.lang.menu.22.label', null=True)
    _lcl_ml_lang_menu_3 = TextField(column_name='@lcl.ml.lang.menu.3', null=True)
    _lcl_ml_lang_menu_3_label = TextField(column_name='@lcl.ml.lang.menu.3.label', null=True)
    _lcl_ml_lang_menu_4 = TextField(column_name='@lcl.ml.lang.menu.4', null=True)
    _lcl_ml_lang_menu_4_label = TextField(column_name='@lcl.ml.lang.menu.4.label', null=True)
    _lcl_ml_lang_menu_5 = TextField(column_name='@lcl.ml.lang.menu.5', null=True)
    _lcl_ml_lang_menu_5_label = TextField(column_name='@lcl.ml.lang.menu.5.label', null=True)
    _lcl_ml_lang_menu_6 = TextField(column_name='@lcl.ml.lang.menu.6', null=True)
    _lcl_ml_lang_menu_6_label = TextField(column_name='@lcl.ml.lang.menu.6.label', null=True)
    _lcl_ml_lang_menu_7 = TextField(column_name='@lcl.ml.lang.menu.7', null=True)
    _lcl_ml_lang_menu_7_label = TextField(column_name='@lcl.ml.lang.menu.7.label', null=True)
    _lcl_ml_lang_menu_8 = TextField(column_name='@lcl.ml.lang.menu.8', null=True)
    _lcl_ml_lang_menu_8_label = TextField(column_name='@lcl.ml.lang.menu.8.label', null=True)
    _lcl_ml_lang_menu_9 = TextField(column_name='@lcl.ml.lang.menu.9', null=True)
    _lcl_ml_lang_menu_9_label = TextField(column_name='@lcl.ml.lang.menu.9.label', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.ml.lang.menu'

class Lclstatus(BaseModel):
    _lcl_status__line_info_at_top = TextField(column_name='@lcl.status.LineInfoAtTop', null=True)
    _lcl_status__line_info_at_top_text = TextField(column_name='@lcl.status.LineInfoAtTopText', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'lcl.status'

class Licensepolling(BaseModel):
    _license_polling_time = TextField(column_name='@license.polling.time', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'license.polling'

class LocInfo(BaseModel):
    _loc_info_source = TextField(column_name='@locInfo.source', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'locInfo'

class Mr(BaseModel):
    _mr_audio_stream_port_end = TextField(column_name='@mr.audioStreamPortEnd', null=True)
    _mr_audio_stream_port_start = TextField(column_name='@mr.audioStreamPortStart', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mr'

class Mrpairtls(BaseModel):
    _mr_pair_tls_enabled = TextField(column_name='@mr.pair.tls.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mr.pair.tls'

class Mrpairuid(BaseModel):
    _mr_pair_uid_1 = TextField(column_name='@mr.pair.uid.1', null=True)
    _mr_pair_uid_2 = TextField(column_name='@mr.pair.uid.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mr.pair.uid'

class MrpairButton(BaseModel):
    _mr_pair_button_notification = TextField(column_name='@mr.pairButton.notification', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mr.pairButton'

class Mrsrtpaudio(BaseModel):
    _mr_srtp_audio_require = TextField(column_name='@mr.srtp.audio.require', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mr.srtp.audio'

class MwibackLight(BaseModel):
    _mwi_back_light_disable = TextField(column_name='@mwi.backLight.disable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'mwi.backLight'

class Netinterface(BaseModel):
    _net_interface_mtu = TextField(column_name='@net.interface.mtu', null=True)
    _net_interface_mtu6 = TextField(column_name='@net.interface.mtu6', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'net.interface'

class PolycomConfig(BaseModel):
    _xmlns_xsi = TextField(column_name='@xmlns:xsi', null=True)
    _xsi_no_namespace_schema_location = TextField(column_name='@xsi:noNamespaceSchemaLocation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'polycomConfig'

class PowerSaving(BaseModel):
    _power_saving_enable = TextField(column_name='@powerSaving.enable', null=True)
    _power_saving_enable_cx5500 = TextField(column_name='@powerSaving.enable.CX5500', null=True)
    _power_saving_enable_vvx150 = TextField(column_name='@powerSaving.enable.VVX150', null=True)
    _power_saving_enable_vvx201 = TextField(column_name='@powerSaving.enable.VVX201', null=True)
    _power_saving_enable_vvx250 = TextField(column_name='@powerSaving.enable.VVX250', null=True)
    _power_saving_enable_vvx300 = TextField(column_name='@powerSaving.enable.VVX300', null=True)
    _power_saving_enable_vvx301 = TextField(column_name='@powerSaving.enable.VVX301', null=True)
    _power_saving_enable_vvx310 = TextField(column_name='@powerSaving.enable.VVX310', null=True)
    _power_saving_enable_vvx311 = TextField(column_name='@powerSaving.enable.VVX311', null=True)
    _power_saving_enable_vvx350 = TextField(column_name='@powerSaving.enable.VVX350', null=True)
    _power_saving_enable_vvx400 = TextField(column_name='@powerSaving.enable.VVX400', null=True)
    _power_saving_enable_vvx401 = TextField(column_name='@powerSaving.enable.VVX401', null=True)
    _power_saving_enable_vvx410 = TextField(column_name='@powerSaving.enable.VVX410', null=True)
    _power_saving_enable_vvx411 = TextField(column_name='@powerSaving.enable.VVX411', null=True)
    _power_saving_enable_vvx450 = TextField(column_name='@powerSaving.enable.VVX450', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving'

class PowerSavingidleTimeout(BaseModel):
    _power_saving_idle_timeout_off_hours = TextField(column_name='@powerSaving.idleTimeout.offHours', null=True)
    _power_saving_idle_timeout_office_hours = TextField(column_name='@powerSaving.idleTimeout.officeHours', null=True)
    _power_saving_idle_timeout_office_hours_vvx1500 = TextField(column_name='@powerSaving.idleTimeout.officeHours.VVX1500', null=True)
    _power_saving_idle_timeout_user_input_extension = TextField(column_name='@powerSaving.idleTimeout.userInputExtension', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving.idleTimeout'

class PowerSavingmotionDetection(BaseModel):
    _power_saving_motion_detection_frame_rate = TextField(column_name='@powerSaving.motionDetection.frameRate', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving.motionDetection'

class PowerSavingofficeHoursduration(BaseModel):
    _power_saving_office_hours_duration_friday = TextField(column_name='@powerSaving.officeHours.duration.friday', null=True)
    _power_saving_office_hours_duration_monday = TextField(column_name='@powerSaving.officeHours.duration.monday', null=True)
    _power_saving_office_hours_duration_saturday = TextField(column_name='@powerSaving.officeHours.duration.saturday', null=True)
    _power_saving_office_hours_duration_sunday = TextField(column_name='@powerSaving.officeHours.duration.sunday', null=True)
    _power_saving_office_hours_duration_thursday = TextField(column_name='@powerSaving.officeHours.duration.thursday', null=True)
    _power_saving_office_hours_duration_tuesday = TextField(column_name='@powerSaving.officeHours.duration.tuesday', null=True)
    _power_saving_office_hours_duration_wednesday = TextField(column_name='@powerSaving.officeHours.duration.wednesday', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving.officeHours.duration'

class PowerSavingofficeHoursstartHour(BaseModel):
    _power_saving_office_hours_start_hour_friday = TextField(column_name='@powerSaving.officeHours.startHour.friday', null=True)
    _power_saving_office_hours_start_hour_monday = TextField(column_name='@powerSaving.officeHours.startHour.monday', null=True)
    _power_saving_office_hours_start_hour_saturday = TextField(column_name='@powerSaving.officeHours.startHour.saturday', null=True)
    _power_saving_office_hours_start_hour_sunday = TextField(column_name='@powerSaving.officeHours.startHour.sunday', null=True)
    _power_saving_office_hours_start_hour_thursday = TextField(column_name='@powerSaving.officeHours.startHour.thursday', null=True)
    _power_saving_office_hours_start_hour_tuesday = TextField(column_name='@powerSaving.officeHours.startHour.tuesday', null=True)
    _power_saving_office_hours_start_hour_wednesday = TextField(column_name='@powerSaving.officeHours.startHour.wednesday', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving.officeHours.startHour'

class PowerSavinguserDetectionSensitivity(BaseModel):
    _power_saving_user_detection_sensitivity_off_hours = TextField(column_name='@powerSaving.userDetectionSensitivity.offHours', null=True)
    _power_saving_user_detection_sensitivity_office_hours = TextField(column_name='@powerSaving.userDetectionSensitivity.officeHours', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'powerSaving.userDetectionSensitivity'

class Prov(BaseModel):
    _prov_config_upload_path = TextField(column_name='@prov.configUploadPath', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov'

class ProvautoConfigUpload(BaseModel):
    _prov_auto_config_upload_enabled = TextField(column_name='@prov.autoConfigUpload.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.autoConfigUpload'

class ProvcoreUpload(BaseModel):
    _prov_core_upload_period = TextField(column_name='@prov.coreUpload.period', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.coreUpload'

class Provlogin(BaseModel):
    _prov_login_automatic_logout = TextField(column_name='@prov.login.automaticLogout', null=True)
    _prov_login_default_only = TextField(column_name='@prov.login.defaultOnly', null=True)
    _prov_login_default_password = TextField(column_name='@prov.login.defaultPassword', null=True)
    _prov_login_default_user = TextField(column_name='@prov.login.defaultUser', null=True)
    _prov_login_enabled = TextField(column_name='@prov.login.enabled', null=True)
    _prov_login_local_password = TextField(column_name='@prov.login.localPassword', null=True)
    _prov_login_persistent = TextField(column_name='@prov.login.persistent', null=True)
    _prov_login_required = TextField(column_name='@prov.login.required', null=True)
    _prov_login_use_prov_auth = TextField(column_name='@prov.login.useProvAuth', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.login'

class ProvloginlocalPassword(BaseModel):
    _prov_login_local_password_hashed = TextField(column_name='@prov.login.localPassword.hashed', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.login.localPassword'

class Provloginpassword(BaseModel):
    _prov_login_password_encoding_mode = TextField(column_name='@prov.login.password.encodingMode', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.login.password'

class ProvloginuserId(BaseModel):
    _prov_login_user_id_encoding_mode = TextField(column_name='@prov.login.userId.encodingMode', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.login.userId'

class ProvloginCredPwdFlushed(BaseModel):
    _prov_login_cred_pwd_flushed_enabled = TextField(column_name='@prov.loginCredPwdFlushed.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.loginCredPwdFlushed'

class Provpolling(BaseModel):
    _prov_polling_enabled = TextField(column_name='@prov.polling.enabled', null=True)
    _prov_polling_mode = TextField(column_name='@prov.polling.mode', null=True)
    _prov_polling_period = TextField(column_name='@prov.polling.period', null=True)
    _prov_polling_time = TextField(column_name='@prov.polling.time', null=True)
    _prov_polling_time_random_end = TextField(column_name='@prov.polling.timeRandomEnd', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.polling'

class ProvquickSetup(BaseModel):
    _prov_quick_setup_enabled = TextField(column_name='@prov.quickSetup.enabled', null=True)
    _prov_quick_setup_limit_server_details = TextField(column_name='@prov.quickSetup.limitServerDetails', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.quickSetup'

class ProvstartupCheck(BaseModel):
    _prov_startup_check_enabled = TextField(column_name='@prov.startupCheck.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.startupCheck'

class ProvuserControl(BaseModel):
    _prov_user_control_enabled = TextField(column_name='@prov.userControl.enabled', null=True)
    _prov_user_control_postpone_time = TextField(column_name='@prov.userControl.postponeTime', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'prov.userControl'

class Ptt(BaseModel):
    _ptt_address = TextField(column_name='@ptt.address', null=True)
    _ptt_allow_off_hook_pages = TextField(column_name='@ptt.allowOffHookPages', null=True)
    _ptt_codec = TextField(column_name='@ptt.codec', null=True)
    _ptt_compatibility_mode = TextField(column_name='@ptt.compatibilityMode', null=True)
    _ptt_default_channel = TextField(column_name='@ptt.defaultChannel', null=True)
    _ptt_display_name = TextField(column_name='@ptt.displayName', null=True)
    _ptt_emergency_channel = TextField(column_name='@ptt.emergencyChannel', null=True)
    _ptt_payload_size = TextField(column_name='@ptt.payloadSize', null=True)
    _ptt_port = TextField(column_name='@ptt.port', null=True)
    _ptt_priority_channel = TextField(column_name='@ptt.priorityChannel', null=True)
    _ptt_volume = TextField(column_name='@ptt.volume', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt'

class PttcallWaiting(BaseModel):
    _ptt_call_waiting_enable = TextField(column_name='@ptt.callWaiting.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt.callWaiting'

class PttemergencyChannel(BaseModel):
    _ptt_emergency_channel_volume = TextField(column_name='@ptt.emergencyChannel.volume', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt.emergencyChannel'

class PttpageMode(BaseModel):
    _ptt_page_mode_allow_off_hook_pages = TextField(column_name='@ptt.pageMode.allowOffHookPages', null=True)
    _ptt_page_mode_codec = TextField(column_name='@ptt.pageMode.codec', null=True)
    _ptt_page_mode_default_group = TextField(column_name='@ptt.pageMode.defaultGroup', null=True)
    _ptt_page_mode_display_name = TextField(column_name='@ptt.pageMode.displayName', null=True)
    _ptt_page_mode_emergency_group = TextField(column_name='@ptt.pageMode.emergencyGroup', null=True)
    _ptt_page_mode_enable = TextField(column_name='@ptt.pageMode.enable', null=True)
    _ptt_page_mode_payload_size = TextField(column_name='@ptt.pageMode.payloadSize', null=True)
    _ptt_page_mode_priority_group = TextField(column_name='@ptt.pageMode.priorityGroup', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt.pageMode'

class PttpageModetransmittimeout(BaseModel):
    _ptt_page_mode_transmit_timeout_continuation = TextField(column_name='@ptt.pageMode.transmit.timeout.continuation', null=True)
    _ptt_page_mode_transmit_timeout_initial = TextField(column_name='@ptt.pageMode.transmit.timeout.initial', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt.pageMode.transmit.timeout'

class PttpttMode(BaseModel):
    _ptt_ptt_mode_enable = TextField(column_name='@ptt.pttMode.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'ptt.pttMode'

class Qosethernet(BaseModel):
    _qos_ethernet_tcp_qos_enabled = TextField(column_name='@qos.ethernet.tcpQosEnabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ethernet'

class QosethernetcallControl(BaseModel):
    _qos_ethernet_call_control_user_priority = TextField(column_name='@qos.ethernet.callControl.user_priority', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ethernet.callControl'

class Qosethernetother(BaseModel):
    _qos_ethernet_other_user_priority = TextField(column_name='@qos.ethernet.other.user_priority', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ethernet.other'

class Qosethernetrtp(BaseModel):
    _qos_ethernet_rtp_user_priority = TextField(column_name='@qos.ethernet.rtp.user_priority', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ethernet.rtp'

class Qosethernetrtpvideo(BaseModel):
    _qos_ethernet_rtp_video_user_priority = TextField(column_name='@qos.ethernet.rtp.video.user_priority', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ethernet.rtp.video'

class QosipcallControl(BaseModel):
    _qos_ip_call_control_dscp = TextField(column_name='@qos.ip.callControl.dscp', null=True)
    _qos_ip_call_control_max_reliability = TextField(column_name='@qos.ip.callControl.max_reliability', null=True)
    _qos_ip_call_control_max_throughput = TextField(column_name='@qos.ip.callControl.max_throughput', null=True)
    _qos_ip_call_control_min_cost = TextField(column_name='@qos.ip.callControl.min_cost', null=True)
    _qos_ip_call_control_min_delay = TextField(column_name='@qos.ip.callControl.min_delay', null=True)
    _qos_ip_call_control_precedence = TextField(column_name='@qos.ip.callControl.precedence', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.callControl'

class QosipcallControldscpassuredService(BaseModel):
    _qos_ip_call_control_dscp_assured_service_1 = TextField(column_name='@qos.ip.callControl.dscp.assuredService.1', null=True)
    _qos_ip_call_control_dscp_assured_service_2 = TextField(column_name='@qos.ip.callControl.dscp.assuredService.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.callControl.dscp.assuredService'

class Qosiprtp(BaseModel):
    _qos_ip_rtp_dscp = TextField(column_name='@qos.ip.rtp.dscp', null=True)
    _qos_ip_rtp_max_reliability = TextField(column_name='@qos.ip.rtp.max_reliability', null=True)
    _qos_ip_rtp_max_throughput = TextField(column_name='@qos.ip.rtp.max_throughput', null=True)
    _qos_ip_rtp_min_cost = TextField(column_name='@qos.ip.rtp.min_cost', null=True)
    _qos_ip_rtp_min_delay = TextField(column_name='@qos.ip.rtp.min_delay', null=True)
    _qos_ip_rtp_precedence = TextField(column_name='@qos.ip.rtp.precedence', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.rtp'

class QosiprtpdscpassuredService(BaseModel):
    _qos_ip_rtp_dscp_assured_service_1 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.1', null=True)
    _qos_ip_rtp_dscp_assured_service_2 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.2', null=True)
    _qos_ip_rtp_dscp_assured_service_3 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.3', null=True)
    _qos_ip_rtp_dscp_assured_service_4 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.4', null=True)
    _qos_ip_rtp_dscp_assured_service_5 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.5', null=True)
    _qos_ip_rtp_dscp_assured_service_6 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.6', null=True)
    _qos_ip_rtp_dscp_assured_service_7 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.7', null=True)
    _qos_ip_rtp_dscp_assured_service_8 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.8', null=True)
    _qos_ip_rtp_dscp_assured_service_9 = TextField(column_name='@qos.ip.rtp.dscp.assuredService.9', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.rtp.dscp.assuredService'

class Qosiprtpvideo(BaseModel):
    _qos_ip_rtp_video_dscp = TextField(column_name='@qos.ip.rtp.video.dscp', null=True)
    _qos_ip_rtp_video_max_reliability = TextField(column_name='@qos.ip.rtp.video.max_reliability', null=True)
    _qos_ip_rtp_video_max_throughput = TextField(column_name='@qos.ip.rtp.video.max_throughput', null=True)
    _qos_ip_rtp_video_min_cost = TextField(column_name='@qos.ip.rtp.video.min_cost', null=True)
    _qos_ip_rtp_video_min_delay = TextField(column_name='@qos.ip.rtp.video.min_delay', null=True)
    _qos_ip_rtp_video_precedence = TextField(column_name='@qos.ip.rtp.video.precedence', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.rtp.video'

class QosiprtpvideodscpassuredService(BaseModel):
    _qos_ip_rtp_video_dscp_assured_service_1 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.1', null=True)
    _qos_ip_rtp_video_dscp_assured_service_2 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.2', null=True)
    _qos_ip_rtp_video_dscp_assured_service_3 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.3', null=True)
    _qos_ip_rtp_video_dscp_assured_service_4 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.4', null=True)
    _qos_ip_rtp_video_dscp_assured_service_5 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.5', null=True)
    _qos_ip_rtp_video_dscp_assured_service_6 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.6', null=True)
    _qos_ip_rtp_video_dscp_assured_service_7 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.7', null=True)
    _qos_ip_rtp_video_dscp_assured_service_8 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.8', null=True)
    _qos_ip_rtp_video_dscp_assured_service_9 = TextField(column_name='@qos.ip.rtp.video.dscp.assuredService.9', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'qos.ip.rtp.video.dscp.assuredService'

class Reg(BaseModel):
    _reg_1_line_1_label = TextField(column_name='@reg.1.line.1.label', null=True)
    _reg_1_line_2_label = TextField(column_name='@reg.1.line.2.label', null=True)
    _reg_1_server_1_address = TextField(column_name='@reg.1.server.1.address', null=True)
    _reg_1_server_1_fail_over_fail_back_mode = TextField(column_name='@reg.1.server.1.failOver.failBack.mode', null=True)
    _reg_1_server_1_fail_over_fail_back_timeout = TextField(column_name='@reg.1.server.1.failOver.failBack.timeout', null=True)
    _reg_1_server_1_fail_over_fail_registration_on = TextField(column_name='@reg.1.server.1.failOver.failRegistrationOn', null=True)
    _reg_1_server_1_fail_over_only_signal_with_registered = TextField(column_name='@reg.1.server.1.failOver.onlySignalWithRegistered', null=True)
    _reg_1_server_1_fail_over_re_register_on = TextField(column_name='@reg.1.server.1.failOver.reRegisterOn', null=True)
    _reg_1_server_1_port = TextField(column_name='@reg.1.server.1.port', null=True)
    _reg_1_server_1_register = TextField(column_name='@reg.1.server.1.register', null=True)
    _reg_1_server_1_transport = TextField(column_name='@reg.1.server.1.transport', null=True)
    _reg_1_server_1_use_outbound_proxy = TextField(column_name='@reg.1.server.1.useOutboundProxy', null=True)
    _reg_1_server_2_address = TextField(column_name='@reg.1.server.2.address', null=True)
    _reg_1_server_2_fail_over_fail_back_mode = TextField(column_name='@reg.1.server.2.failOver.failBack.mode', null=True)
    _reg_1_server_2_fail_over_fail_back_timeout = TextField(column_name='@reg.1.server.2.failOver.failBack.timeout', null=True)
    _reg_1_server_2_fail_over_fail_registration_on = TextField(column_name='@reg.1.server.2.failOver.failRegistrationOn', null=True)
    _reg_1_server_2_fail_over_only_signal_with_registered = TextField(column_name='@reg.1.server.2.failOver.onlySignalWithRegistered', null=True)
    _reg_1_server_2_fail_over_re_register_on = TextField(column_name='@reg.1.server.2.failOver.reRegisterOn', null=True)
    _reg_1_server_2_port = TextField(column_name='@reg.1.server.2.port', null=True)
    _reg_1_server_2_register = TextField(column_name='@reg.1.server.2.register', null=True)
    _reg_1_server_2_transport = TextField(column_name='@reg.1.server.2.transport', null=True)
    _reg_1_server_2_use_outbound_proxy = TextField(column_name='@reg.1.server.2.useOutboundProxy', null=True)
    _reg_1_server_h323_1_address = TextField(column_name='@reg.1.server.H323.1.address', null=True)
    _reg_1_server_h323_1_expires = TextField(column_name='@reg.1.server.H323.1.expires', null=True)
    _reg_1_server_h323_1_port = TextField(column_name='@reg.1.server.H323.1.port', null=True)
    _reg_1_server_h323_2_address = TextField(column_name='@reg.1.server.H323.2.address', null=True)
    _reg_1_server_h323_2_expires = TextField(column_name='@reg.1.server.H323.2.expires', null=True)
    _reg_1_server_h323_2_port = TextField(column_name='@reg.1.server.H323.2.port', null=True)
    _reg_2_line_1_label = TextField(column_name='@reg.2.line.1.label', null=True)
    _reg_2_line_2_label = TextField(column_name='@reg.2.line.2.label', null=True)
    _reg_2_server_1_address = TextField(column_name='@reg.2.server.1.address', null=True)
    _reg_2_server_1_fail_over_fail_back_mode = TextField(column_name='@reg.2.server.1.failOver.failBack.mode', null=True)
    _reg_2_server_1_fail_over_fail_back_timeout = TextField(column_name='@reg.2.server.1.failOver.failBack.timeout', null=True)
    _reg_2_server_1_fail_over_fail_registration_on = TextField(column_name='@reg.2.server.1.failOver.failRegistrationOn', null=True)
    _reg_2_server_1_fail_over_only_signal_with_registered = TextField(column_name='@reg.2.server.1.failOver.onlySignalWithRegistered', null=True)
    _reg_2_server_1_fail_over_re_register_on = TextField(column_name='@reg.2.server.1.failOver.reRegisterOn', null=True)
    _reg_2_server_1_port = TextField(column_name='@reg.2.server.1.port', null=True)
    _reg_2_server_1_register = TextField(column_name='@reg.2.server.1.register', null=True)
    _reg_2_server_1_transport = TextField(column_name='@reg.2.server.1.transport', null=True)
    _reg_2_server_1_use_outbound_proxy = TextField(column_name='@reg.2.server.1.useOutboundProxy', null=True)
    _reg_2_server_2_address = TextField(column_name='@reg.2.server.2.address', null=True)
    _reg_2_server_2_fail_over_fail_back_mode = TextField(column_name='@reg.2.server.2.failOver.failBack.mode', null=True)
    _reg_2_server_2_fail_over_fail_back_timeout = TextField(column_name='@reg.2.server.2.failOver.failBack.timeout', null=True)
    _reg_2_server_2_fail_over_fail_registration_on = TextField(column_name='@reg.2.server.2.failOver.failRegistrationOn', null=True)
    _reg_2_server_2_fail_over_only_signal_with_registered = TextField(column_name='@reg.2.server.2.failOver.onlySignalWithRegistered', null=True)
    _reg_2_server_2_fail_over_re_register_on = TextField(column_name='@reg.2.server.2.failOver.reRegisterOn', null=True)
    _reg_2_server_2_port = TextField(column_name='@reg.2.server.2.port', null=True)
    _reg_2_server_2_register = TextField(column_name='@reg.2.server.2.register', null=True)
    _reg_2_server_2_transport = TextField(column_name='@reg.2.server.2.transport', null=True)
    _reg_2_server_2_use_outbound_proxy = TextField(column_name='@reg.2.server.2.useOutboundProxy', null=True)
    _reg_2_server_h323_1_address = TextField(column_name='@reg.2.server.H323.1.address', null=True)
    _reg_2_server_h323_1_expires = TextField(column_name='@reg.2.server.H323.1.expires', null=True)
    _reg_2_server_h323_1_port = TextField(column_name='@reg.2.server.H323.1.port', null=True)
    _reg_2_server_h323_2_address = TextField(column_name='@reg.2.server.H323.2.address', null=True)
    _reg_2_server_h323_2_expires = TextField(column_name='@reg.2.server.H323.2.expires', null=True)
    _reg_2_server_h323_2_port = TextField(column_name='@reg.2.server.H323.2.port', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'reg'

class Saf(BaseModel):
    _saf_1 = TextField(column_name='@saf.1', null=True)
    _saf_2 = TextField(column_name='@saf.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'saf'

class Se(BaseModel):
    _se_stutter_on_voice_mail = TextField(column_name='@se.stutterOnVoiceMail', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se'

class Sepatringerringer1(BaseModel):
    _se_pat_ringer_ringer1_name = TextField(column_name='@se.pat.ringer.ringer1.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer1'

class Sepatringerringer1Inst(BaseModel):
    _se_pat_ringer_ringer1_inst_1_type = TextField(column_name='@se.pat.ringer.ringer1.inst.1.type', null=True)
    _se_pat_ringer_ringer1_inst_1_value = TextField(column_name='@se.pat.ringer.ringer1.inst.1.value', null=True)
    _se_pat_ringer_ringer1_inst_2_type = TextField(column_name='@se.pat.ringer.ringer1.inst.2.type', null=True)
    _se_pat_ringer_ringer1_inst_2_value = TextField(column_name='@se.pat.ringer.ringer1.inst.2.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer1.inst'

class Sepatringerringer10(BaseModel):
    _se_pat_ringer_ringer10_name = TextField(column_name='@se.pat.ringer.ringer10.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer10'

class Sepatringerringer10Inst(BaseModel):
    _se_pat_ringer_ringer10_inst_1_type = TextField(column_name='@se.pat.ringer.ringer10.inst.1.type', null=True)
    _se_pat_ringer_ringer10_inst_1_value = TextField(column_name='@se.pat.ringer.ringer10.inst.1.value', null=True)
    _se_pat_ringer_ringer10_inst_10_type = TextField(column_name='@se.pat.ringer.ringer10.inst.10.type', null=True)
    _se_pat_ringer_ringer10_inst_10_value = TextField(column_name='@se.pat.ringer.ringer10.inst.10.value', null=True)
    _se_pat_ringer_ringer10_inst_11_type = TextField(column_name='@se.pat.ringer.ringer10.inst.11.type', null=True)
    _se_pat_ringer_ringer10_inst_11_value = TextField(column_name='@se.pat.ringer.ringer10.inst.11.value', null=True)
    _se_pat_ringer_ringer10_inst_2_type = TextField(column_name='@se.pat.ringer.ringer10.inst.2.type', null=True)
    _se_pat_ringer_ringer10_inst_2_value = TextField(column_name='@se.pat.ringer.ringer10.inst.2.value', null=True)
    _se_pat_ringer_ringer10_inst_3_type = TextField(column_name='@se.pat.ringer.ringer10.inst.3.type', null=True)
    _se_pat_ringer_ringer10_inst_3_value = TextField(column_name='@se.pat.ringer.ringer10.inst.3.value', null=True)
    _se_pat_ringer_ringer10_inst_4_type = TextField(column_name='@se.pat.ringer.ringer10.inst.4.type', null=True)
    _se_pat_ringer_ringer10_inst_4_value = TextField(column_name='@se.pat.ringer.ringer10.inst.4.value', null=True)
    _se_pat_ringer_ringer10_inst_5_type = TextField(column_name='@se.pat.ringer.ringer10.inst.5.type', null=True)
    _se_pat_ringer_ringer10_inst_5_value = TextField(column_name='@se.pat.ringer.ringer10.inst.5.value', null=True)
    _se_pat_ringer_ringer10_inst_6_type = TextField(column_name='@se.pat.ringer.ringer10.inst.6.type', null=True)
    _se_pat_ringer_ringer10_inst_6_value = TextField(column_name='@se.pat.ringer.ringer10.inst.6.value', null=True)
    _se_pat_ringer_ringer10_inst_7_type = TextField(column_name='@se.pat.ringer.ringer10.inst.7.type', null=True)
    _se_pat_ringer_ringer10_inst_7_value = TextField(column_name='@se.pat.ringer.ringer10.inst.7.value', null=True)
    _se_pat_ringer_ringer10_inst_8_type = TextField(column_name='@se.pat.ringer.ringer10.inst.8.type', null=True)
    _se_pat_ringer_ringer10_inst_8_value = TextField(column_name='@se.pat.ringer.ringer10.inst.8.value', null=True)
    _se_pat_ringer_ringer10_inst_9_type = TextField(column_name='@se.pat.ringer.ringer10.inst.9.type', null=True)
    _se_pat_ringer_ringer10_inst_9_value = TextField(column_name='@se.pat.ringer.ringer10.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer10.inst'

class Sepatringerringer11(BaseModel):
    _se_pat_ringer_ringer11_name = TextField(column_name='@se.pat.ringer.ringer11.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer11'

class Sepatringerringer11Inst(BaseModel):
    _se_pat_ringer_ringer11_inst_1_type = TextField(column_name='@se.pat.ringer.ringer11.inst.1.type', null=True)
    _se_pat_ringer_ringer11_inst_1_value = TextField(column_name='@se.pat.ringer.ringer11.inst.1.value', null=True)
    _se_pat_ringer_ringer11_inst_10_type = TextField(column_name='@se.pat.ringer.ringer11.inst.10.type', null=True)
    _se_pat_ringer_ringer11_inst_10_value = TextField(column_name='@se.pat.ringer.ringer11.inst.10.value', null=True)
    _se_pat_ringer_ringer11_inst_11_type = TextField(column_name='@se.pat.ringer.ringer11.inst.11.type', null=True)
    _se_pat_ringer_ringer11_inst_11_value = TextField(column_name='@se.pat.ringer.ringer11.inst.11.value', null=True)
    _se_pat_ringer_ringer11_inst_12_type = TextField(column_name='@se.pat.ringer.ringer11.inst.12.type', null=True)
    _se_pat_ringer_ringer11_inst_12_value = TextField(column_name='@se.pat.ringer.ringer11.inst.12.value', null=True)
    _se_pat_ringer_ringer11_inst_13_type = TextField(column_name='@se.pat.ringer.ringer11.inst.13.type', null=True)
    _se_pat_ringer_ringer11_inst_13_value = TextField(column_name='@se.pat.ringer.ringer11.inst.13.value', null=True)
    _se_pat_ringer_ringer11_inst_2_type = TextField(column_name='@se.pat.ringer.ringer11.inst.2.type', null=True)
    _se_pat_ringer_ringer11_inst_2_value = TextField(column_name='@se.pat.ringer.ringer11.inst.2.value', null=True)
    _se_pat_ringer_ringer11_inst_3_type = TextField(column_name='@se.pat.ringer.ringer11.inst.3.type', null=True)
    _se_pat_ringer_ringer11_inst_3_value = TextField(column_name='@se.pat.ringer.ringer11.inst.3.value', null=True)
    _se_pat_ringer_ringer11_inst_4_type = TextField(column_name='@se.pat.ringer.ringer11.inst.4.type', null=True)
    _se_pat_ringer_ringer11_inst_4_value = TextField(column_name='@se.pat.ringer.ringer11.inst.4.value', null=True)
    _se_pat_ringer_ringer11_inst_5_type = TextField(column_name='@se.pat.ringer.ringer11.inst.5.type', null=True)
    _se_pat_ringer_ringer11_inst_5_value = TextField(column_name='@se.pat.ringer.ringer11.inst.5.value', null=True)
    _se_pat_ringer_ringer11_inst_6_type = TextField(column_name='@se.pat.ringer.ringer11.inst.6.type', null=True)
    _se_pat_ringer_ringer11_inst_6_value = TextField(column_name='@se.pat.ringer.ringer11.inst.6.value', null=True)
    _se_pat_ringer_ringer11_inst_7_type = TextField(column_name='@se.pat.ringer.ringer11.inst.7.type', null=True)
    _se_pat_ringer_ringer11_inst_7_value = TextField(column_name='@se.pat.ringer.ringer11.inst.7.value', null=True)
    _se_pat_ringer_ringer11_inst_8_type = TextField(column_name='@se.pat.ringer.ringer11.inst.8.type', null=True)
    _se_pat_ringer_ringer11_inst_8_value = TextField(column_name='@se.pat.ringer.ringer11.inst.8.value', null=True)
    _se_pat_ringer_ringer11_inst_9_type = TextField(column_name='@se.pat.ringer.ringer11.inst.9.type', null=True)
    _se_pat_ringer_ringer11_inst_9_value = TextField(column_name='@se.pat.ringer.ringer11.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer11.inst'

class Sepatringerringer12(BaseModel):
    _se_pat_ringer_ringer12_name = TextField(column_name='@se.pat.ringer.ringer12.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer12'

class Sepatringerringer12Inst(BaseModel):
    _se_pat_ringer_ringer12_inst_1_type = TextField(column_name='@se.pat.ringer.ringer12.inst.1.type', null=True)
    _se_pat_ringer_ringer12_inst_1_value = TextField(column_name='@se.pat.ringer.ringer12.inst.1.value', null=True)
    _se_pat_ringer_ringer12_inst_2_type = TextField(column_name='@se.pat.ringer.ringer12.inst.2.type', null=True)
    _se_pat_ringer_ringer12_inst_2_value = TextField(column_name='@se.pat.ringer.ringer12.inst.2.value', null=True)
    _se_pat_ringer_ringer12_inst_3_type = TextField(column_name='@se.pat.ringer.ringer12.inst.3.type', null=True)
    _se_pat_ringer_ringer12_inst_3_value = TextField(column_name='@se.pat.ringer.ringer12.inst.3.value', null=True)
    _se_pat_ringer_ringer12_inst_4_type = TextField(column_name='@se.pat.ringer.ringer12.inst.4.type', null=True)
    _se_pat_ringer_ringer12_inst_4_value = TextField(column_name='@se.pat.ringer.ringer12.inst.4.value', null=True)
    _se_pat_ringer_ringer12_inst_5_type = TextField(column_name='@se.pat.ringer.ringer12.inst.5.type', null=True)
    _se_pat_ringer_ringer12_inst_5_value = TextField(column_name='@se.pat.ringer.ringer12.inst.5.value', null=True)
    _se_pat_ringer_ringer12_inst_6_type = TextField(column_name='@se.pat.ringer.ringer12.inst.6.type', null=True)
    _se_pat_ringer_ringer12_inst_6_value = TextField(column_name='@se.pat.ringer.ringer12.inst.6.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer12.inst'

class Sepatringerringer13(BaseModel):
    _se_pat_ringer_ringer13_name = TextField(column_name='@se.pat.ringer.ringer13.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer13'

class Sepatringerringer13Inst(BaseModel):
    _se_pat_ringer_ringer13_inst_1_type = TextField(column_name='@se.pat.ringer.ringer13.inst.1.type', null=True)
    _se_pat_ringer_ringer13_inst_1_value = TextField(column_name='@se.pat.ringer.ringer13.inst.1.value', null=True)
    _se_pat_ringer_ringer13_inst_10_type = TextField(column_name='@se.pat.ringer.ringer13.inst.10.type', null=True)
    _se_pat_ringer_ringer13_inst_10_value = TextField(column_name='@se.pat.ringer.ringer13.inst.10.value', null=True)
    _se_pat_ringer_ringer13_inst_11_type = TextField(column_name='@se.pat.ringer.ringer13.inst.11.type', null=True)
    _se_pat_ringer_ringer13_inst_11_value = TextField(column_name='@se.pat.ringer.ringer13.inst.11.value', null=True)
    _se_pat_ringer_ringer13_inst_12_type = TextField(column_name='@se.pat.ringer.ringer13.inst.12.type', null=True)
    _se_pat_ringer_ringer13_inst_12_value = TextField(column_name='@se.pat.ringer.ringer13.inst.12.value', null=True)
    _se_pat_ringer_ringer13_inst_13_type = TextField(column_name='@se.pat.ringer.ringer13.inst.13.type', null=True)
    _se_pat_ringer_ringer13_inst_13_value = TextField(column_name='@se.pat.ringer.ringer13.inst.13.value', null=True)
    _se_pat_ringer_ringer13_inst_14_type = TextField(column_name='@se.pat.ringer.ringer13.inst.14.type', null=True)
    _se_pat_ringer_ringer13_inst_14_value = TextField(column_name='@se.pat.ringer.ringer13.inst.14.value', null=True)
    _se_pat_ringer_ringer13_inst_15_type = TextField(column_name='@se.pat.ringer.ringer13.inst.15.type', null=True)
    _se_pat_ringer_ringer13_inst_15_value = TextField(column_name='@se.pat.ringer.ringer13.inst.15.value', null=True)
    _se_pat_ringer_ringer13_inst_16_type = TextField(column_name='@se.pat.ringer.ringer13.inst.16.type', null=True)
    _se_pat_ringer_ringer13_inst_16_value = TextField(column_name='@se.pat.ringer.ringer13.inst.16.value', null=True)
    _se_pat_ringer_ringer13_inst_17_type = TextField(column_name='@se.pat.ringer.ringer13.inst.17.type', null=True)
    _se_pat_ringer_ringer13_inst_17_value = TextField(column_name='@se.pat.ringer.ringer13.inst.17.value', null=True)
    _se_pat_ringer_ringer13_inst_18_type = TextField(column_name='@se.pat.ringer.ringer13.inst.18.type', null=True)
    _se_pat_ringer_ringer13_inst_18_value = TextField(column_name='@se.pat.ringer.ringer13.inst.18.value', null=True)
    _se_pat_ringer_ringer13_inst_2_type = TextField(column_name='@se.pat.ringer.ringer13.inst.2.type', null=True)
    _se_pat_ringer_ringer13_inst_2_value = TextField(column_name='@se.pat.ringer.ringer13.inst.2.value', null=True)
    _se_pat_ringer_ringer13_inst_3_type = TextField(column_name='@se.pat.ringer.ringer13.inst.3.type', null=True)
    _se_pat_ringer_ringer13_inst_3_value = TextField(column_name='@se.pat.ringer.ringer13.inst.3.value', null=True)
    _se_pat_ringer_ringer13_inst_4_type = TextField(column_name='@se.pat.ringer.ringer13.inst.4.type', null=True)
    _se_pat_ringer_ringer13_inst_4_value = TextField(column_name='@se.pat.ringer.ringer13.inst.4.value', null=True)
    _se_pat_ringer_ringer13_inst_5_type = TextField(column_name='@se.pat.ringer.ringer13.inst.5.type', null=True)
    _se_pat_ringer_ringer13_inst_5_value = TextField(column_name='@se.pat.ringer.ringer13.inst.5.value', null=True)
    _se_pat_ringer_ringer13_inst_6_type = TextField(column_name='@se.pat.ringer.ringer13.inst.6.type', null=True)
    _se_pat_ringer_ringer13_inst_6_value = TextField(column_name='@se.pat.ringer.ringer13.inst.6.value', null=True)
    _se_pat_ringer_ringer13_inst_7_type = TextField(column_name='@se.pat.ringer.ringer13.inst.7.type', null=True)
    _se_pat_ringer_ringer13_inst_7_value = TextField(column_name='@se.pat.ringer.ringer13.inst.7.value', null=True)
    _se_pat_ringer_ringer13_inst_8_type = TextField(column_name='@se.pat.ringer.ringer13.inst.8.type', null=True)
    _se_pat_ringer_ringer13_inst_8_value = TextField(column_name='@se.pat.ringer.ringer13.inst.8.value', null=True)
    _se_pat_ringer_ringer13_inst_9_type = TextField(column_name='@se.pat.ringer.ringer13.inst.9.type', null=True)
    _se_pat_ringer_ringer13_inst_9_value = TextField(column_name='@se.pat.ringer.ringer13.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer13.inst'

class Sepatringerringer14(BaseModel):
    _se_pat_ringer_ringer14_name = TextField(column_name='@se.pat.ringer.ringer14.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer14'

class Sepatringerringer14Inst(BaseModel):
    _se_pat_ringer_ringer14_inst_1_type = TextField(column_name='@se.pat.ringer.ringer14.inst.1.type', null=True)
    _se_pat_ringer_ringer14_inst_1_value = TextField(column_name='@se.pat.ringer.ringer14.inst.1.value', null=True)
    _se_pat_ringer_ringer14_inst_2_type = TextField(column_name='@se.pat.ringer.ringer14.inst.2.type', null=True)
    _se_pat_ringer_ringer14_inst_2_value = TextField(column_name='@se.pat.ringer.ringer14.inst.2.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer14.inst'

class Sepatringerringer15(BaseModel):
    _se_pat_ringer_ringer15_name = TextField(column_name='@se.pat.ringer.ringer15.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer15'

class Sepatringerringer15Inst(BaseModel):
    _se_pat_ringer_ringer15_inst_1_type = TextField(column_name='@se.pat.ringer.ringer15.inst.1.type', null=True)
    _se_pat_ringer_ringer15_inst_1_value = TextField(column_name='@se.pat.ringer.ringer15.inst.1.value', null=True)
    _se_pat_ringer_ringer15_inst_2_type = TextField(column_name='@se.pat.ringer.ringer15.inst.2.type', null=True)
    _se_pat_ringer_ringer15_inst_2_value = TextField(column_name='@se.pat.ringer.ringer15.inst.2.value', null=True)
    _se_pat_ringer_ringer15_inst_3_type = TextField(column_name='@se.pat.ringer.ringer15.inst.3.type', null=True)
    _se_pat_ringer_ringer15_inst_3_value = TextField(column_name='@se.pat.ringer.ringer15.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer15.inst'

class Sepatringerringer16(BaseModel):
    _se_pat_ringer_ringer16_name = TextField(column_name='@se.pat.ringer.ringer16.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer16'

class Sepatringerringer16Inst(BaseModel):
    _se_pat_ringer_ringer16_inst_1_type = TextField(column_name='@se.pat.ringer.ringer16.inst.1.type', null=True)
    _se_pat_ringer_ringer16_inst_1_value = TextField(column_name='@se.pat.ringer.ringer16.inst.1.value', null=True)
    _se_pat_ringer_ringer16_inst_2_type = TextField(column_name='@se.pat.ringer.ringer16.inst.2.type', null=True)
    _se_pat_ringer_ringer16_inst_2_value = TextField(column_name='@se.pat.ringer.ringer16.inst.2.value', null=True)
    _se_pat_ringer_ringer16_inst_3_type = TextField(column_name='@se.pat.ringer.ringer16.inst.3.type', null=True)
    _se_pat_ringer_ringer16_inst_3_value = TextField(column_name='@se.pat.ringer.ringer16.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer16.inst'

class Sepatringerringer17(BaseModel):
    _se_pat_ringer_ringer17_name = TextField(column_name='@se.pat.ringer.ringer17.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer17'

class Sepatringerringer17Inst(BaseModel):
    _se_pat_ringer_ringer17_inst_1_type = TextField(column_name='@se.pat.ringer.ringer17.inst.1.type', null=True)
    _se_pat_ringer_ringer17_inst_1_value = TextField(column_name='@se.pat.ringer.ringer17.inst.1.value', null=True)
    _se_pat_ringer_ringer17_inst_2_type = TextField(column_name='@se.pat.ringer.ringer17.inst.2.type', null=True)
    _se_pat_ringer_ringer17_inst_2_value = TextField(column_name='@se.pat.ringer.ringer17.inst.2.value', null=True)
    _se_pat_ringer_ringer17_inst_3_type = TextField(column_name='@se.pat.ringer.ringer17.inst.3.type', null=True)
    _se_pat_ringer_ringer17_inst_3_value = TextField(column_name='@se.pat.ringer.ringer17.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer17.inst'

class Sepatringerringer18(BaseModel):
    _se_pat_ringer_ringer18_name = TextField(column_name='@se.pat.ringer.ringer18.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer18'

class Sepatringerringer18Inst(BaseModel):
    _se_pat_ringer_ringer18_inst_1_type = TextField(column_name='@se.pat.ringer.ringer18.inst.1.type', null=True)
    _se_pat_ringer_ringer18_inst_1_value = TextField(column_name='@se.pat.ringer.ringer18.inst.1.value', null=True)
    _se_pat_ringer_ringer18_inst_2_type = TextField(column_name='@se.pat.ringer.ringer18.inst.2.type', null=True)
    _se_pat_ringer_ringer18_inst_2_value = TextField(column_name='@se.pat.ringer.ringer18.inst.2.value', null=True)
    _se_pat_ringer_ringer18_inst_3_type = TextField(column_name='@se.pat.ringer.ringer18.inst.3.type', null=True)
    _se_pat_ringer_ringer18_inst_3_value = TextField(column_name='@se.pat.ringer.ringer18.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer18.inst'

class Sepatringerringer19(BaseModel):
    _se_pat_ringer_ringer19_name = TextField(column_name='@se.pat.ringer.ringer19.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer19'

class Sepatringerringer19Inst(BaseModel):
    _se_pat_ringer_ringer19_inst_1_type = TextField(column_name='@se.pat.ringer.ringer19.inst.1.type', null=True)
    _se_pat_ringer_ringer19_inst_1_value = TextField(column_name='@se.pat.ringer.ringer19.inst.1.value', null=True)
    _se_pat_ringer_ringer19_inst_2_type = TextField(column_name='@se.pat.ringer.ringer19.inst.2.type', null=True)
    _se_pat_ringer_ringer19_inst_2_value = TextField(column_name='@se.pat.ringer.ringer19.inst.2.value', null=True)
    _se_pat_ringer_ringer19_inst_3_type = TextField(column_name='@se.pat.ringer.ringer19.inst.3.type', null=True)
    _se_pat_ringer_ringer19_inst_3_value = TextField(column_name='@se.pat.ringer.ringer19.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer19.inst'

class Sepatringerringer2(BaseModel):
    _se_pat_ringer_ringer2_name = TextField(column_name='@se.pat.ringer.ringer2.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer2'

class Sepatringerringer2Inst(BaseModel):
    _se_pat_ringer_ringer2_inst_1_type = TextField(column_name='@se.pat.ringer.ringer2.inst.1.type', null=True)
    _se_pat_ringer_ringer2_inst_1_value = TextField(column_name='@se.pat.ringer.ringer2.inst.1.value', null=True)
    _se_pat_ringer_ringer2_inst_10_type = TextField(column_name='@se.pat.ringer.ringer2.inst.10.type', null=True)
    _se_pat_ringer_ringer2_inst_10_value = TextField(column_name='@se.pat.ringer.ringer2.inst.10.value', null=True)
    _se_pat_ringer_ringer2_inst_11_type = TextField(column_name='@se.pat.ringer.ringer2.inst.11.type', null=True)
    _se_pat_ringer_ringer2_inst_11_value = TextField(column_name='@se.pat.ringer.ringer2.inst.11.value', null=True)
    _se_pat_ringer_ringer2_inst_12_type = TextField(column_name='@se.pat.ringer.ringer2.inst.12.type', null=True)
    _se_pat_ringer_ringer2_inst_12_value = TextField(column_name='@se.pat.ringer.ringer2.inst.12.value', null=True)
    _se_pat_ringer_ringer2_inst_2_type = TextField(column_name='@se.pat.ringer.ringer2.inst.2.type', null=True)
    _se_pat_ringer_ringer2_inst_2_value = TextField(column_name='@se.pat.ringer.ringer2.inst.2.value', null=True)
    _se_pat_ringer_ringer2_inst_3_type = TextField(column_name='@se.pat.ringer.ringer2.inst.3.type', null=True)
    _se_pat_ringer_ringer2_inst_3_value = TextField(column_name='@se.pat.ringer.ringer2.inst.3.value', null=True)
    _se_pat_ringer_ringer2_inst_4_type = TextField(column_name='@se.pat.ringer.ringer2.inst.4.type', null=True)
    _se_pat_ringer_ringer2_inst_4_value = TextField(column_name='@se.pat.ringer.ringer2.inst.4.value', null=True)
    _se_pat_ringer_ringer2_inst_5_type = TextField(column_name='@se.pat.ringer.ringer2.inst.5.type', null=True)
    _se_pat_ringer_ringer2_inst_5_value = TextField(column_name='@se.pat.ringer.ringer2.inst.5.value', null=True)
    _se_pat_ringer_ringer2_inst_6_type = TextField(column_name='@se.pat.ringer.ringer2.inst.6.type', null=True)
    _se_pat_ringer_ringer2_inst_6_value = TextField(column_name='@se.pat.ringer.ringer2.inst.6.value', null=True)
    _se_pat_ringer_ringer2_inst_7_type = TextField(column_name='@se.pat.ringer.ringer2.inst.7.type', null=True)
    _se_pat_ringer_ringer2_inst_7_value = TextField(column_name='@se.pat.ringer.ringer2.inst.7.value', null=True)
    _se_pat_ringer_ringer2_inst_8_type = TextField(column_name='@se.pat.ringer.ringer2.inst.8.type', null=True)
    _se_pat_ringer_ringer2_inst_8_value = TextField(column_name='@se.pat.ringer.ringer2.inst.8.value', null=True)
    _se_pat_ringer_ringer2_inst_9_type = TextField(column_name='@se.pat.ringer.ringer2.inst.9.type', null=True)
    _se_pat_ringer_ringer2_inst_9_value = TextField(column_name='@se.pat.ringer.ringer2.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer2.inst'

class Sepatringerringer20(BaseModel):
    _se_pat_ringer_ringer20_name = TextField(column_name='@se.pat.ringer.ringer20.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer20'

class Sepatringerringer20Inst(BaseModel):
    _se_pat_ringer_ringer20_inst_1_type = TextField(column_name='@se.pat.ringer.ringer20.inst.1.type', null=True)
    _se_pat_ringer_ringer20_inst_1_value = TextField(column_name='@se.pat.ringer.ringer20.inst.1.value', null=True)
    _se_pat_ringer_ringer20_inst_2_type = TextField(column_name='@se.pat.ringer.ringer20.inst.2.type', null=True)
    _se_pat_ringer_ringer20_inst_2_value = TextField(column_name='@se.pat.ringer.ringer20.inst.2.value', null=True)
    _se_pat_ringer_ringer20_inst_3_type = TextField(column_name='@se.pat.ringer.ringer20.inst.3.type', null=True)
    _se_pat_ringer_ringer20_inst_3_value = TextField(column_name='@se.pat.ringer.ringer20.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer20.inst'

class Sepatringerringer21(BaseModel):
    _se_pat_ringer_ringer21_name = TextField(column_name='@se.pat.ringer.ringer21.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer21'

class Sepatringerringer21Inst(BaseModel):
    _se_pat_ringer_ringer21_inst_1_type = TextField(column_name='@se.pat.ringer.ringer21.inst.1.type', null=True)
    _se_pat_ringer_ringer21_inst_1_value = TextField(column_name='@se.pat.ringer.ringer21.inst.1.value', null=True)
    _se_pat_ringer_ringer21_inst_2_type = TextField(column_name='@se.pat.ringer.ringer21.inst.2.type', null=True)
    _se_pat_ringer_ringer21_inst_2_value = TextField(column_name='@se.pat.ringer.ringer21.inst.2.value', null=True)
    _se_pat_ringer_ringer21_inst_3_type = TextField(column_name='@se.pat.ringer.ringer21.inst.3.type', null=True)
    _se_pat_ringer_ringer21_inst_3_value = TextField(column_name='@se.pat.ringer.ringer21.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer21.inst'

class Sepatringerringer22(BaseModel):
    _se_pat_ringer_ringer22_name = TextField(column_name='@se.pat.ringer.ringer22.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer22'

class Sepatringerringer22Inst(BaseModel):
    _se_pat_ringer_ringer22_inst_1_type = TextField(column_name='@se.pat.ringer.ringer22.inst.1.type', null=True)
    _se_pat_ringer_ringer22_inst_1_value = TextField(column_name='@se.pat.ringer.ringer22.inst.1.value', null=True)
    _se_pat_ringer_ringer22_inst_2_type = TextField(column_name='@se.pat.ringer.ringer22.inst.2.type', null=True)
    _se_pat_ringer_ringer22_inst_2_value = TextField(column_name='@se.pat.ringer.ringer22.inst.2.value', null=True)
    _se_pat_ringer_ringer22_inst_3_type = TextField(column_name='@se.pat.ringer.ringer22.inst.3.type', null=True)
    _se_pat_ringer_ringer22_inst_3_value = TextField(column_name='@se.pat.ringer.ringer22.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer22.inst'

class Sepatringerringer23(BaseModel):
    _se_pat_ringer_ringer23_name = TextField(column_name='@se.pat.ringer.ringer23.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer23'

class Sepatringerringer23Inst(BaseModel):
    _se_pat_ringer_ringer23_inst_1_type = TextField(column_name='@se.pat.ringer.ringer23.inst.1.type', null=True)
    _se_pat_ringer_ringer23_inst_1_value = TextField(column_name='@se.pat.ringer.ringer23.inst.1.value', null=True)
    _se_pat_ringer_ringer23_inst_2_type = TextField(column_name='@se.pat.ringer.ringer23.inst.2.type', null=True)
    _se_pat_ringer_ringer23_inst_2_value = TextField(column_name='@se.pat.ringer.ringer23.inst.2.value', null=True)
    _se_pat_ringer_ringer23_inst_3_type = TextField(column_name='@se.pat.ringer.ringer23.inst.3.type', null=True)
    _se_pat_ringer_ringer23_inst_3_value = TextField(column_name='@se.pat.ringer.ringer23.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer23.inst'

class Sepatringerringer24(BaseModel):
    _se_pat_ringer_ringer24_name = TextField(column_name='@se.pat.ringer.ringer24.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer24'

class Sepatringerringer24Inst(BaseModel):
    _se_pat_ringer_ringer24_inst_1_type = TextField(column_name='@se.pat.ringer.ringer24.inst.1.type', null=True)
    _se_pat_ringer_ringer24_inst_1_value = TextField(column_name='@se.pat.ringer.ringer24.inst.1.value', null=True)
    _se_pat_ringer_ringer24_inst_2_type = TextField(column_name='@se.pat.ringer.ringer24.inst.2.type', null=True)
    _se_pat_ringer_ringer24_inst_2_value = TextField(column_name='@se.pat.ringer.ringer24.inst.2.value', null=True)
    _se_pat_ringer_ringer24_inst_3_type = TextField(column_name='@se.pat.ringer.ringer24.inst.3.type', null=True)
    _se_pat_ringer_ringer24_inst_3_value = TextField(column_name='@se.pat.ringer.ringer24.inst.3.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer24.inst'

class Sepatringerringer3(BaseModel):
    _se_pat_ringer_ringer3_name = TextField(column_name='@se.pat.ringer.ringer3.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer3'

class Sepatringerringer3Inst(BaseModel):
    _se_pat_ringer_ringer3_inst_1_type = TextField(column_name='@se.pat.ringer.ringer3.inst.1.type', null=True)
    _se_pat_ringer_ringer3_inst_1_value = TextField(column_name='@se.pat.ringer.ringer3.inst.1.value', null=True)
    _se_pat_ringer_ringer3_inst_10_type = TextField(column_name='@se.pat.ringer.ringer3.inst.10.type', null=True)
    _se_pat_ringer_ringer3_inst_10_value = TextField(column_name='@se.pat.ringer.ringer3.inst.10.value', null=True)
    _se_pat_ringer_ringer3_inst_11_type = TextField(column_name='@se.pat.ringer.ringer3.inst.11.type', null=True)
    _se_pat_ringer_ringer3_inst_11_value = TextField(column_name='@se.pat.ringer.ringer3.inst.11.value', null=True)
    _se_pat_ringer_ringer3_inst_2_type = TextField(column_name='@se.pat.ringer.ringer3.inst.2.type', null=True)
    _se_pat_ringer_ringer3_inst_2_value = TextField(column_name='@se.pat.ringer.ringer3.inst.2.value', null=True)
    _se_pat_ringer_ringer3_inst_3_type = TextField(column_name='@se.pat.ringer.ringer3.inst.3.type', null=True)
    _se_pat_ringer_ringer3_inst_3_value = TextField(column_name='@se.pat.ringer.ringer3.inst.3.value', null=True)
    _se_pat_ringer_ringer3_inst_4_type = TextField(column_name='@se.pat.ringer.ringer3.inst.4.type', null=True)
    _se_pat_ringer_ringer3_inst_4_value = TextField(column_name='@se.pat.ringer.ringer3.inst.4.value', null=True)
    _se_pat_ringer_ringer3_inst_5_type = TextField(column_name='@se.pat.ringer.ringer3.inst.5.type', null=True)
    _se_pat_ringer_ringer3_inst_5_value = TextField(column_name='@se.pat.ringer.ringer3.inst.5.value', null=True)
    _se_pat_ringer_ringer3_inst_6_type = TextField(column_name='@se.pat.ringer.ringer3.inst.6.type', null=True)
    _se_pat_ringer_ringer3_inst_6_value = TextField(column_name='@se.pat.ringer.ringer3.inst.6.value', null=True)
    _se_pat_ringer_ringer3_inst_7_type = TextField(column_name='@se.pat.ringer.ringer3.inst.7.type', null=True)
    _se_pat_ringer_ringer3_inst_7_value = TextField(column_name='@se.pat.ringer.ringer3.inst.7.value', null=True)
    _se_pat_ringer_ringer3_inst_8_type = TextField(column_name='@se.pat.ringer.ringer3.inst.8.type', null=True)
    _se_pat_ringer_ringer3_inst_8_value = TextField(column_name='@se.pat.ringer.ringer3.inst.8.value', null=True)
    _se_pat_ringer_ringer3_inst_9_type = TextField(column_name='@se.pat.ringer.ringer3.inst.9.type', null=True)
    _se_pat_ringer_ringer3_inst_9_value = TextField(column_name='@se.pat.ringer.ringer3.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer3.inst'

class Sepatringerringer4(BaseModel):
    _se_pat_ringer_ringer4_name = TextField(column_name='@se.pat.ringer.ringer4.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer4'

class Sepatringerringer4Inst(BaseModel):
    _se_pat_ringer_ringer4_inst_1_type = TextField(column_name='@se.pat.ringer.ringer4.inst.1.type', null=True)
    _se_pat_ringer_ringer4_inst_1_value = TextField(column_name='@se.pat.ringer.ringer4.inst.1.value', null=True)
    _se_pat_ringer_ringer4_inst_10_type = TextField(column_name='@se.pat.ringer.ringer4.inst.10.type', null=True)
    _se_pat_ringer_ringer4_inst_10_value = TextField(column_name='@se.pat.ringer.ringer4.inst.10.value', null=True)
    _se_pat_ringer_ringer4_inst_11_type = TextField(column_name='@se.pat.ringer.ringer4.inst.11.type', null=True)
    _se_pat_ringer_ringer4_inst_11_value = TextField(column_name='@se.pat.ringer.ringer4.inst.11.value', null=True)
    _se_pat_ringer_ringer4_inst_12_type = TextField(column_name='@se.pat.ringer.ringer4.inst.12.type', null=True)
    _se_pat_ringer_ringer4_inst_12_value = TextField(column_name='@se.pat.ringer.ringer4.inst.12.value', null=True)
    _se_pat_ringer_ringer4_inst_2_type = TextField(column_name='@se.pat.ringer.ringer4.inst.2.type', null=True)
    _se_pat_ringer_ringer4_inst_2_value = TextField(column_name='@se.pat.ringer.ringer4.inst.2.value', null=True)
    _se_pat_ringer_ringer4_inst_3_type = TextField(column_name='@se.pat.ringer.ringer4.inst.3.type', null=True)
    _se_pat_ringer_ringer4_inst_3_value = TextField(column_name='@se.pat.ringer.ringer4.inst.3.value', null=True)
    _se_pat_ringer_ringer4_inst_4_type = TextField(column_name='@se.pat.ringer.ringer4.inst.4.type', null=True)
    _se_pat_ringer_ringer4_inst_4_value = TextField(column_name='@se.pat.ringer.ringer4.inst.4.value', null=True)
    _se_pat_ringer_ringer4_inst_5_type = TextField(column_name='@se.pat.ringer.ringer4.inst.5.type', null=True)
    _se_pat_ringer_ringer4_inst_5_value = TextField(column_name='@se.pat.ringer.ringer4.inst.5.value', null=True)
    _se_pat_ringer_ringer4_inst_6_type = TextField(column_name='@se.pat.ringer.ringer4.inst.6.type', null=True)
    _se_pat_ringer_ringer4_inst_6_value = TextField(column_name='@se.pat.ringer.ringer4.inst.6.value', null=True)
    _se_pat_ringer_ringer4_inst_7_type = TextField(column_name='@se.pat.ringer.ringer4.inst.7.type', null=True)
    _se_pat_ringer_ringer4_inst_7_value = TextField(column_name='@se.pat.ringer.ringer4.inst.7.value', null=True)
    _se_pat_ringer_ringer4_inst_8_type = TextField(column_name='@se.pat.ringer.ringer4.inst.8.type', null=True)
    _se_pat_ringer_ringer4_inst_8_value = TextField(column_name='@se.pat.ringer.ringer4.inst.8.value', null=True)
    _se_pat_ringer_ringer4_inst_9_type = TextField(column_name='@se.pat.ringer.ringer4.inst.9.type', null=True)
    _se_pat_ringer_ringer4_inst_9_value = TextField(column_name='@se.pat.ringer.ringer4.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer4.inst'

class Sepatringerringer5(BaseModel):
    _se_pat_ringer_ringer5_name = TextField(column_name='@se.pat.ringer.ringer5.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer5'

class Sepatringerringer5Inst(BaseModel):
    _se_pat_ringer_ringer5_inst_1_type = TextField(column_name='@se.pat.ringer.ringer5.inst.1.type', null=True)
    _se_pat_ringer_ringer5_inst_1_value = TextField(column_name='@se.pat.ringer.ringer5.inst.1.value', null=True)
    _se_pat_ringer_ringer5_inst_10_type = TextField(column_name='@se.pat.ringer.ringer5.inst.10.type', null=True)
    _se_pat_ringer_ringer5_inst_10_value = TextField(column_name='@se.pat.ringer.ringer5.inst.10.value', null=True)
    _se_pat_ringer_ringer5_inst_11_type = TextField(column_name='@se.pat.ringer.ringer5.inst.11.type', null=True)
    _se_pat_ringer_ringer5_inst_11_value = TextField(column_name='@se.pat.ringer.ringer5.inst.11.value', null=True)
    _se_pat_ringer_ringer5_inst_2_type = TextField(column_name='@se.pat.ringer.ringer5.inst.2.type', null=True)
    _se_pat_ringer_ringer5_inst_2_value = TextField(column_name='@se.pat.ringer.ringer5.inst.2.value', null=True)
    _se_pat_ringer_ringer5_inst_3_type = TextField(column_name='@se.pat.ringer.ringer5.inst.3.type', null=True)
    _se_pat_ringer_ringer5_inst_3_value = TextField(column_name='@se.pat.ringer.ringer5.inst.3.value', null=True)
    _se_pat_ringer_ringer5_inst_4_type = TextField(column_name='@se.pat.ringer.ringer5.inst.4.type', null=True)
    _se_pat_ringer_ringer5_inst_4_value = TextField(column_name='@se.pat.ringer.ringer5.inst.4.value', null=True)
    _se_pat_ringer_ringer5_inst_5_type = TextField(column_name='@se.pat.ringer.ringer5.inst.5.type', null=True)
    _se_pat_ringer_ringer5_inst_5_value = TextField(column_name='@se.pat.ringer.ringer5.inst.5.value', null=True)
    _se_pat_ringer_ringer5_inst_6_type = TextField(column_name='@se.pat.ringer.ringer5.inst.6.type', null=True)
    _se_pat_ringer_ringer5_inst_6_value = TextField(column_name='@se.pat.ringer.ringer5.inst.6.value', null=True)
    _se_pat_ringer_ringer5_inst_7_type = TextField(column_name='@se.pat.ringer.ringer5.inst.7.type', null=True)
    _se_pat_ringer_ringer5_inst_7_value = TextField(column_name='@se.pat.ringer.ringer5.inst.7.value', null=True)
    _se_pat_ringer_ringer5_inst_8_type = TextField(column_name='@se.pat.ringer.ringer5.inst.8.type', null=True)
    _se_pat_ringer_ringer5_inst_8_value = TextField(column_name='@se.pat.ringer.ringer5.inst.8.value', null=True)
    _se_pat_ringer_ringer5_inst_9_type = TextField(column_name='@se.pat.ringer.ringer5.inst.9.type', null=True)
    _se_pat_ringer_ringer5_inst_9_value = TextField(column_name='@se.pat.ringer.ringer5.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer5.inst'

class Sepatringerringer6(BaseModel):
    _se_pat_ringer_ringer6_name = TextField(column_name='@se.pat.ringer.ringer6.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer6'

class Sepatringerringer6Inst(BaseModel):
    _se_pat_ringer_ringer6_inst_1_type = TextField(column_name='@se.pat.ringer.ringer6.inst.1.type', null=True)
    _se_pat_ringer_ringer6_inst_1_value = TextField(column_name='@se.pat.ringer.ringer6.inst.1.value', null=True)
    _se_pat_ringer_ringer6_inst_10_type = TextField(column_name='@se.pat.ringer.ringer6.inst.10.type', null=True)
    _se_pat_ringer_ringer6_inst_10_value = TextField(column_name='@se.pat.ringer.ringer6.inst.10.value', null=True)
    _se_pat_ringer_ringer6_inst_11_type = TextField(column_name='@se.pat.ringer.ringer6.inst.11.type', null=True)
    _se_pat_ringer_ringer6_inst_11_value = TextField(column_name='@se.pat.ringer.ringer6.inst.11.value', null=True)
    _se_pat_ringer_ringer6_inst_12_type = TextField(column_name='@se.pat.ringer.ringer6.inst.12.type', null=True)
    _se_pat_ringer_ringer6_inst_12_value = TextField(column_name='@se.pat.ringer.ringer6.inst.12.value', null=True)
    _se_pat_ringer_ringer6_inst_2_type = TextField(column_name='@se.pat.ringer.ringer6.inst.2.type', null=True)
    _se_pat_ringer_ringer6_inst_2_value = TextField(column_name='@se.pat.ringer.ringer6.inst.2.value', null=True)
    _se_pat_ringer_ringer6_inst_3_type = TextField(column_name='@se.pat.ringer.ringer6.inst.3.type', null=True)
    _se_pat_ringer_ringer6_inst_3_value = TextField(column_name='@se.pat.ringer.ringer6.inst.3.value', null=True)
    _se_pat_ringer_ringer6_inst_4_type = TextField(column_name='@se.pat.ringer.ringer6.inst.4.type', null=True)
    _se_pat_ringer_ringer6_inst_4_value = TextField(column_name='@se.pat.ringer.ringer6.inst.4.value', null=True)
    _se_pat_ringer_ringer6_inst_5_type = TextField(column_name='@se.pat.ringer.ringer6.inst.5.type', null=True)
    _se_pat_ringer_ringer6_inst_5_value = TextField(column_name='@se.pat.ringer.ringer6.inst.5.value', null=True)
    _se_pat_ringer_ringer6_inst_6_type = TextField(column_name='@se.pat.ringer.ringer6.inst.6.type', null=True)
    _se_pat_ringer_ringer6_inst_6_value = TextField(column_name='@se.pat.ringer.ringer6.inst.6.value', null=True)
    _se_pat_ringer_ringer6_inst_7_type = TextField(column_name='@se.pat.ringer.ringer6.inst.7.type', null=True)
    _se_pat_ringer_ringer6_inst_7_value = TextField(column_name='@se.pat.ringer.ringer6.inst.7.value', null=True)
    _se_pat_ringer_ringer6_inst_8_type = TextField(column_name='@se.pat.ringer.ringer6.inst.8.type', null=True)
    _se_pat_ringer_ringer6_inst_8_value = TextField(column_name='@se.pat.ringer.ringer6.inst.8.value', null=True)
    _se_pat_ringer_ringer6_inst_9_type = TextField(column_name='@se.pat.ringer.ringer6.inst.9.type', null=True)
    _se_pat_ringer_ringer6_inst_9_value = TextField(column_name='@se.pat.ringer.ringer6.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer6.inst'

class Sepatringerringer7(BaseModel):
    _se_pat_ringer_ringer7_name = TextField(column_name='@se.pat.ringer.ringer7.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer7'

class Sepatringerringer7Inst(BaseModel):
    _se_pat_ringer_ringer7_inst_1_type = TextField(column_name='@se.pat.ringer.ringer7.inst.1.type', null=True)
    _se_pat_ringer_ringer7_inst_1_value = TextField(column_name='@se.pat.ringer.ringer7.inst.1.value', null=True)
    _se_pat_ringer_ringer7_inst_10_type = TextField(column_name='@se.pat.ringer.ringer7.inst.10.type', null=True)
    _se_pat_ringer_ringer7_inst_10_value = TextField(column_name='@se.pat.ringer.ringer7.inst.10.value', null=True)
    _se_pat_ringer_ringer7_inst_11_type = TextField(column_name='@se.pat.ringer.ringer7.inst.11.type', null=True)
    _se_pat_ringer_ringer7_inst_11_value = TextField(column_name='@se.pat.ringer.ringer7.inst.11.value', null=True)
    _se_pat_ringer_ringer7_inst_2_type = TextField(column_name='@se.pat.ringer.ringer7.inst.2.type', null=True)
    _se_pat_ringer_ringer7_inst_2_value = TextField(column_name='@se.pat.ringer.ringer7.inst.2.value', null=True)
    _se_pat_ringer_ringer7_inst_3_type = TextField(column_name='@se.pat.ringer.ringer7.inst.3.type', null=True)
    _se_pat_ringer_ringer7_inst_3_value = TextField(column_name='@se.pat.ringer.ringer7.inst.3.value', null=True)
    _se_pat_ringer_ringer7_inst_4_type = TextField(column_name='@se.pat.ringer.ringer7.inst.4.type', null=True)
    _se_pat_ringer_ringer7_inst_4_value = TextField(column_name='@se.pat.ringer.ringer7.inst.4.value', null=True)
    _se_pat_ringer_ringer7_inst_5_type = TextField(column_name='@se.pat.ringer.ringer7.inst.5.type', null=True)
    _se_pat_ringer_ringer7_inst_5_value = TextField(column_name='@se.pat.ringer.ringer7.inst.5.value', null=True)
    _se_pat_ringer_ringer7_inst_6_type = TextField(column_name='@se.pat.ringer.ringer7.inst.6.type', null=True)
    _se_pat_ringer_ringer7_inst_6_value = TextField(column_name='@se.pat.ringer.ringer7.inst.6.value', null=True)
    _se_pat_ringer_ringer7_inst_7_type = TextField(column_name='@se.pat.ringer.ringer7.inst.7.type', null=True)
    _se_pat_ringer_ringer7_inst_7_value = TextField(column_name='@se.pat.ringer.ringer7.inst.7.value', null=True)
    _se_pat_ringer_ringer7_inst_8_type = TextField(column_name='@se.pat.ringer.ringer7.inst.8.type', null=True)
    _se_pat_ringer_ringer7_inst_8_value = TextField(column_name='@se.pat.ringer.ringer7.inst.8.value', null=True)
    _se_pat_ringer_ringer7_inst_9_type = TextField(column_name='@se.pat.ringer.ringer7.inst.9.type', null=True)
    _se_pat_ringer_ringer7_inst_9_value = TextField(column_name='@se.pat.ringer.ringer7.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer7.inst'

class Sepatringerringer8(BaseModel):
    _se_pat_ringer_ringer8_name = TextField(column_name='@se.pat.ringer.ringer8.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer8'

class Sepatringerringer8Inst(BaseModel):
    _se_pat_ringer_ringer8_inst_1_type = TextField(column_name='@se.pat.ringer.ringer8.inst.1.type', null=True)
    _se_pat_ringer_ringer8_inst_1_value = TextField(column_name='@se.pat.ringer.ringer8.inst.1.value', null=True)
    _se_pat_ringer_ringer8_inst_10_type = TextField(column_name='@se.pat.ringer.ringer8.inst.10.type', null=True)
    _se_pat_ringer_ringer8_inst_10_value = TextField(column_name='@se.pat.ringer.ringer8.inst.10.value', null=True)
    _se_pat_ringer_ringer8_inst_11_type = TextField(column_name='@se.pat.ringer.ringer8.inst.11.type', null=True)
    _se_pat_ringer_ringer8_inst_11_value = TextField(column_name='@se.pat.ringer.ringer8.inst.11.value', null=True)
    _se_pat_ringer_ringer8_inst_12_type = TextField(column_name='@se.pat.ringer.ringer8.inst.12.type', null=True)
    _se_pat_ringer_ringer8_inst_12_value = TextField(column_name='@se.pat.ringer.ringer8.inst.12.value', null=True)
    _se_pat_ringer_ringer8_inst_2_type = TextField(column_name='@se.pat.ringer.ringer8.inst.2.type', null=True)
    _se_pat_ringer_ringer8_inst_2_value = TextField(column_name='@se.pat.ringer.ringer8.inst.2.value', null=True)
    _se_pat_ringer_ringer8_inst_3_type = TextField(column_name='@se.pat.ringer.ringer8.inst.3.type', null=True)
    _se_pat_ringer_ringer8_inst_3_value = TextField(column_name='@se.pat.ringer.ringer8.inst.3.value', null=True)
    _se_pat_ringer_ringer8_inst_4_type = TextField(column_name='@se.pat.ringer.ringer8.inst.4.type', null=True)
    _se_pat_ringer_ringer8_inst_4_value = TextField(column_name='@se.pat.ringer.ringer8.inst.4.value', null=True)
    _se_pat_ringer_ringer8_inst_5_type = TextField(column_name='@se.pat.ringer.ringer8.inst.5.type', null=True)
    _se_pat_ringer_ringer8_inst_5_value = TextField(column_name='@se.pat.ringer.ringer8.inst.5.value', null=True)
    _se_pat_ringer_ringer8_inst_6_type = TextField(column_name='@se.pat.ringer.ringer8.inst.6.type', null=True)
    _se_pat_ringer_ringer8_inst_6_value = TextField(column_name='@se.pat.ringer.ringer8.inst.6.value', null=True)
    _se_pat_ringer_ringer8_inst_7_type = TextField(column_name='@se.pat.ringer.ringer8.inst.7.type', null=True)
    _se_pat_ringer_ringer8_inst_7_value = TextField(column_name='@se.pat.ringer.ringer8.inst.7.value', null=True)
    _se_pat_ringer_ringer8_inst_8_type = TextField(column_name='@se.pat.ringer.ringer8.inst.8.type', null=True)
    _se_pat_ringer_ringer8_inst_8_value = TextField(column_name='@se.pat.ringer.ringer8.inst.8.value', null=True)
    _se_pat_ringer_ringer8_inst_9_type = TextField(column_name='@se.pat.ringer.ringer8.inst.9.type', null=True)
    _se_pat_ringer_ringer8_inst_9_value = TextField(column_name='@se.pat.ringer.ringer8.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer8.inst'

class Sepatringerringer9(BaseModel):
    _se_pat_ringer_ringer9_name = TextField(column_name='@se.pat.ringer.ringer9.name', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer9'

class Sepatringerringer9Inst(BaseModel):
    _se_pat_ringer_ringer9_inst_1_type = TextField(column_name='@se.pat.ringer.ringer9.inst.1.type', null=True)
    _se_pat_ringer_ringer9_inst_1_value = TextField(column_name='@se.pat.ringer.ringer9.inst.1.value', null=True)
    _se_pat_ringer_ringer9_inst_10_type = TextField(column_name='@se.pat.ringer.ringer9.inst.10.type', null=True)
    _se_pat_ringer_ringer9_inst_10_value = TextField(column_name='@se.pat.ringer.ringer9.inst.10.value', null=True)
    _se_pat_ringer_ringer9_inst_11_type = TextField(column_name='@se.pat.ringer.ringer9.inst.11.type', null=True)
    _se_pat_ringer_ringer9_inst_11_value = TextField(column_name='@se.pat.ringer.ringer9.inst.11.value', null=True)
    _se_pat_ringer_ringer9_inst_2_type = TextField(column_name='@se.pat.ringer.ringer9.inst.2.type', null=True)
    _se_pat_ringer_ringer9_inst_2_value = TextField(column_name='@se.pat.ringer.ringer9.inst.2.value', null=True)
    _se_pat_ringer_ringer9_inst_3_type = TextField(column_name='@se.pat.ringer.ringer9.inst.3.type', null=True)
    _se_pat_ringer_ringer9_inst_3_value = TextField(column_name='@se.pat.ringer.ringer9.inst.3.value', null=True)
    _se_pat_ringer_ringer9_inst_4_type = TextField(column_name='@se.pat.ringer.ringer9.inst.4.type', null=True)
    _se_pat_ringer_ringer9_inst_4_value = TextField(column_name='@se.pat.ringer.ringer9.inst.4.value', null=True)
    _se_pat_ringer_ringer9_inst_5_type = TextField(column_name='@se.pat.ringer.ringer9.inst.5.type', null=True)
    _se_pat_ringer_ringer9_inst_5_value = TextField(column_name='@se.pat.ringer.ringer9.inst.5.value', null=True)
    _se_pat_ringer_ringer9_inst_6_type = TextField(column_name='@se.pat.ringer.ringer9.inst.6.type', null=True)
    _se_pat_ringer_ringer9_inst_6_value = TextField(column_name='@se.pat.ringer.ringer9.inst.6.value', null=True)
    _se_pat_ringer_ringer9_inst_7_type = TextField(column_name='@se.pat.ringer.ringer9.inst.7.type', null=True)
    _se_pat_ringer_ringer9_inst_7_value = TextField(column_name='@se.pat.ringer.ringer9.inst.7.value', null=True)
    _se_pat_ringer_ringer9_inst_8_type = TextField(column_name='@se.pat.ringer.ringer9.inst.8.type', null=True)
    _se_pat_ringer_ringer9_inst_8_value = TextField(column_name='@se.pat.ringer.ringer9.inst.8.value', null=True)
    _se_pat_ringer_ringer9_inst_9_type = TextField(column_name='@se.pat.ringer.ringer9.inst.9.type', null=True)
    _se_pat_ringer_ringer9_inst_9_value = TextField(column_name='@se.pat.ringer.ringer9.inst.9.value', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'se.pat.ringer.ringer9.inst'

class Sec(BaseModel):
    _sec_tag_serial_no = TextField(column_name='@sec.tagSerialNo', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec'

class Sech235MediaEncryption(BaseModel):
    _sec_h235_media_encryption_enabled = TextField(column_name='@sec.H235.mediaEncryption.enabled', null=True)
    _sec_h235_media_encryption_offer = TextField(column_name='@sec.H235.mediaEncryption.offer', null=True)
    _sec_h235_media_encryption_require = TextField(column_name='@sec.H235.mediaEncryption.require', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.H235.mediaEncryption'

class Sectls(BaseModel):
    _sec_tls_cipher_list = TextField(column_name='@sec.TLS.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS'

class Sectlsldap(BaseModel):
    _sec_tls_ldap_cipher_list = TextField(column_name='@sec.TLS.LDAP.cipherList', null=True)
    _sec_tls_ldap_custom_ca_cert_url = TextField(column_name='@sec.TLS.LDAP.customCaCertUrl', null=True)
    _sec_tls_ldap_strict_cert_common_name_validation = TextField(column_name='@sec.TLS.LDAP.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.LDAP'

class Sectlssip(BaseModel):
    _sec_tls_sip_cipher_list = TextField(column_name='@sec.TLS.SIP.cipherList', null=True)
    _sec_tls_sip_strict_cert_common_name_validation = TextField(column_name='@sec.TLS.SIP.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.SIP'

class Sectlssopi(BaseModel):
    _sec_tls_sopi_cipher_list = TextField(column_name='@sec.TLS.SOPI.cipherList', null=True)
    _sec_tls_sopi_strict_cert_common_name_validation = TextField(column_name='@sec.TLS.SOPI.strictCertCommonNameValidation', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.SOPI'

class Sectlsbrowser(BaseModel):
    _sec_tls_browser_cipher_list = TextField(column_name='@sec.TLS.browser.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.browser'

class SectlscustomCaCert(BaseModel):
    _sec_tls_custom_ca_cert_1 = TextField(column_name='@sec.TLS.customCaCert.1', null=True)
    _sec_tls_custom_ca_cert_2 = TextField(column_name='@sec.TLS.customCaCert.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.customCaCert'

class SectlscustomDeviceCert(BaseModel):
    _sec_tls_custom_device_cert_1 = TextField(column_name='@sec.TLS.customDeviceCert.1', null=True)
    _sec_tls_custom_device_cert_2 = TextField(column_name='@sec.TLS.customDeviceCert.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.customDeviceCert'

class SectlscustomDeviceKey(BaseModel):
    _sec_tls_custom_device_key_1 = TextField(column_name='@sec.TLS.customDeviceKey.1', null=True)
    _sec_tls_custom_device_key_2 = TextField(column_name='@sec.TLS.customDeviceKey.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.customDeviceKey'

class SectlsexchangeServices(BaseModel):
    _sec_tls_exchange_services_cipher_list = TextField(column_name='@sec.TLS.exchangeServices.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.exchangeServices'

class Sectlsprofile(BaseModel):
    _sec_tls_profile_1_ca_cert_application1 = TextField(column_name='@sec.TLS.profile.1.caCert.application1', null=True)
    _sec_tls_profile_1_ca_cert_application2 = TextField(column_name='@sec.TLS.profile.1.caCert.application2', null=True)
    _sec_tls_profile_1_ca_cert_application3 = TextField(column_name='@sec.TLS.profile.1.caCert.application3', null=True)
    _sec_tls_profile_1_ca_cert_application4 = TextField(column_name='@sec.TLS.profile.1.caCert.application4', null=True)
    _sec_tls_profile_1_ca_cert_application5 = TextField(column_name='@sec.TLS.profile.1.caCert.application5', null=True)
    _sec_tls_profile_1_ca_cert_application6 = TextField(column_name='@sec.TLS.profile.1.caCert.application6', null=True)
    _sec_tls_profile_1_ca_cert_application7 = TextField(column_name='@sec.TLS.profile.1.caCert.application7', null=True)
    _sec_tls_profile_1_ca_cert_default_list = TextField(column_name='@sec.TLS.profile.1.caCert.defaultList', null=True)
    _sec_tls_profile_1_ca_cert_platform1 = TextField(column_name='@sec.TLS.profile.1.caCert.platform1', null=True)
    _sec_tls_profile_1_ca_cert_platform2 = TextField(column_name='@sec.TLS.profile.1.caCert.platform2', null=True)
    _sec_tls_profile_1_ca_cert_platform3 = TextField(column_name='@sec.TLS.profile.1.caCert.platform3', null=True)
    _sec_tls_profile_1_cipher_suite = TextField(column_name='@sec.TLS.profile.1.cipherSuite', null=True)
    _sec_tls_profile_1_cipher_suite_default = TextField(column_name='@sec.TLS.profile.1.cipherSuiteDefault', null=True)
    _sec_tls_profile_1_device_cert = TextField(column_name='@sec.TLS.profile.1.deviceCert', null=True)
    _sec_tls_profile_2_ca_cert_application1 = TextField(column_name='@sec.TLS.profile.2.caCert.application1', null=True)
    _sec_tls_profile_2_ca_cert_application2 = TextField(column_name='@sec.TLS.profile.2.caCert.application2', null=True)
    _sec_tls_profile_2_ca_cert_application3 = TextField(column_name='@sec.TLS.profile.2.caCert.application3', null=True)
    _sec_tls_profile_2_ca_cert_application4 = TextField(column_name='@sec.TLS.profile.2.caCert.application4', null=True)
    _sec_tls_profile_2_ca_cert_application5 = TextField(column_name='@sec.TLS.profile.2.caCert.application5', null=True)
    _sec_tls_profile_2_ca_cert_application6 = TextField(column_name='@sec.TLS.profile.2.caCert.application6', null=True)
    _sec_tls_profile_2_ca_cert_application7 = TextField(column_name='@sec.TLS.profile.2.caCert.application7', null=True)
    _sec_tls_profile_2_ca_cert_default_list = TextField(column_name='@sec.TLS.profile.2.caCert.defaultList', null=True)
    _sec_tls_profile_2_ca_cert_platform1 = TextField(column_name='@sec.TLS.profile.2.caCert.platform1', null=True)
    _sec_tls_profile_2_ca_cert_platform2 = TextField(column_name='@sec.TLS.profile.2.caCert.platform2', null=True)
    _sec_tls_profile_2_ca_cert_platform3 = TextField(column_name='@sec.TLS.profile.2.caCert.platform3', null=True)
    _sec_tls_profile_2_cipher_suite = TextField(column_name='@sec.TLS.profile.2.cipherSuite', null=True)
    _sec_tls_profile_2_cipher_suite_default = TextField(column_name='@sec.TLS.profile.2.cipherSuiteDefault', null=True)
    _sec_tls_profile_2_device_cert = TextField(column_name='@sec.TLS.profile.2.deviceCert', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.profile'

class SectlsprofileexchangeServices(BaseModel):
    _sec_tls_profile_exchange_services_cipher_suite_default = TextField(column_name='@sec.TLS.profile.exchangeServices.cipherSuiteDefault', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.profile.exchangeServices'

class SectlsprofilewebServer(BaseModel):
    _sec_tls_profile_web_server_cipher_suite_default = TextField(column_name='@sec.TLS.profile.webServer.cipherSuiteDefault', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.profile.webServer'

class SectlsprofileSelection(BaseModel):
    _sec_tls_profile_selection_ldap = TextField(column_name='@sec.TLS.profileSelection.LDAP', null=True)
    _sec_tls_profile_selection_sip = TextField(column_name='@sec.TLS.profileSelection.SIP', null=True)
    _sec_tls_profile_selection_sopi = TextField(column_name='@sec.TLS.profileSelection.SOPI', null=True)
    _sec_tls_profile_selection_xmpp = TextField(column_name='@sec.TLS.profileSelection.XMPP', null=True)
    _sec_tls_profile_selection_browser = TextField(column_name='@sec.TLS.profileSelection.browser', null=True)
    _sec_tls_profile_selection_syslog = TextField(column_name='@sec.TLS.profileSelection.syslog', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.profileSelection'

class Sectlsprotocol(BaseModel):
    _sec_tls_protocol_browser = TextField(column_name='@sec.TLS.protocol.browser', null=True)
    _sec_tls_protocol_exchange_services = TextField(column_name='@sec.TLS.protocol.exchangeServices', null=True)
    _sec_tls_protocol_ldap = TextField(column_name='@sec.TLS.protocol.ldap', null=True)
    _sec_tls_protocol_sip = TextField(column_name='@sec.TLS.protocol.sip', null=True)
    _sec_tls_protocol_sopi = TextField(column_name='@sec.TLS.protocol.sopi', null=True)
    _sec_tls_protocol_web_server = TextField(column_name='@sec.TLS.protocol.webServer', null=True)
    _sec_tls_protocol_xmpp = TextField(column_name='@sec.TLS.protocol.xmpp', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.protocol'

class Sectlsprov(BaseModel):
    _sec_tls_prov_cipher_list = TextField(column_name='@sec.TLS.prov.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.prov'

class Sectlssyslog(BaseModel):
    _sec_tls_syslog_cipher_list = TextField(column_name='@sec.TLS.syslog.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.syslog'

class SectlswebServer(BaseModel):
    _sec_tls_web_server_cipher_list = TextField(column_name='@sec.TLS.webServer.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.webServer'

class Sectlsxmpp(BaseModel):
    _sec_tls_xmpp_cipher_list = TextField(column_name='@sec.TLS.xmpp.cipherList', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.TLS.xmpp'

class Secdot1Xeapollogoff(BaseModel):
    _sec_dot1x_eapollogoff_enabled = TextField(column_name='@sec.dot1x.eapollogoff.enabled', null=True)
    _sec_dot1x_eapollogoff_lanlinkreset = TextField(column_name='@sec.dot1x.eapollogoff.lanlinkreset', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.dot1x.eapollogoff'

class Secencryptionupload(BaseModel):
    _sec_encryption_upload_call_lists = TextField(column_name='@sec.encryption.upload.callLists', null=True)
    _sec_encryption_upload_config = TextField(column_name='@sec.encryption.upload.config', null=True)
    _sec_encryption_upload_dir = TextField(column_name='@sec.encryption.upload.dir', null=True)
    _sec_encryption_upload_overrides = TextField(column_name='@sec.encryption.upload.overrides', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.encryption.upload'

class SechostMoveDetectcdp(BaseModel):
    _sec_host_move_detect_cdp_enabled = TextField(column_name='@sec.hostMoveDetect.cdp.enabled', null=True)
    _sec_host_move_detect_cdp_sleep_time = TextField(column_name='@sec.hostMoveDetect.cdp.sleepTime', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.hostMoveDetect.cdp'

class Secpwdlength(BaseModel):
    _sec_pwd_length_admin = TextField(column_name='@sec.pwd.length.admin', null=True)
    _sec_pwd_length_user = TextField(column_name='@sec.pwd.length.user', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.pwd.length'

class SecuploadDevice(BaseModel):
    _sec_upload_device_private_key = TextField(column_name='@sec.uploadDevice.privateKey', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'sec.uploadDevice'

class TcpIpAppdhcp(BaseModel):
    _tcp_ip_app_dhcp_release_on_link_recovery = TextField(column_name='@tcpIpApp.dhcp.releaseOnLinkRecovery', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.dhcp'

class TcpIpAppdns(BaseModel):
    _tcp_ip_app_dns_alt_server = TextField(column_name='@tcpIpApp.dns.altServer', null=True)
    _tcp_ip_app_dns_domain = TextField(column_name='@tcpIpApp.dns.domain', null=True)
    _tcp_ip_app_dns_server = TextField(column_name='@tcpIpApp.dns.server', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.dns'

class TcpIpAppdnsaddress(BaseModel):
    _tcp_ip_app_dns_address_override_dhcp = TextField(column_name='@tcpIpApp.dns.address.overrideDHCP', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.dns.address'

class TcpIpAppdnsdomain(BaseModel):
    _tcp_ip_app_dns_domain_override_dhcp = TextField(column_name='@tcpIpApp.dns.domain.overrideDHCP', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.dns.domain'

class TcpIpAppfileTransfer(BaseModel):
    _tcp_ip_app_file_transfer_wait_for_link_if_down = TextField(column_name='@tcpIpApp.fileTransfer.waitForLinkIfDown', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.fileTransfer'

class TcpIpAppkeepaliveaudio(BaseModel):
    _tcp_ip_app_keepalive_audio_enable = TextField(column_name='@tcpIpApp.keepalive.audio.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.keepalive.audio'

class TcpIpAppkeepalivetcp(BaseModel):
    _tcp_ip_app_keepalive_tcp_idle_transmit_interval = TextField(column_name='@tcpIpApp.keepalive.tcp.idleTransmitInterval', null=True)
    _tcp_ip_app_keepalive_tcp_no_response_transmit_interval = TextField(column_name='@tcpIpApp.keepalive.tcp.noResponseTransmitInterval', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.keepalive.tcp'

class TcpIpAppkeepalivetcpsippersistentConnection(BaseModel):
    _tcp_ip_app_keepalive_tcp_sip_persistent_connection_enable = TextField(column_name='@tcpIpApp.keepalive.tcp.sip.persistentConnection.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.keepalive.tcp.sip.persistentConnection'

class TcpIpAppkeepalivetcpsiptls(BaseModel):
    _tcp_ip_app_keepalive_tcp_sip_tls_enable = TextField(column_name='@tcpIpApp.keepalive.tcp.sip.tls.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.keepalive.tcp.sip.tls'

class TcpIpAppkeepalivevideo(BaseModel):
    _tcp_ip_app_keepalive_video_enable = TextField(column_name='@tcpIpApp.keepalive.video.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.keepalive.video'

class TcpIpAppportrtp(BaseModel):
    _tcp_ip_app_port_rtp_filter_by_ip = TextField(column_name='@tcpIpApp.port.rtp.filterByIp', null=True)
    _tcp_ip_app_port_rtp_filter_by_port = TextField(column_name='@tcpIpApp.port.rtp.filterByPort', null=True)
    _tcp_ip_app_port_rtp_force_send = TextField(column_name='@tcpIpApp.port.rtp.forceSend', null=True)
    _tcp_ip_app_port_rtp_media_port_range_end = TextField(column_name='@tcpIpApp.port.rtp.mediaPortRangeEnd', null=True)
    _tcp_ip_app_port_rtp_media_port_range_start = TextField(column_name='@tcpIpApp.port.rtp.mediaPortRangeStart', null=True)
    _tcp_ip_app_port_rtp_video_port_range_end = TextField(column_name='@tcpIpApp.port.rtp.videoPortRangeEnd', null=True)
    _tcp_ip_app_port_rtp_video_port_range_start = TextField(column_name='@tcpIpApp.port.rtp.videoPortRangeStart', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.port.rtp'

class TcpIpAppportrtplync(BaseModel):
    _tcp_ip_app_port_rtp_lync_audio_port_range_end = TextField(column_name='@tcpIpApp.port.rtp.lync.audioPortRangeEnd', null=True)
    _tcp_ip_app_port_rtp_lync_audio_port_range_start = TextField(column_name='@tcpIpApp.port.rtp.lync.audioPortRangeStart', null=True)
    _tcp_ip_app_port_rtp_lync_video_port_range_end = TextField(column_name='@tcpIpApp.port.rtp.lync.videoPortRangeEnd', null=True)
    _tcp_ip_app_port_rtp_lync_video_port_range_start = TextField(column_name='@tcpIpApp.port.rtp.lync.videoPortRangeStart', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.port.rtp.lync'

class TcpIpAppportrtpvideoPortRange(BaseModel):
    _tcp_ip_app_port_rtp_video_port_range_enable = TextField(column_name='@tcpIpApp.port.rtp.videoPortRange.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.port.rtp.videoPortRange'

class TcpIpAppsntp(BaseModel):
    _tcp_ip_app_sntp_a_query = TextField(column_name='@tcpIpApp.sntp.AQuery', null=True)
    _tcp_ip_app_sntp_address = TextField(column_name='@tcpIpApp.sntp.address', null=True)
    _tcp_ip_app_sntp_gmt_offset = TextField(column_name='@tcpIpApp.sntp.gmtOffset', null=True)
    _tcp_ip_app_sntp_gmt_offsetcity_id = TextField(column_name='@tcpIpApp.sntp.gmtOffsetcityID', null=True)
    _tcp_ip_app_sntp_resync_period = TextField(column_name='@tcpIpApp.sntp.resyncPeriod', null=True)
    _tcp_ip_app_sntp_retry_dns_period = TextField(column_name='@tcpIpApp.sntp.retryDnsPeriod', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp'

class TcpIpAppsntpaddress(BaseModel):
    _tcp_ip_app_sntp_address_override_dhcp = TextField(column_name='@tcpIpApp.sntp.address.overrideDHCP', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.address'

class TcpIpAppsntpdaylightSavings(BaseModel):
    _tcp_ip_app_sntp_daylight_savings_enable = TextField(column_name='@tcpIpApp.sntp.daylightSavings.enable', null=True)
    _tcp_ip_app_sntp_daylight_savings_fixed_day_enable = TextField(column_name='@tcpIpApp.sntp.daylightSavings.fixedDayEnable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.daylightSavings'

class TcpIpAppsntpdaylightSavingsstart(BaseModel):
    _tcp_ip_app_sntp_daylight_savings_start_date = TextField(column_name='@tcpIpApp.sntp.daylightSavings.start.date', null=True)
    _tcp_ip_app_sntp_daylight_savings_start_day_of_week = TextField(column_name='@tcpIpApp.sntp.daylightSavings.start.dayOfWeek', null=True)
    _tcp_ip_app_sntp_daylight_savings_start_month = TextField(column_name='@tcpIpApp.sntp.daylightSavings.start.month', null=True)
    _tcp_ip_app_sntp_daylight_savings_start_time = TextField(column_name='@tcpIpApp.sntp.daylightSavings.start.time', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.daylightSavings.start'

class TcpIpAppsntpdaylightSavingsstartdayOfWeek(BaseModel):
    _tcp_ip_app_sntp_daylight_savings_start_day_of_week_last_in_month = TextField(column_name='@tcpIpApp.sntp.daylightSavings.start.dayOfWeek.lastInMonth', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.daylightSavings.start.dayOfWeek'

class TcpIpAppsntpdaylightSavingsstop(BaseModel):
    _tcp_ip_app_sntp_daylight_savings_stop_date = TextField(column_name='@tcpIpApp.sntp.daylightSavings.stop.date', null=True)
    _tcp_ip_app_sntp_daylight_savings_stop_day_of_week = TextField(column_name='@tcpIpApp.sntp.daylightSavings.stop.dayOfWeek', null=True)
    _tcp_ip_app_sntp_daylight_savings_stop_month = TextField(column_name='@tcpIpApp.sntp.daylightSavings.stop.month', null=True)
    _tcp_ip_app_sntp_daylight_savings_stop_time = TextField(column_name='@tcpIpApp.sntp.daylightSavings.stop.time', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.daylightSavings.stop'

class TcpIpAppsntpdaylightSavingsstopdayOfWeek(BaseModel):
    _tcp_ip_app_sntp_daylight_savings_stop_day_of_week_last_in_month = TextField(column_name='@tcpIpApp.sntp.daylightSavings.stop.dayOfWeek.lastInMonth', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.daylightSavings.stop.dayOfWeek'

class TcpIpAppsntpgmtOffset(BaseModel):
    _tcp_ip_app_sntp_gmt_offset_override_dhcp = TextField(column_name='@tcpIpApp.sntp.gmtOffset.overrideDHCP', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tcpIpApp.sntp.gmtOffset'

class TonechordcallProgspare1(BaseModel):
    _tone_chord_call_prog_spare1_off_dur = TextField(column_name='@tone.chord.callProg.spare1.offDur', null=True)
    _tone_chord_call_prog_spare1_on_dur = TextField(column_name='@tone.chord.callProg.spare1.onDur', null=True)
    _tone_chord_call_prog_spare1_repeat = TextField(column_name='@tone.chord.callProg.spare1.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare1'

class TonechordcallProgspare1Freq(BaseModel):
    _tone_chord_call_prog_spare1_freq_1 = TextField(column_name='@tone.chord.callProg.spare1.freq.1', null=True)
    _tone_chord_call_prog_spare1_freq_2 = TextField(column_name='@tone.chord.callProg.spare1.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare1.freq'

class TonechordcallProgspare1Level(BaseModel):
    _tone_chord_call_prog_spare1_level_1 = TextField(column_name='@tone.chord.callProg.spare1.level.1', null=True)
    _tone_chord_call_prog_spare1_level_2 = TextField(column_name='@tone.chord.callProg.spare1.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare1.level'

class TonechordcallProgspare2(BaseModel):
    _tone_chord_call_prog_spare2_off_dur = TextField(column_name='@tone.chord.callProg.spare2.offDur', null=True)
    _tone_chord_call_prog_spare2_on_dur = TextField(column_name='@tone.chord.callProg.spare2.onDur', null=True)
    _tone_chord_call_prog_spare2_repeat = TextField(column_name='@tone.chord.callProg.spare2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare2'

class TonechordcallProgspare2Freq(BaseModel):
    _tone_chord_call_prog_spare2_freq_1 = TextField(column_name='@tone.chord.callProg.spare2.freq.1', null=True)
    _tone_chord_call_prog_spare2_freq_2 = TextField(column_name='@tone.chord.callProg.spare2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare2.freq'

class TonechordcallProgspare2Level(BaseModel):
    _tone_chord_call_prog_spare2_level_1 = TextField(column_name='@tone.chord.callProg.spare2.level.1', null=True)
    _tone_chord_call_prog_spare2_level_2 = TextField(column_name='@tone.chord.callProg.spare2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare2.level'

class TonechordcallProgspare3(BaseModel):
    _tone_chord_call_prog_spare3_off_dur = TextField(column_name='@tone.chord.callProg.spare3.offDur', null=True)
    _tone_chord_call_prog_spare3_on_dur = TextField(column_name='@tone.chord.callProg.spare3.onDur', null=True)
    _tone_chord_call_prog_spare3_repeat = TextField(column_name='@tone.chord.callProg.spare3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare3'

class TonechordcallProgspare3Freq(BaseModel):
    _tone_chord_call_prog_spare3_freq_1 = TextField(column_name='@tone.chord.callProg.spare3.freq.1', null=True)
    _tone_chord_call_prog_spare3_freq_2 = TextField(column_name='@tone.chord.callProg.spare3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare3.freq'

class TonechordcallProgspare3Level(BaseModel):
    _tone_chord_call_prog_spare3_level_1 = TextField(column_name='@tone.chord.callProg.spare3.level.1', null=True)
    _tone_chord_call_prog_spare3_level_2 = TextField(column_name='@tone.chord.callProg.spare3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare3.level'

class TonechordcallProgspare4(BaseModel):
    _tone_chord_call_prog_spare4_off_dur = TextField(column_name='@tone.chord.callProg.spare4.offDur', null=True)
    _tone_chord_call_prog_spare4_on_dur = TextField(column_name='@tone.chord.callProg.spare4.onDur', null=True)
    _tone_chord_call_prog_spare4_repeat = TextField(column_name='@tone.chord.callProg.spare4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare4'

class TonechordcallProgspare4Freq(BaseModel):
    _tone_chord_call_prog_spare4_freq_1 = TextField(column_name='@tone.chord.callProg.spare4.freq.1', null=True)
    _tone_chord_call_prog_spare4_freq_2 = TextField(column_name='@tone.chord.callProg.spare4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare4.freq'

class TonechordcallProgspare4Level(BaseModel):
    _tone_chord_call_prog_spare4_level_1 = TextField(column_name='@tone.chord.callProg.spare4.level.1', null=True)
    _tone_chord_call_prog_spare4_level_2 = TextField(column_name='@tone.chord.callProg.spare4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare4.level'

class TonechordcallProgspare5(BaseModel):
    _tone_chord_call_prog_spare5_off_dur = TextField(column_name='@tone.chord.callProg.spare5.offDur', null=True)
    _tone_chord_call_prog_spare5_on_dur = TextField(column_name='@tone.chord.callProg.spare5.onDur', null=True)
    _tone_chord_call_prog_spare5_repeat = TextField(column_name='@tone.chord.callProg.spare5.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare5'

class TonechordcallProgspare5Freq(BaseModel):
    _tone_chord_call_prog_spare5_freq_1 = TextField(column_name='@tone.chord.callProg.spare5.freq.1', null=True)
    _tone_chord_call_prog_spare5_freq_2 = TextField(column_name='@tone.chord.callProg.spare5.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare5.freq'

class TonechordcallProgspare5Level(BaseModel):
    _tone_chord_call_prog_spare5_level_1 = TextField(column_name='@tone.chord.callProg.spare5.level.1', null=True)
    _tone_chord_call_prog_spare5_level_2 = TextField(column_name='@tone.chord.callProg.spare5.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare5.level'

class TonechordcallProgspare6(BaseModel):
    _tone_chord_call_prog_spare6_off_dur = TextField(column_name='@tone.chord.callProg.spare6.offDur', null=True)
    _tone_chord_call_prog_spare6_on_dur = TextField(column_name='@tone.chord.callProg.spare6.onDur', null=True)
    _tone_chord_call_prog_spare6_repeat = TextField(column_name='@tone.chord.callProg.spare6.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare6'

class TonechordcallProgspare6Freq(BaseModel):
    _tone_chord_call_prog_spare6_freq_1 = TextField(column_name='@tone.chord.callProg.spare6.freq.1', null=True)
    _tone_chord_call_prog_spare6_freq_2 = TextField(column_name='@tone.chord.callProg.spare6.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare6.freq'

class TonechordcallProgspare6Level(BaseModel):
    _tone_chord_call_prog_spare6_level_1 = TextField(column_name='@tone.chord.callProg.spare6.level.1', null=True)
    _tone_chord_call_prog_spare6_level_2 = TextField(column_name='@tone.chord.callProg.spare6.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.callProg.spare6.level'

class TonechordmiscDb3Major(BaseModel):
    _tone_chord_misc__db3_major_off_dur = TextField(column_name='@tone.chord.misc.Db3Major.offDur', null=True)
    _tone_chord_misc__db3_major_on_dur = TextField(column_name='@tone.chord.misc.Db3Major.onDur', null=True)
    _tone_chord_misc__db3_major_repeat = TextField(column_name='@tone.chord.misc.Db3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.Db3Major'

class TonechordmiscDb3Majorfreq(BaseModel):
    _tone_chord_misc__db3_major_freq_1 = TextField(column_name='@tone.chord.misc.Db3Major.freq.1', null=True)
    _tone_chord_misc__db3_major_freq_2 = TextField(column_name='@tone.chord.misc.Db3Major.freq.2', null=True)
    _tone_chord_misc__db3_major_freq_3 = TextField(column_name='@tone.chord.misc.Db3Major.freq.3', null=True)
    _tone_chord_misc__db3_major_freq_4 = TextField(column_name='@tone.chord.misc.Db3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.Db3Major.freq'

class TonechordmiscDb3Majorlevel(BaseModel):
    _tone_chord_misc__db3_major_level_1 = TextField(column_name='@tone.chord.misc.Db3Major.level.1', null=True)
    _tone_chord_misc__db3_major_level_2 = TextField(column_name='@tone.chord.misc.Db3Major.level.2', null=True)
    _tone_chord_misc__db3_major_level_3 = TextField(column_name='@tone.chord.misc.Db3Major.level.3', null=True)
    _tone_chord_misc__db3_major_level_4 = TextField(column_name='@tone.chord.misc.Db3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.Db3Major.level'

class Tonechordmisce3Major(BaseModel):
    _tone_chord_misc_e3_major_off_dur = TextField(column_name='@tone.chord.misc.E3Major.offDur', null=True)
    _tone_chord_misc_e3_major_on_dur = TextField(column_name='@tone.chord.misc.E3Major.onDur', null=True)
    _tone_chord_misc_e3_major_repeat = TextField(column_name='@tone.chord.misc.E3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.E3Major'

class Tonechordmisce3Majorfreq(BaseModel):
    _tone_chord_misc_e3_major_freq_1 = TextField(column_name='@tone.chord.misc.E3Major.freq.1', null=True)
    _tone_chord_misc_e3_major_freq_2 = TextField(column_name='@tone.chord.misc.E3Major.freq.2', null=True)
    _tone_chord_misc_e3_major_freq_3 = TextField(column_name='@tone.chord.misc.E3Major.freq.3', null=True)
    _tone_chord_misc_e3_major_freq_4 = TextField(column_name='@tone.chord.misc.E3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.E3Major.freq'

class Tonechordmisce3Majorlevel(BaseModel):
    _tone_chord_misc_e3_major_level_1 = TextField(column_name='@tone.chord.misc.E3Major.level.1', null=True)
    _tone_chord_misc_e3_major_level_2 = TextField(column_name='@tone.chord.misc.E3Major.level.2', null=True)
    _tone_chord_misc_e3_major_level_3 = TextField(column_name='@tone.chord.misc.E3Major.level.3', null=True)
    _tone_chord_misc_e3_major_level_4 = TextField(column_name='@tone.chord.misc.E3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.E3Major.level'

class Tonechordmiscspare1(BaseModel):
    _tone_chord_misc_spare1_off_dur = TextField(column_name='@tone.chord.misc.spare1.offDur', null=True)
    _tone_chord_misc_spare1_on_dur = TextField(column_name='@tone.chord.misc.spare1.onDur', null=True)
    _tone_chord_misc_spare1_repeat = TextField(column_name='@tone.chord.misc.spare1.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare1'

class Tonechordmiscspare1Freq(BaseModel):
    _tone_chord_misc_spare1_freq_1 = TextField(column_name='@tone.chord.misc.spare1.freq.1', null=True)
    _tone_chord_misc_spare1_freq_2 = TextField(column_name='@tone.chord.misc.spare1.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare1.freq'

class Tonechordmiscspare1Level(BaseModel):
    _tone_chord_misc_spare1_level_1 = TextField(column_name='@tone.chord.misc.spare1.level.1', null=True)
    _tone_chord_misc_spare1_level_2 = TextField(column_name='@tone.chord.misc.spare1.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare1.level'

class Tonechordmiscspare2(BaseModel):
    _tone_chord_misc_spare2_off_dur = TextField(column_name='@tone.chord.misc.spare2.offDur', null=True)
    _tone_chord_misc_spare2_on_dur = TextField(column_name='@tone.chord.misc.spare2.onDur', null=True)
    _tone_chord_misc_spare2_repeat = TextField(column_name='@tone.chord.misc.spare2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare2'

class Tonechordmiscspare2Freq(BaseModel):
    _tone_chord_misc_spare2_freq_1 = TextField(column_name='@tone.chord.misc.spare2.freq.1', null=True)
    _tone_chord_misc_spare2_freq_2 = TextField(column_name='@tone.chord.misc.spare2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare2.freq'

class Tonechordmiscspare2Level(BaseModel):
    _tone_chord_misc_spare2_level_1 = TextField(column_name='@tone.chord.misc.spare2.level.1', null=True)
    _tone_chord_misc_spare2_level_2 = TextField(column_name='@tone.chord.misc.spare2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare2.level'

class Tonechordmiscspare3(BaseModel):
    _tone_chord_misc_spare3_off_dur = TextField(column_name='@tone.chord.misc.spare3.offDur', null=True)
    _tone_chord_misc_spare3_on_dur = TextField(column_name='@tone.chord.misc.spare3.onDur', null=True)
    _tone_chord_misc_spare3_repeat = TextField(column_name='@tone.chord.misc.spare3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare3'

class Tonechordmiscspare3Freq(BaseModel):
    _tone_chord_misc_spare3_freq_1 = TextField(column_name='@tone.chord.misc.spare3.freq.1', null=True)
    _tone_chord_misc_spare3_freq_2 = TextField(column_name='@tone.chord.misc.spare3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare3.freq'

class Tonechordmiscspare3Level(BaseModel):
    _tone_chord_misc_spare3_level_1 = TextField(column_name='@tone.chord.misc.spare3.level.1', null=True)
    _tone_chord_misc_spare3_level_2 = TextField(column_name='@tone.chord.misc.spare3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare3.level'

class Tonechordmiscspare4(BaseModel):
    _tone_chord_misc_spare4_off_dur = TextField(column_name='@tone.chord.misc.spare4.offDur', null=True)
    _tone_chord_misc_spare4_on_dur = TextField(column_name='@tone.chord.misc.spare4.onDur', null=True)
    _tone_chord_misc_spare4_repeat = TextField(column_name='@tone.chord.misc.spare4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare4'

class Tonechordmiscspare4Freq(BaseModel):
    _tone_chord_misc_spare4_freq_1 = TextField(column_name='@tone.chord.misc.spare4.freq.1', null=True)
    _tone_chord_misc_spare4_freq_2 = TextField(column_name='@tone.chord.misc.spare4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare4.freq'

class Tonechordmiscspare4Level(BaseModel):
    _tone_chord_misc_spare4_level_1 = TextField(column_name='@tone.chord.misc.spare4.level.1', null=True)
    _tone_chord_misc_spare4_level_2 = TextField(column_name='@tone.chord.misc.spare4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare4.level'

class Tonechordmiscspare5(BaseModel):
    _tone_chord_misc_spare5_off_dur = TextField(column_name='@tone.chord.misc.spare5.offDur', null=True)
    _tone_chord_misc_spare5_on_dur = TextField(column_name='@tone.chord.misc.spare5.onDur', null=True)
    _tone_chord_misc_spare5_repeat = TextField(column_name='@tone.chord.misc.spare5.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare5'

class Tonechordmiscspare5Freq(BaseModel):
    _tone_chord_misc_spare5_freq_1 = TextField(column_name='@tone.chord.misc.spare5.freq.1', null=True)
    _tone_chord_misc_spare5_freq_2 = TextField(column_name='@tone.chord.misc.spare5.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare5.freq'

class Tonechordmiscspare5Level(BaseModel):
    _tone_chord_misc_spare5_level_1 = TextField(column_name='@tone.chord.misc.spare5.level.1', null=True)
    _tone_chord_misc_spare5_level_2 = TextField(column_name='@tone.chord.misc.spare5.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare5.level'

class Tonechordmiscspare6(BaseModel):
    _tone_chord_misc_spare6_off_dur = TextField(column_name='@tone.chord.misc.spare6.offDur', null=True)
    _tone_chord_misc_spare6_on_dur = TextField(column_name='@tone.chord.misc.spare6.onDur', null=True)
    _tone_chord_misc_spare6_repeat = TextField(column_name='@tone.chord.misc.spare6.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare6'

class Tonechordmiscspare6Freq(BaseModel):
    _tone_chord_misc_spare6_freq_1 = TextField(column_name='@tone.chord.misc.spare6.freq.1', null=True)
    _tone_chord_misc_spare6_freq_2 = TextField(column_name='@tone.chord.misc.spare6.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare6.freq'

class Tonechordmiscspare6Level(BaseModel):
    _tone_chord_misc_spare6_level_1 = TextField(column_name='@tone.chord.misc.spare6.level.1', null=True)
    _tone_chord_misc_spare6_level_2 = TextField(column_name='@tone.chord.misc.spare6.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare6.level'

class Tonechordmiscspare7(BaseModel):
    _tone_chord_misc_spare7_off_dur = TextField(column_name='@tone.chord.misc.spare7.offDur', null=True)
    _tone_chord_misc_spare7_on_dur = TextField(column_name='@tone.chord.misc.spare7.onDur', null=True)
    _tone_chord_misc_spare7_repeat = TextField(column_name='@tone.chord.misc.spare7.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare7'

class Tonechordmiscspare7Freq(BaseModel):
    _tone_chord_misc_spare7_freq_1 = TextField(column_name='@tone.chord.misc.spare7.freq.1', null=True)
    _tone_chord_misc_spare7_freq_2 = TextField(column_name='@tone.chord.misc.spare7.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare7.freq'

class Tonechordmiscspare7Level(BaseModel):
    _tone_chord_misc_spare7_level_1 = TextField(column_name='@tone.chord.misc.spare7.level.1', null=True)
    _tone_chord_misc_spare7_level_2 = TextField(column_name='@tone.chord.misc.spare7.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare7.level'

class Tonechordmiscspare8(BaseModel):
    _tone_chord_misc_spare8_off_dur = TextField(column_name='@tone.chord.misc.spare8.offDur', null=True)
    _tone_chord_misc_spare8_on_dur = TextField(column_name='@tone.chord.misc.spare8.onDur', null=True)
    _tone_chord_misc_spare8_repeat = TextField(column_name='@tone.chord.misc.spare8.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare8'

class Tonechordmiscspare8Freq(BaseModel):
    _tone_chord_misc_spare8_freq_1 = TextField(column_name='@tone.chord.misc.spare8.freq.1', null=True)
    _tone_chord_misc_spare8_freq_2 = TextField(column_name='@tone.chord.misc.spare8.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare8.freq'

class Tonechordmiscspare8Level(BaseModel):
    _tone_chord_misc_spare8_level_1 = TextField(column_name='@tone.chord.misc.spare8.level.1', null=True)
    _tone_chord_misc_spare8_level_2 = TextField(column_name='@tone.chord.misc.spare8.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare8.level'

class Tonechordmiscspare9(BaseModel):
    _tone_chord_misc_spare9_off_dur = TextField(column_name='@tone.chord.misc.spare9.offDur', null=True)
    _tone_chord_misc_spare9_on_dur = TextField(column_name='@tone.chord.misc.spare9.onDur', null=True)
    _tone_chord_misc_spare9_repeat = TextField(column_name='@tone.chord.misc.spare9.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare9'

class Tonechordmiscspare9Freq(BaseModel):
    _tone_chord_misc_spare9_freq_1 = TextField(column_name='@tone.chord.misc.spare9.freq.1', null=True)
    _tone_chord_misc_spare9_freq_2 = TextField(column_name='@tone.chord.misc.spare9.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare9.freq'

class Tonechordmiscspare9Level(BaseModel):
    _tone_chord_misc_spare9_level_1 = TextField(column_name='@tone.chord.misc.spare9.level.1', null=True)
    _tone_chord_misc_spare9_level_2 = TextField(column_name='@tone.chord.misc.spare9.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.misc.spare9.level'

class Tonechordringera3(BaseModel):
    _tone_chord_ringer_a3_off_dur = TextField(column_name='@tone.chord.ringer.A3.offDur', null=True)
    _tone_chord_ringer_a3_on_dur = TextField(column_name='@tone.chord.ringer.A3.onDur', null=True)
    _tone_chord_ringer_a3_repeat = TextField(column_name='@tone.chord.ringer.A3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3'

class Tonechordringera3Freq(BaseModel):
    _tone_chord_ringer_a3_freq_1 = TextField(column_name='@tone.chord.ringer.A3.freq.1', null=True)
    _tone_chord_ringer_a3_freq_2 = TextField(column_name='@tone.chord.ringer.A3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3.freq'

class Tonechordringera3Level(BaseModel):
    _tone_chord_ringer_a3_level_1 = TextField(column_name='@tone.chord.ringer.A3.level.1', null=True)
    _tone_chord_ringer_a3_level_2 = TextField(column_name='@tone.chord.ringer.A3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3.level'

class Tonechordringera3Major(BaseModel):
    _tone_chord_ringer_a3_major_off_dur = TextField(column_name='@tone.chord.ringer.A3Major.offDur', null=True)
    _tone_chord_ringer_a3_major_on_dur = TextField(column_name='@tone.chord.ringer.A3Major.onDur', null=True)
    _tone_chord_ringer_a3_major_repeat = TextField(column_name='@tone.chord.ringer.A3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3Major'

class Tonechordringera3Majorfreq(BaseModel):
    _tone_chord_ringer_a3_major_freq_1 = TextField(column_name='@tone.chord.ringer.A3Major.freq.1', null=True)
    _tone_chord_ringer_a3_major_freq_2 = TextField(column_name='@tone.chord.ringer.A3Major.freq.2', null=True)
    _tone_chord_ringer_a3_major_freq_3 = TextField(column_name='@tone.chord.ringer.A3Major.freq.3', null=True)
    _tone_chord_ringer_a3_major_freq_4 = TextField(column_name='@tone.chord.ringer.A3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3Major.freq'

class Tonechordringera3Majorlevel(BaseModel):
    _tone_chord_ringer_a3_major_level_1 = TextField(column_name='@tone.chord.ringer.A3Major.level.1', null=True)
    _tone_chord_ringer_a3_major_level_2 = TextField(column_name='@tone.chord.ringer.A3Major.level.2', null=True)
    _tone_chord_ringer_a3_major_level_3 = TextField(column_name='@tone.chord.ringer.A3Major.level.3', null=True)
    _tone_chord_ringer_a3_major_level_4 = TextField(column_name='@tone.chord.ringer.A3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A3Major.level'

class Tonechordringera4(BaseModel):
    _tone_chord_ringer_a4_off_dur = TextField(column_name='@tone.chord.ringer.A4.offDur', null=True)
    _tone_chord_ringer_a4_on_dur = TextField(column_name='@tone.chord.ringer.A4.onDur', null=True)
    _tone_chord_ringer_a4_repeat = TextField(column_name='@tone.chord.ringer.A4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4'

class Tonechordringera4Freq(BaseModel):
    _tone_chord_ringer_a4_freq_1 = TextField(column_name='@tone.chord.ringer.A4.freq.1', null=True)
    _tone_chord_ringer_a4_freq_2 = TextField(column_name='@tone.chord.ringer.A4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4.freq'

class Tonechordringera4Level(BaseModel):
    _tone_chord_ringer_a4_level_1 = TextField(column_name='@tone.chord.ringer.A4.level.1', null=True)
    _tone_chord_ringer_a4_level_2 = TextField(column_name='@tone.chord.ringer.A4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4.level'

class Tonechordringera4Major(BaseModel):
    _tone_chord_ringer_a4_major_off_dur = TextField(column_name='@tone.chord.ringer.A4Major.offDur', null=True)
    _tone_chord_ringer_a4_major_on_dur = TextField(column_name='@tone.chord.ringer.A4Major.onDur', null=True)
    _tone_chord_ringer_a4_major_repeat = TextField(column_name='@tone.chord.ringer.A4Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4Major'

class Tonechordringera4Majorfreq(BaseModel):
    _tone_chord_ringer_a4_major_freq_1 = TextField(column_name='@tone.chord.ringer.A4Major.freq.1', null=True)
    _tone_chord_ringer_a4_major_freq_2 = TextField(column_name='@tone.chord.ringer.A4Major.freq.2', null=True)
    _tone_chord_ringer_a4_major_freq_3 = TextField(column_name='@tone.chord.ringer.A4Major.freq.3', null=True)
    _tone_chord_ringer_a4_major_freq_4 = TextField(column_name='@tone.chord.ringer.A4Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4Major.freq'

class Tonechordringera4Majorlevel(BaseModel):
    _tone_chord_ringer_a4_major_level_1 = TextField(column_name='@tone.chord.ringer.A4Major.level.1', null=True)
    _tone_chord_ringer_a4_major_level_2 = TextField(column_name='@tone.chord.ringer.A4Major.level.2', null=True)
    _tone_chord_ringer_a4_major_level_3 = TextField(column_name='@tone.chord.ringer.A4Major.level.3', null=True)
    _tone_chord_ringer_a4_major_level_4 = TextField(column_name='@tone.chord.ringer.A4Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.A4Major.level'

class TonechordringerAb2(BaseModel):
    _tone_chord_ringer__ab2_off_dur = TextField(column_name='@tone.chord.ringer.Ab2.offDur', null=True)
    _tone_chord_ringer__ab2_on_dur = TextField(column_name='@tone.chord.ringer.Ab2.onDur', null=True)
    _tone_chord_ringer__ab2_repeat = TextField(column_name='@tone.chord.ringer.Ab2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab2'

class TonechordringerAb2Freq(BaseModel):
    _tone_chord_ringer__ab2_freq_1 = TextField(column_name='@tone.chord.ringer.Ab2.freq.1', null=True)
    _tone_chord_ringer__ab2_freq_2 = TextField(column_name='@tone.chord.ringer.Ab2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab2.freq'

class TonechordringerAb2Level(BaseModel):
    _tone_chord_ringer__ab2_level_1 = TextField(column_name='@tone.chord.ringer.Ab2.level.1', null=True)
    _tone_chord_ringer__ab2_level_2 = TextField(column_name='@tone.chord.ringer.Ab2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab2.level'

class TonechordringerAb3(BaseModel):
    _tone_chord_ringer__ab3_off_dur = TextField(column_name='@tone.chord.ringer.Ab3.offDur', null=True)
    _tone_chord_ringer__ab3_on_dur = TextField(column_name='@tone.chord.ringer.Ab3.onDur', null=True)
    _tone_chord_ringer__ab3_repeat = TextField(column_name='@tone.chord.ringer.Ab3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3'

class TonechordringerAb3Freq(BaseModel):
    _tone_chord_ringer__ab3_freq_1 = TextField(column_name='@tone.chord.ringer.Ab3.freq.1', null=True)
    _tone_chord_ringer__ab3_freq_2 = TextField(column_name='@tone.chord.ringer.Ab3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3.freq'

class TonechordringerAb3Level(BaseModel):
    _tone_chord_ringer__ab3_level_1 = TextField(column_name='@tone.chord.ringer.Ab3.level.1', null=True)
    _tone_chord_ringer__ab3_level_2 = TextField(column_name='@tone.chord.ringer.Ab3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3.level'

class TonechordringerAb3Major(BaseModel):
    _tone_chord_ringer__ab3_major_off_dur = TextField(column_name='@tone.chord.ringer.Ab3Major.offDur', null=True)
    _tone_chord_ringer__ab3_major_on_dur = TextField(column_name='@tone.chord.ringer.Ab3Major.onDur', null=True)
    _tone_chord_ringer__ab3_major_repeat = TextField(column_name='@tone.chord.ringer.Ab3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3Major'

class TonechordringerAb3Majorfreq(BaseModel):
    _tone_chord_ringer__ab3_major_freq_1 = TextField(column_name='@tone.chord.ringer.Ab3Major.freq.1', null=True)
    _tone_chord_ringer__ab3_major_freq_2 = TextField(column_name='@tone.chord.ringer.Ab3Major.freq.2', null=True)
    _tone_chord_ringer__ab3_major_freq_3 = TextField(column_name='@tone.chord.ringer.Ab3Major.freq.3', null=True)
    _tone_chord_ringer__ab3_major_freq_4 = TextField(column_name='@tone.chord.ringer.Ab3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3Major.freq'

class TonechordringerAb3Majorlevel(BaseModel):
    _tone_chord_ringer__ab3_major_level_1 = TextField(column_name='@tone.chord.ringer.Ab3Major.level.1', null=True)
    _tone_chord_ringer__ab3_major_level_2 = TextField(column_name='@tone.chord.ringer.Ab3Major.level.2', null=True)
    _tone_chord_ringer__ab3_major_level_3 = TextField(column_name='@tone.chord.ringer.Ab3Major.level.3', null=True)
    _tone_chord_ringer__ab3_major_level_4 = TextField(column_name='@tone.chord.ringer.Ab3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Ab3Major.level'

class Tonechordringerb3(BaseModel):
    _tone_chord_ringer_b3_off_dur = TextField(column_name='@tone.chord.ringer.B3.offDur', null=True)
    _tone_chord_ringer_b3_on_dur = TextField(column_name='@tone.chord.ringer.B3.onDur', null=True)
    _tone_chord_ringer_b3_repeat = TextField(column_name='@tone.chord.ringer.B3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3'

class Tonechordringerb3Freq(BaseModel):
    _tone_chord_ringer_b3_freq_1 = TextField(column_name='@tone.chord.ringer.B3.freq.1', null=True)
    _tone_chord_ringer_b3_freq_2 = TextField(column_name='@tone.chord.ringer.B3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3.freq'

class Tonechordringerb3Level(BaseModel):
    _tone_chord_ringer_b3_level_1 = TextField(column_name='@tone.chord.ringer.B3.level.1', null=True)
    _tone_chord_ringer_b3_level_2 = TextField(column_name='@tone.chord.ringer.B3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3.level'

class Tonechordringerb3Major(BaseModel):
    _tone_chord_ringer_b3_major_off_dur = TextField(column_name='@tone.chord.ringer.B3Major.offDur', null=True)
    _tone_chord_ringer_b3_major_on_dur = TextField(column_name='@tone.chord.ringer.B3Major.onDur', null=True)
    _tone_chord_ringer_b3_major_repeat = TextField(column_name='@tone.chord.ringer.B3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3Major'

class Tonechordringerb3Majorfreq(BaseModel):
    _tone_chord_ringer_b3_major_freq_1 = TextField(column_name='@tone.chord.ringer.B3Major.freq.1', null=True)
    _tone_chord_ringer_b3_major_freq_2 = TextField(column_name='@tone.chord.ringer.B3Major.freq.2', null=True)
    _tone_chord_ringer_b3_major_freq_3 = TextField(column_name='@tone.chord.ringer.B3Major.freq.3', null=True)
    _tone_chord_ringer_b3_major_freq_4 = TextField(column_name='@tone.chord.ringer.B3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3Major.freq'

class Tonechordringerb3Majorlevel(BaseModel):
    _tone_chord_ringer_b3_major_level_1 = TextField(column_name='@tone.chord.ringer.B3Major.level.1', null=True)
    _tone_chord_ringer_b3_major_level_2 = TextField(column_name='@tone.chord.ringer.B3Major.level.2', null=True)
    _tone_chord_ringer_b3_major_level_3 = TextField(column_name='@tone.chord.ringer.B3Major.level.3', null=True)
    _tone_chord_ringer_b3_major_level_4 = TextField(column_name='@tone.chord.ringer.B3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B3Major.level'

class Tonechordringerb4(BaseModel):
    _tone_chord_ringer_b4_off_dur = TextField(column_name='@tone.chord.ringer.B4.offDur', null=True)
    _tone_chord_ringer_b4_on_dur = TextField(column_name='@tone.chord.ringer.B4.onDur', null=True)
    _tone_chord_ringer_b4_repeat = TextField(column_name='@tone.chord.ringer.B4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B4'

class Tonechordringerb4Freq(BaseModel):
    _tone_chord_ringer_b4_freq_1 = TextField(column_name='@tone.chord.ringer.B4.freq.1', null=True)
    _tone_chord_ringer_b4_freq_2 = TextField(column_name='@tone.chord.ringer.B4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B4.freq'

class Tonechordringerb4Level(BaseModel):
    _tone_chord_ringer_b4_level_1 = TextField(column_name='@tone.chord.ringer.B4.level.1', null=True)
    _tone_chord_ringer_b4_level_2 = TextField(column_name='@tone.chord.ringer.B4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.B4.level'

class TonechordringerBb3(BaseModel):
    _tone_chord_ringer__bb3_off_dur = TextField(column_name='@tone.chord.ringer.Bb3.offDur', null=True)
    _tone_chord_ringer__bb3_on_dur = TextField(column_name='@tone.chord.ringer.Bb3.onDur', null=True)
    _tone_chord_ringer__bb3_repeat = TextField(column_name='@tone.chord.ringer.Bb3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3'

class TonechordringerBb3Freq(BaseModel):
    _tone_chord_ringer__bb3_freq_1 = TextField(column_name='@tone.chord.ringer.Bb3.freq.1', null=True)
    _tone_chord_ringer__bb3_freq_2 = TextField(column_name='@tone.chord.ringer.Bb3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3.freq'

class TonechordringerBb3Level(BaseModel):
    _tone_chord_ringer__bb3_level_1 = TextField(column_name='@tone.chord.ringer.Bb3.level.1', null=True)
    _tone_chord_ringer__bb3_level_2 = TextField(column_name='@tone.chord.ringer.Bb3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3.level'

class TonechordringerBb3Major(BaseModel):
    _tone_chord_ringer__bb3_major_off_dur = TextField(column_name='@tone.chord.ringer.Bb3Major.offDur', null=True)
    _tone_chord_ringer__bb3_major_on_dur = TextField(column_name='@tone.chord.ringer.Bb3Major.onDur', null=True)
    _tone_chord_ringer__bb3_major_repeat = TextField(column_name='@tone.chord.ringer.Bb3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3Major'

class TonechordringerBb3Majorfreq(BaseModel):
    _tone_chord_ringer__bb3_major_freq_1 = TextField(column_name='@tone.chord.ringer.Bb3Major.freq.1', null=True)
    _tone_chord_ringer__bb3_major_freq_2 = TextField(column_name='@tone.chord.ringer.Bb3Major.freq.2', null=True)
    _tone_chord_ringer__bb3_major_freq_3 = TextField(column_name='@tone.chord.ringer.Bb3Major.freq.3', null=True)
    _tone_chord_ringer__bb3_major_freq_4 = TextField(column_name='@tone.chord.ringer.Bb3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3Major.freq'

class TonechordringerBb3Majorlevel(BaseModel):
    _tone_chord_ringer__bb3_major_level_1 = TextField(column_name='@tone.chord.ringer.Bb3Major.level.1', null=True)
    _tone_chord_ringer__bb3_major_level_2 = TextField(column_name='@tone.chord.ringer.Bb3Major.level.2', null=True)
    _tone_chord_ringer__bb3_major_level_3 = TextField(column_name='@tone.chord.ringer.Bb3Major.level.3', null=True)
    _tone_chord_ringer__bb3_major_level_4 = TextField(column_name='@tone.chord.ringer.Bb3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb3Major.level'

class TonechordringerBb4(BaseModel):
    _tone_chord_ringer__bb4_off_dur = TextField(column_name='@tone.chord.ringer.Bb4.offDur', null=True)
    _tone_chord_ringer__bb4_on_dur = TextField(column_name='@tone.chord.ringer.Bb4.onDur', null=True)
    _tone_chord_ringer__bb4_repeat = TextField(column_name='@tone.chord.ringer.Bb4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb4'

class TonechordringerBb4Freq(BaseModel):
    _tone_chord_ringer__bb4_freq_1 = TextField(column_name='@tone.chord.ringer.Bb4.freq.1', null=True)
    _tone_chord_ringer__bb4_freq_2 = TextField(column_name='@tone.chord.ringer.Bb4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb4.freq'

class TonechordringerBb4Level(BaseModel):
    _tone_chord_ringer__bb4_level_1 = TextField(column_name='@tone.chord.ringer.Bb4.level.1', null=True)
    _tone_chord_ringer__bb4_level_2 = TextField(column_name='@tone.chord.ringer.Bb4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Bb4.level'

class Tonechordringerc3(BaseModel):
    _tone_chord_ringer_c3_off_dur = TextField(column_name='@tone.chord.ringer.C3.offDur', null=True)
    _tone_chord_ringer_c3_on_dur = TextField(column_name='@tone.chord.ringer.C3.onDur', null=True)
    _tone_chord_ringer_c3_repeat = TextField(column_name='@tone.chord.ringer.C3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3'

class Tonechordringerc3Freq(BaseModel):
    _tone_chord_ringer_c3_freq_1 = TextField(column_name='@tone.chord.ringer.C3.freq.1', null=True)
    _tone_chord_ringer_c3_freq_2 = TextField(column_name='@tone.chord.ringer.C3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3.freq'

class Tonechordringerc3Level(BaseModel):
    _tone_chord_ringer_c3_level_1 = TextField(column_name='@tone.chord.ringer.C3.level.1', null=True)
    _tone_chord_ringer_c3_level_2 = TextField(column_name='@tone.chord.ringer.C3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3.level'

class Tonechordringerc3Major(BaseModel):
    _tone_chord_ringer_c3_major_off_dur = TextField(column_name='@tone.chord.ringer.C3Major.offDur', null=True)
    _tone_chord_ringer_c3_major_on_dur = TextField(column_name='@tone.chord.ringer.C3Major.onDur', null=True)
    _tone_chord_ringer_c3_major_repeat = TextField(column_name='@tone.chord.ringer.C3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3Major'

class Tonechordringerc3Majorfreq(BaseModel):
    _tone_chord_ringer_c3_major_freq_1 = TextField(column_name='@tone.chord.ringer.C3Major.freq.1', null=True)
    _tone_chord_ringer_c3_major_freq_2 = TextField(column_name='@tone.chord.ringer.C3Major.freq.2', null=True)
    _tone_chord_ringer_c3_major_freq_3 = TextField(column_name='@tone.chord.ringer.C3Major.freq.3', null=True)
    _tone_chord_ringer_c3_major_freq_4 = TextField(column_name='@tone.chord.ringer.C3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3Major.freq'

class Tonechordringerc3Majorlevel(BaseModel):
    _tone_chord_ringer_c3_major_level_1 = TextField(column_name='@tone.chord.ringer.C3Major.level.1', null=True)
    _tone_chord_ringer_c3_major_level_2 = TextField(column_name='@tone.chord.ringer.C3Major.level.2', null=True)
    _tone_chord_ringer_c3_major_level_3 = TextField(column_name='@tone.chord.ringer.C3Major.level.3', null=True)
    _tone_chord_ringer_c3_major_level_4 = TextField(column_name='@tone.chord.ringer.C3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C3Major.level'

class Tonechordringerc4(BaseModel):
    _tone_chord_ringer_c4_off_dur = TextField(column_name='@tone.chord.ringer.C4.offDur', null=True)
    _tone_chord_ringer_c4_on_dur = TextField(column_name='@tone.chord.ringer.C4.onDur', null=True)
    _tone_chord_ringer_c4_repeat = TextField(column_name='@tone.chord.ringer.C4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C4'

class Tonechordringerc4Freq(BaseModel):
    _tone_chord_ringer_c4_freq_1 = TextField(column_name='@tone.chord.ringer.C4.freq.1', null=True)
    _tone_chord_ringer_c4_freq_2 = TextField(column_name='@tone.chord.ringer.C4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C4.freq'

class Tonechordringerc4Level(BaseModel):
    _tone_chord_ringer_c4_level_1 = TextField(column_name='@tone.chord.ringer.C4.level.1', null=True)
    _tone_chord_ringer_c4_level_2 = TextField(column_name='@tone.chord.ringer.C4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.C4.level'

class Tonechordringerd3(BaseModel):
    _tone_chord_ringer_d3_off_dur = TextField(column_name='@tone.chord.ringer.D3.offDur', null=True)
    _tone_chord_ringer_d3_on_dur = TextField(column_name='@tone.chord.ringer.D3.onDur', null=True)
    _tone_chord_ringer_d3_repeat = TextField(column_name='@tone.chord.ringer.D3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3'

class Tonechordringerd3Freq(BaseModel):
    _tone_chord_ringer_d3_freq_1 = TextField(column_name='@tone.chord.ringer.D3.freq.1', null=True)
    _tone_chord_ringer_d3_freq_2 = TextField(column_name='@tone.chord.ringer.D3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3.freq'

class Tonechordringerd3Level(BaseModel):
    _tone_chord_ringer_d3_level_1 = TextField(column_name='@tone.chord.ringer.D3.level.1', null=True)
    _tone_chord_ringer_d3_level_2 = TextField(column_name='@tone.chord.ringer.D3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3.level'

class Tonechordringerd3Major(BaseModel):
    _tone_chord_ringer_d3_major_off_dur = TextField(column_name='@tone.chord.ringer.D3Major.offDur', null=True)
    _tone_chord_ringer_d3_major_on_dur = TextField(column_name='@tone.chord.ringer.D3Major.onDur', null=True)
    _tone_chord_ringer_d3_major_repeat = TextField(column_name='@tone.chord.ringer.D3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3Major'

class Tonechordringerd3Majorfreq(BaseModel):
    _tone_chord_ringer_d3_major_freq_1 = TextField(column_name='@tone.chord.ringer.D3Major.freq.1', null=True)
    _tone_chord_ringer_d3_major_freq_2 = TextField(column_name='@tone.chord.ringer.D3Major.freq.2', null=True)
    _tone_chord_ringer_d3_major_freq_3 = TextField(column_name='@tone.chord.ringer.D3Major.freq.3', null=True)
    _tone_chord_ringer_d3_major_freq_4 = TextField(column_name='@tone.chord.ringer.D3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3Major.freq'

class Tonechordringerd3Majorlevel(BaseModel):
    _tone_chord_ringer_d3_major_level_1 = TextField(column_name='@tone.chord.ringer.D3Major.level.1', null=True)
    _tone_chord_ringer_d3_major_level_2 = TextField(column_name='@tone.chord.ringer.D3Major.level.2', null=True)
    _tone_chord_ringer_d3_major_level_3 = TextField(column_name='@tone.chord.ringer.D3Major.level.3', null=True)
    _tone_chord_ringer_d3_major_level_4 = TextField(column_name='@tone.chord.ringer.D3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D3Major.level'

class Tonechordringerd4(BaseModel):
    _tone_chord_ringer_d4_off_dur = TextField(column_name='@tone.chord.ringer.D4.offDur', null=True)
    _tone_chord_ringer_d4_on_dur = TextField(column_name='@tone.chord.ringer.D4.onDur', null=True)
    _tone_chord_ringer_d4_repeat = TextField(column_name='@tone.chord.ringer.D4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D4'

class Tonechordringerd4Freq(BaseModel):
    _tone_chord_ringer_d4_freq_1 = TextField(column_name='@tone.chord.ringer.D4.freq.1', null=True)
    _tone_chord_ringer_d4_freq_2 = TextField(column_name='@tone.chord.ringer.D4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D4.freq'

class Tonechordringerd4Level(BaseModel):
    _tone_chord_ringer_d4_level_1 = TextField(column_name='@tone.chord.ringer.D4.level.1', null=True)
    _tone_chord_ringer_d4_level_2 = TextField(column_name='@tone.chord.ringer.D4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.D4.level'

class TonechordringerDb3(BaseModel):
    _tone_chord_ringer__db3_off_dur = TextField(column_name='@tone.chord.ringer.Db3.offDur', null=True)
    _tone_chord_ringer__db3_on_dur = TextField(column_name='@tone.chord.ringer.Db3.onDur', null=True)
    _tone_chord_ringer__db3_repeat = TextField(column_name='@tone.chord.ringer.Db3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3'

class TonechordringerDb3Freq(BaseModel):
    _tone_chord_ringer__db3_freq_1 = TextField(column_name='@tone.chord.ringer.Db3.freq.1', null=True)
    _tone_chord_ringer__db3_freq_2 = TextField(column_name='@tone.chord.ringer.Db3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3.freq'

class TonechordringerDb3Level(BaseModel):
    _tone_chord_ringer__db3_level_1 = TextField(column_name='@tone.chord.ringer.Db3.level.1', null=True)
    _tone_chord_ringer__db3_level_2 = TextField(column_name='@tone.chord.ringer.Db3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3.level'

class TonechordringerDb3Major(BaseModel):
    _tone_chord_ringer__db3_major_off_dur = TextField(column_name='@tone.chord.ringer.Db3Major.offDur', null=True)
    _tone_chord_ringer__db3_major_on_dur = TextField(column_name='@tone.chord.ringer.Db3Major.onDur', null=True)
    _tone_chord_ringer__db3_major_repeat = TextField(column_name='@tone.chord.ringer.Db3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3Major'

class TonechordringerDb3Majorfreq(BaseModel):
    _tone_chord_ringer__db3_major_freq_1 = TextField(column_name='@tone.chord.ringer.Db3Major.freq.1', null=True)
    _tone_chord_ringer__db3_major_freq_2 = TextField(column_name='@tone.chord.ringer.Db3Major.freq.2', null=True)
    _tone_chord_ringer__db3_major_freq_3 = TextField(column_name='@tone.chord.ringer.Db3Major.freq.3', null=True)
    _tone_chord_ringer__db3_major_freq_4 = TextField(column_name='@tone.chord.ringer.Db3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3Major.freq'

class TonechordringerDb3Majorlevel(BaseModel):
    _tone_chord_ringer__db3_major_level_1 = TextField(column_name='@tone.chord.ringer.Db3Major.level.1', null=True)
    _tone_chord_ringer__db3_major_level_2 = TextField(column_name='@tone.chord.ringer.Db3Major.level.2', null=True)
    _tone_chord_ringer__db3_major_level_3 = TextField(column_name='@tone.chord.ringer.Db3Major.level.3', null=True)
    _tone_chord_ringer__db3_major_level_4 = TextField(column_name='@tone.chord.ringer.Db3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db3Major.level'

class TonechordringerDb4(BaseModel):
    _tone_chord_ringer__db4_off_dur = TextField(column_name='@tone.chord.ringer.Db4.offDur', null=True)
    _tone_chord_ringer__db4_on_dur = TextField(column_name='@tone.chord.ringer.Db4.onDur', null=True)
    _tone_chord_ringer__db4_repeat = TextField(column_name='@tone.chord.ringer.Db4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db4'

class TonechordringerDb4Freq(BaseModel):
    _tone_chord_ringer__db4_freq_1 = TextField(column_name='@tone.chord.ringer.Db4.freq.1', null=True)
    _tone_chord_ringer__db4_freq_2 = TextField(column_name='@tone.chord.ringer.Db4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db4.freq'

class TonechordringerDb4Level(BaseModel):
    _tone_chord_ringer__db4_level_1 = TextField(column_name='@tone.chord.ringer.Db4.level.1', null=True)
    _tone_chord_ringer__db4_level_2 = TextField(column_name='@tone.chord.ringer.Db4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Db4.level'

class Tonechordringere3(BaseModel):
    _tone_chord_ringer_e3_off_dur = TextField(column_name='@tone.chord.ringer.E3.offDur', null=True)
    _tone_chord_ringer_e3_on_dur = TextField(column_name='@tone.chord.ringer.E3.onDur', null=True)
    _tone_chord_ringer_e3_repeat = TextField(column_name='@tone.chord.ringer.E3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3'

class Tonechordringere3Freq(BaseModel):
    _tone_chord_ringer_e3_freq_1 = TextField(column_name='@tone.chord.ringer.E3.freq.1', null=True)
    _tone_chord_ringer_e3_freq_2 = TextField(column_name='@tone.chord.ringer.E3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3.freq'

class Tonechordringere3Level(BaseModel):
    _tone_chord_ringer_e3_level_1 = TextField(column_name='@tone.chord.ringer.E3.level.1', null=True)
    _tone_chord_ringer_e3_level_2 = TextField(column_name='@tone.chord.ringer.E3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3.level'

class Tonechordringere3Major(BaseModel):
    _tone_chord_ringer_e3_major_off_dur = TextField(column_name='@tone.chord.ringer.E3Major.offDur', null=True)
    _tone_chord_ringer_e3_major_on_dur = TextField(column_name='@tone.chord.ringer.E3Major.onDur', null=True)
    _tone_chord_ringer_e3_major_repeat = TextField(column_name='@tone.chord.ringer.E3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3Major'

class Tonechordringere3Majorfreq(BaseModel):
    _tone_chord_ringer_e3_major_freq_1 = TextField(column_name='@tone.chord.ringer.E3Major.freq.1', null=True)
    _tone_chord_ringer_e3_major_freq_2 = TextField(column_name='@tone.chord.ringer.E3Major.freq.2', null=True)
    _tone_chord_ringer_e3_major_freq_3 = TextField(column_name='@tone.chord.ringer.E3Major.freq.3', null=True)
    _tone_chord_ringer_e3_major_freq_4 = TextField(column_name='@tone.chord.ringer.E3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3Major.freq'

class Tonechordringere3Majorlevel(BaseModel):
    _tone_chord_ringer_e3_major_level_1 = TextField(column_name='@tone.chord.ringer.E3Major.level.1', null=True)
    _tone_chord_ringer_e3_major_level_2 = TextField(column_name='@tone.chord.ringer.E3Major.level.2', null=True)
    _tone_chord_ringer_e3_major_level_3 = TextField(column_name='@tone.chord.ringer.E3Major.level.3', null=True)
    _tone_chord_ringer_e3_major_level_4 = TextField(column_name='@tone.chord.ringer.E3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E3Major.level'

class Tonechordringere4(BaseModel):
    _tone_chord_ringer_e4_off_dur = TextField(column_name='@tone.chord.ringer.E4.offDur', null=True)
    _tone_chord_ringer_e4_on_dur = TextField(column_name='@tone.chord.ringer.E4.onDur', null=True)
    _tone_chord_ringer_e4_repeat = TextField(column_name='@tone.chord.ringer.E4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E4'

class Tonechordringere4Freq(BaseModel):
    _tone_chord_ringer_e4_freq_1 = TextField(column_name='@tone.chord.ringer.E4.freq.1', null=True)
    _tone_chord_ringer_e4_freq_2 = TextField(column_name='@tone.chord.ringer.E4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E4.freq'

class Tonechordringere4Level(BaseModel):
    _tone_chord_ringer_e4_level_1 = TextField(column_name='@tone.chord.ringer.E4.level.1', null=True)
    _tone_chord_ringer_e4_level_2 = TextField(column_name='@tone.chord.ringer.E4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.E4.level'

class TonechordringerEb3(BaseModel):
    _tone_chord_ringer__eb3_off_dur = TextField(column_name='@tone.chord.ringer.Eb3.offDur', null=True)
    _tone_chord_ringer__eb3_on_dur = TextField(column_name='@tone.chord.ringer.Eb3.onDur', null=True)
    _tone_chord_ringer__eb3_repeat = TextField(column_name='@tone.chord.ringer.Eb3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3'

class TonechordringerEb3Freq(BaseModel):
    _tone_chord_ringer__eb3_freq_1 = TextField(column_name='@tone.chord.ringer.Eb3.freq.1', null=True)
    _tone_chord_ringer__eb3_freq_2 = TextField(column_name='@tone.chord.ringer.Eb3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3.freq'

class TonechordringerEb3Level(BaseModel):
    _tone_chord_ringer__eb3_level_1 = TextField(column_name='@tone.chord.ringer.Eb3.level.1', null=True)
    _tone_chord_ringer__eb3_level_2 = TextField(column_name='@tone.chord.ringer.Eb3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3.level'

class TonechordringerEb3Major(BaseModel):
    _tone_chord_ringer__eb3_major_off_dur = TextField(column_name='@tone.chord.ringer.Eb3Major.offDur', null=True)
    _tone_chord_ringer__eb3_major_on_dur = TextField(column_name='@tone.chord.ringer.Eb3Major.onDur', null=True)
    _tone_chord_ringer__eb3_major_repeat = TextField(column_name='@tone.chord.ringer.Eb3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3Major'

class TonechordringerEb3Majorfreq(BaseModel):
    _tone_chord_ringer__eb3_major_freq_1 = TextField(column_name='@tone.chord.ringer.Eb3Major.freq.1', null=True)
    _tone_chord_ringer__eb3_major_freq_2 = TextField(column_name='@tone.chord.ringer.Eb3Major.freq.2', null=True)
    _tone_chord_ringer__eb3_major_freq_3 = TextField(column_name='@tone.chord.ringer.Eb3Major.freq.3', null=True)
    _tone_chord_ringer__eb3_major_freq_4 = TextField(column_name='@tone.chord.ringer.Eb3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3Major.freq'

class TonechordringerEb3Majorlevel(BaseModel):
    _tone_chord_ringer__eb3_major_level_1 = TextField(column_name='@tone.chord.ringer.Eb3Major.level.1', null=True)
    _tone_chord_ringer__eb3_major_level_2 = TextField(column_name='@tone.chord.ringer.Eb3Major.level.2', null=True)
    _tone_chord_ringer__eb3_major_level_3 = TextField(column_name='@tone.chord.ringer.Eb3Major.level.3', null=True)
    _tone_chord_ringer__eb3_major_level_4 = TextField(column_name='@tone.chord.ringer.Eb3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb3Major.level'

class TonechordringerEb4(BaseModel):
    _tone_chord_ringer__eb4_off_dur = TextField(column_name='@tone.chord.ringer.Eb4.offDur', null=True)
    _tone_chord_ringer__eb4_on_dur = TextField(column_name='@tone.chord.ringer.Eb4.onDur', null=True)
    _tone_chord_ringer__eb4_repeat = TextField(column_name='@tone.chord.ringer.Eb4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb4'

class TonechordringerEb4Freq(BaseModel):
    _tone_chord_ringer__eb4_freq_1 = TextField(column_name='@tone.chord.ringer.Eb4.freq.1', null=True)
    _tone_chord_ringer__eb4_freq_2 = TextField(column_name='@tone.chord.ringer.Eb4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb4.freq'

class TonechordringerEb4Level(BaseModel):
    _tone_chord_ringer__eb4_level_1 = TextField(column_name='@tone.chord.ringer.Eb4.level.1', null=True)
    _tone_chord_ringer__eb4_level_2 = TextField(column_name='@tone.chord.ringer.Eb4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Eb4.level'

class Tonechordringerf2(BaseModel):
    _tone_chord_ringer_f2_off_dur = TextField(column_name='@tone.chord.ringer.F2.offDur', null=True)
    _tone_chord_ringer_f2_on_dur = TextField(column_name='@tone.chord.ringer.F2.onDur', null=True)
    _tone_chord_ringer_f2_repeat = TextField(column_name='@tone.chord.ringer.F2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F2'

class Tonechordringerf2Freq(BaseModel):
    _tone_chord_ringer_f2_freq_1 = TextField(column_name='@tone.chord.ringer.F2.freq.1', null=True)
    _tone_chord_ringer_f2_freq_2 = TextField(column_name='@tone.chord.ringer.F2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F2.freq'

class Tonechordringerf2Level(BaseModel):
    _tone_chord_ringer_f2_level_1 = TextField(column_name='@tone.chord.ringer.F2.level.1', null=True)
    _tone_chord_ringer_f2_level_2 = TextField(column_name='@tone.chord.ringer.F2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F2.level'

class Tonechordringerf3(BaseModel):
    _tone_chord_ringer_f3_off_dur = TextField(column_name='@tone.chord.ringer.F3.offDur', null=True)
    _tone_chord_ringer_f3_on_dur = TextField(column_name='@tone.chord.ringer.F3.onDur', null=True)
    _tone_chord_ringer_f3_repeat = TextField(column_name='@tone.chord.ringer.F3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3'

class Tonechordringerf3Freq(BaseModel):
    _tone_chord_ringer_f3_freq_1 = TextField(column_name='@tone.chord.ringer.F3.freq.1', null=True)
    _tone_chord_ringer_f3_freq_2 = TextField(column_name='@tone.chord.ringer.F3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3.freq'

class Tonechordringerf3Level(BaseModel):
    _tone_chord_ringer_f3_level_1 = TextField(column_name='@tone.chord.ringer.F3.level.1', null=True)
    _tone_chord_ringer_f3_level_2 = TextField(column_name='@tone.chord.ringer.F3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3.level'

class Tonechordringerf3Major(BaseModel):
    _tone_chord_ringer_f3_major_off_dur = TextField(column_name='@tone.chord.ringer.F3Major.offDur', null=True)
    _tone_chord_ringer_f3_major_on_dur = TextField(column_name='@tone.chord.ringer.F3Major.onDur', null=True)
    _tone_chord_ringer_f3_major_repeat = TextField(column_name='@tone.chord.ringer.F3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3Major'

class Tonechordringerf3Majorfreq(BaseModel):
    _tone_chord_ringer_f3_major_freq_1 = TextField(column_name='@tone.chord.ringer.F3Major.freq.1', null=True)
    _tone_chord_ringer_f3_major_freq_2 = TextField(column_name='@tone.chord.ringer.F3Major.freq.2', null=True)
    _tone_chord_ringer_f3_major_freq_3 = TextField(column_name='@tone.chord.ringer.F3Major.freq.3', null=True)
    _tone_chord_ringer_f3_major_freq_4 = TextField(column_name='@tone.chord.ringer.F3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3Major.freq'

class Tonechordringerf3Majorlevel(BaseModel):
    _tone_chord_ringer_f3_major_level_1 = TextField(column_name='@tone.chord.ringer.F3Major.level.1', null=True)
    _tone_chord_ringer_f3_major_level_2 = TextField(column_name='@tone.chord.ringer.F3Major.level.2', null=True)
    _tone_chord_ringer_f3_major_level_3 = TextField(column_name='@tone.chord.ringer.F3Major.level.3', null=True)
    _tone_chord_ringer_f3_major_level_4 = TextField(column_name='@tone.chord.ringer.F3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F3Major.level'

class Tonechordringerf4(BaseModel):
    _tone_chord_ringer_f4_off_dur = TextField(column_name='@tone.chord.ringer.F4.offDur', null=True)
    _tone_chord_ringer_f4_on_dur = TextField(column_name='@tone.chord.ringer.F4.onDur', null=True)
    _tone_chord_ringer_f4_repeat = TextField(column_name='@tone.chord.ringer.F4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F4'

class Tonechordringerf4Freq(BaseModel):
    _tone_chord_ringer_f4_freq_1 = TextField(column_name='@tone.chord.ringer.F4.freq.1', null=True)
    _tone_chord_ringer_f4_freq_2 = TextField(column_name='@tone.chord.ringer.F4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F4.freq'

class Tonechordringerf4Level(BaseModel):
    _tone_chord_ringer_f4_level_1 = TextField(column_name='@tone.chord.ringer.F4.level.1', null=True)
    _tone_chord_ringer_f4_level_2 = TextField(column_name='@tone.chord.ringer.F4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.F4.level'

class Tonechordringerg2(BaseModel):
    _tone_chord_ringer_g2_off_dur = TextField(column_name='@tone.chord.ringer.G2.offDur', null=True)
    _tone_chord_ringer_g2_on_dur = TextField(column_name='@tone.chord.ringer.G2.onDur', null=True)
    _tone_chord_ringer_g2_repeat = TextField(column_name='@tone.chord.ringer.G2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G2'

class Tonechordringerg2Freq(BaseModel):
    _tone_chord_ringer_g2_freq_1 = TextField(column_name='@tone.chord.ringer.G2.freq.1', null=True)
    _tone_chord_ringer_g2_freq_2 = TextField(column_name='@tone.chord.ringer.G2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G2.freq'

class Tonechordringerg2Level(BaseModel):
    _tone_chord_ringer_g2_level_1 = TextField(column_name='@tone.chord.ringer.G2.level.1', null=True)
    _tone_chord_ringer_g2_level_2 = TextField(column_name='@tone.chord.ringer.G2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G2.level'

class Tonechordringerg3(BaseModel):
    _tone_chord_ringer_g3_off_dur = TextField(column_name='@tone.chord.ringer.G3.offDur', null=True)
    _tone_chord_ringer_g3_on_dur = TextField(column_name='@tone.chord.ringer.G3.onDur', null=True)
    _tone_chord_ringer_g3_repeat = TextField(column_name='@tone.chord.ringer.G3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3'

class Tonechordringerg3Freq(BaseModel):
    _tone_chord_ringer_g3_freq_1 = TextField(column_name='@tone.chord.ringer.G3.freq.1', null=True)
    _tone_chord_ringer_g3_freq_2 = TextField(column_name='@tone.chord.ringer.G3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3.freq'

class Tonechordringerg3Level(BaseModel):
    _tone_chord_ringer_g3_level_1 = TextField(column_name='@tone.chord.ringer.G3.level.1', null=True)
    _tone_chord_ringer_g3_level_2 = TextField(column_name='@tone.chord.ringer.G3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3.level'

class Tonechordringerg3Major(BaseModel):
    _tone_chord_ringer_g3_major_off_dur = TextField(column_name='@tone.chord.ringer.G3Major.offDur', null=True)
    _tone_chord_ringer_g3_major_on_dur = TextField(column_name='@tone.chord.ringer.G3Major.onDur', null=True)
    _tone_chord_ringer_g3_major_repeat = TextField(column_name='@tone.chord.ringer.G3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3Major'

class Tonechordringerg3Majorfreq(BaseModel):
    _tone_chord_ringer_g3_major_freq_1 = TextField(column_name='@tone.chord.ringer.G3Major.freq.1', null=True)
    _tone_chord_ringer_g3_major_freq_2 = TextField(column_name='@tone.chord.ringer.G3Major.freq.2', null=True)
    _tone_chord_ringer_g3_major_freq_3 = TextField(column_name='@tone.chord.ringer.G3Major.freq.3', null=True)
    _tone_chord_ringer_g3_major_freq_4 = TextField(column_name='@tone.chord.ringer.G3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3Major.freq'

class Tonechordringerg3Majorlevel(BaseModel):
    _tone_chord_ringer_g3_major_level_1 = TextField(column_name='@tone.chord.ringer.G3Major.level.1', null=True)
    _tone_chord_ringer_g3_major_level_2 = TextField(column_name='@tone.chord.ringer.G3Major.level.2', null=True)
    _tone_chord_ringer_g3_major_level_3 = TextField(column_name='@tone.chord.ringer.G3Major.level.3', null=True)
    _tone_chord_ringer_g3_major_level_4 = TextField(column_name='@tone.chord.ringer.G3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.G3Major.level'

class TonechordringerGb2(BaseModel):
    _tone_chord_ringer__gb2_off_dur = TextField(column_name='@tone.chord.ringer.Gb2.offDur', null=True)
    _tone_chord_ringer__gb2_on_dur = TextField(column_name='@tone.chord.ringer.Gb2.onDur', null=True)
    _tone_chord_ringer__gb2_repeat = TextField(column_name='@tone.chord.ringer.Gb2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb2'

class TonechordringerGb2Freq(BaseModel):
    _tone_chord_ringer__gb2_freq_1 = TextField(column_name='@tone.chord.ringer.Gb2.freq.1', null=True)
    _tone_chord_ringer__gb2_freq_2 = TextField(column_name='@tone.chord.ringer.Gb2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb2.freq'

class TonechordringerGb2Level(BaseModel):
    _tone_chord_ringer__gb2_level_1 = TextField(column_name='@tone.chord.ringer.Gb2.level.1', null=True)
    _tone_chord_ringer__gb2_level_2 = TextField(column_name='@tone.chord.ringer.Gb2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb2.level'

class TonechordringerGb3(BaseModel):
    _tone_chord_ringer__gb3_off_dur = TextField(column_name='@tone.chord.ringer.Gb3.offDur', null=True)
    _tone_chord_ringer__gb3_on_dur = TextField(column_name='@tone.chord.ringer.Gb3.onDur', null=True)
    _tone_chord_ringer__gb3_repeat = TextField(column_name='@tone.chord.ringer.Gb3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3'

class TonechordringerGb3Freq(BaseModel):
    _tone_chord_ringer__gb3_freq_1 = TextField(column_name='@tone.chord.ringer.Gb3.freq.1', null=True)
    _tone_chord_ringer__gb3_freq_2 = TextField(column_name='@tone.chord.ringer.Gb3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3.freq'

class TonechordringerGb3Level(BaseModel):
    _tone_chord_ringer__gb3_level_1 = TextField(column_name='@tone.chord.ringer.Gb3.level.1', null=True)
    _tone_chord_ringer__gb3_level_2 = TextField(column_name='@tone.chord.ringer.Gb3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3.level'

class TonechordringerGb3Major(BaseModel):
    _tone_chord_ringer__gb3_major_off_dur = TextField(column_name='@tone.chord.ringer.Gb3Major.offDur', null=True)
    _tone_chord_ringer__gb3_major_on_dur = TextField(column_name='@tone.chord.ringer.Gb3Major.onDur', null=True)
    _tone_chord_ringer__gb3_major_repeat = TextField(column_name='@tone.chord.ringer.Gb3Major.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3Major'

class TonechordringerGb3Majorfreq(BaseModel):
    _tone_chord_ringer__gb3_major_freq_1 = TextField(column_name='@tone.chord.ringer.Gb3Major.freq.1', null=True)
    _tone_chord_ringer__gb3_major_freq_2 = TextField(column_name='@tone.chord.ringer.Gb3Major.freq.2', null=True)
    _tone_chord_ringer__gb3_major_freq_3 = TextField(column_name='@tone.chord.ringer.Gb3Major.freq.3', null=True)
    _tone_chord_ringer__gb3_major_freq_4 = TextField(column_name='@tone.chord.ringer.Gb3Major.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3Major.freq'

class TonechordringerGb3Majorlevel(BaseModel):
    _tone_chord_ringer__gb3_major_level_1 = TextField(column_name='@tone.chord.ringer.Gb3Major.level.1', null=True)
    _tone_chord_ringer__gb3_major_level_2 = TextField(column_name='@tone.chord.ringer.Gb3Major.level.2', null=True)
    _tone_chord_ringer__gb3_major_level_3 = TextField(column_name='@tone.chord.ringer.Gb3Major.level.3', null=True)
    _tone_chord_ringer__gb3_major_level_4 = TextField(column_name='@tone.chord.ringer.Gb3Major.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.Gb3Major.level'

class TonechordringeroriginalHigh(BaseModel):
    _tone_chord_ringer_original_high_off_dur = TextField(column_name='@tone.chord.ringer.originalHigh.offDur', null=True)
    _tone_chord_ringer_original_high_on_dur = TextField(column_name='@tone.chord.ringer.originalHigh.onDur', null=True)
    _tone_chord_ringer_original_high_repeat = TextField(column_name='@tone.chord.ringer.originalHigh.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalHigh'

class TonechordringeroriginalHighfreq(BaseModel):
    _tone_chord_ringer_original_high_freq_1 = TextField(column_name='@tone.chord.ringer.originalHigh.freq.1', null=True)
    _tone_chord_ringer_original_high_freq_2 = TextField(column_name='@tone.chord.ringer.originalHigh.freq.2', null=True)
    _tone_chord_ringer_original_high_freq_3 = TextField(column_name='@tone.chord.ringer.originalHigh.freq.3', null=True)
    _tone_chord_ringer_original_high_freq_4 = TextField(column_name='@tone.chord.ringer.originalHigh.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalHigh.freq'

class TonechordringeroriginalHighlevel(BaseModel):
    _tone_chord_ringer_original_high_level_1 = TextField(column_name='@tone.chord.ringer.originalHigh.level.1', null=True)
    _tone_chord_ringer_original_high_level_2 = TextField(column_name='@tone.chord.ringer.originalHigh.level.2', null=True)
    _tone_chord_ringer_original_high_level_3 = TextField(column_name='@tone.chord.ringer.originalHigh.level.3', null=True)
    _tone_chord_ringer_original_high_level_4 = TextField(column_name='@tone.chord.ringer.originalHigh.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalHigh.level'

class TonechordringeroriginalLow(BaseModel):
    _tone_chord_ringer_original_low_off_dur = TextField(column_name='@tone.chord.ringer.originalLow.offDur', null=True)
    _tone_chord_ringer_original_low_on_dur = TextField(column_name='@tone.chord.ringer.originalLow.onDur', null=True)
    _tone_chord_ringer_original_low_repeat = TextField(column_name='@tone.chord.ringer.originalLow.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalLow'

class TonechordringeroriginalLowfreq(BaseModel):
    _tone_chord_ringer_original_low_freq_1 = TextField(column_name='@tone.chord.ringer.originalLow.freq.1', null=True)
    _tone_chord_ringer_original_low_freq_2 = TextField(column_name='@tone.chord.ringer.originalLow.freq.2', null=True)
    _tone_chord_ringer_original_low_freq_3 = TextField(column_name='@tone.chord.ringer.originalLow.freq.3', null=True)
    _tone_chord_ringer_original_low_freq_4 = TextField(column_name='@tone.chord.ringer.originalLow.freq.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalLow.freq'

class TonechordringeroriginalLowlevel(BaseModel):
    _tone_chord_ringer_original_low_level_1 = TextField(column_name='@tone.chord.ringer.originalLow.level.1', null=True)
    _tone_chord_ringer_original_low_level_2 = TextField(column_name='@tone.chord.ringer.originalLow.level.2', null=True)
    _tone_chord_ringer_original_low_level_3 = TextField(column_name='@tone.chord.ringer.originalLow.level.3', null=True)
    _tone_chord_ringer_original_low_level_4 = TextField(column_name='@tone.chord.ringer.originalLow.level.4', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.originalLow.level'

class Tonechordringerringback(BaseModel):
    _tone_chord_ringer_ringback_off_dur = TextField(column_name='@tone.chord.ringer.ringback.offDur', null=True)
    _tone_chord_ringer_ringback_on_dur = TextField(column_name='@tone.chord.ringer.ringback.onDur', null=True)
    _tone_chord_ringer_ringback_repeat = TextField(column_name='@tone.chord.ringer.ringback.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.ringback'

class Tonechordringerringbackfreq(BaseModel):
    _tone_chord_ringer_ringback_freq_1 = TextField(column_name='@tone.chord.ringer.ringback.freq.1', null=True)
    _tone_chord_ringer_ringback_freq_2 = TextField(column_name='@tone.chord.ringer.ringback.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.ringback.freq'

class Tonechordringerringbacklevel(BaseModel):
    _tone_chord_ringer_ringback_level_1 = TextField(column_name='@tone.chord.ringer.ringback.level.1', null=True)
    _tone_chord_ringer_ringback_level_2 = TextField(column_name='@tone.chord.ringer.ringback.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.ringback.level'

class Tonechordringerspare1(BaseModel):
    _tone_chord_ringer_spare1_off_dur = TextField(column_name='@tone.chord.ringer.spare1.offDur', null=True)
    _tone_chord_ringer_spare1_on_dur = TextField(column_name='@tone.chord.ringer.spare1.onDur', null=True)
    _tone_chord_ringer_spare1_repeat = TextField(column_name='@tone.chord.ringer.spare1.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare1'

class Tonechordringerspare1Freq(BaseModel):
    _tone_chord_ringer_spare1_freq_1 = TextField(column_name='@tone.chord.ringer.spare1.freq.1', null=True)
    _tone_chord_ringer_spare1_freq_2 = TextField(column_name='@tone.chord.ringer.spare1.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare1.freq'

class Tonechordringerspare1Level(BaseModel):
    _tone_chord_ringer_spare1_level_1 = TextField(column_name='@tone.chord.ringer.spare1.level.1', null=True)
    _tone_chord_ringer_spare1_level_2 = TextField(column_name='@tone.chord.ringer.spare1.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare1.level'

class Tonechordringerspare10(BaseModel):
    _tone_chord_ringer_spare10_off_dur = TextField(column_name='@tone.chord.ringer.spare10.offDur', null=True)
    _tone_chord_ringer_spare10_on_dur = TextField(column_name='@tone.chord.ringer.spare10.onDur', null=True)
    _tone_chord_ringer_spare10_repeat = TextField(column_name='@tone.chord.ringer.spare10.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare10'

class Tonechordringerspare10Freq(BaseModel):
    _tone_chord_ringer_spare10_freq_1 = TextField(column_name='@tone.chord.ringer.spare10.freq.1', null=True)
    _tone_chord_ringer_spare10_freq_2 = TextField(column_name='@tone.chord.ringer.spare10.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare10.freq'

class Tonechordringerspare10Level(BaseModel):
    _tone_chord_ringer_spare10_level_1 = TextField(column_name='@tone.chord.ringer.spare10.level.1', null=True)
    _tone_chord_ringer_spare10_level_2 = TextField(column_name='@tone.chord.ringer.spare10.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare10.level'

class Tonechordringerspare11(BaseModel):
    _tone_chord_ringer_spare11_off_dur = TextField(column_name='@tone.chord.ringer.spare11.offDur', null=True)
    _tone_chord_ringer_spare11_on_dur = TextField(column_name='@tone.chord.ringer.spare11.onDur', null=True)
    _tone_chord_ringer_spare11_repeat = TextField(column_name='@tone.chord.ringer.spare11.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare11'

class Tonechordringerspare11Freq(BaseModel):
    _tone_chord_ringer_spare11_freq_1 = TextField(column_name='@tone.chord.ringer.spare11.freq.1', null=True)
    _tone_chord_ringer_spare11_freq_2 = TextField(column_name='@tone.chord.ringer.spare11.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare11.freq'

class Tonechordringerspare11Level(BaseModel):
    _tone_chord_ringer_spare11_level_1 = TextField(column_name='@tone.chord.ringer.spare11.level.1', null=True)
    _tone_chord_ringer_spare11_level_2 = TextField(column_name='@tone.chord.ringer.spare11.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare11.level'

class Tonechordringerspare12(BaseModel):
    _tone_chord_ringer_spare12_off_dur = TextField(column_name='@tone.chord.ringer.spare12.offDur', null=True)
    _tone_chord_ringer_spare12_on_dur = TextField(column_name='@tone.chord.ringer.spare12.onDur', null=True)
    _tone_chord_ringer_spare12_repeat = TextField(column_name='@tone.chord.ringer.spare12.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare12'

class Tonechordringerspare12Freq(BaseModel):
    _tone_chord_ringer_spare12_freq_1 = TextField(column_name='@tone.chord.ringer.spare12.freq.1', null=True)
    _tone_chord_ringer_spare12_freq_2 = TextField(column_name='@tone.chord.ringer.spare12.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare12.freq'

class Tonechordringerspare12Level(BaseModel):
    _tone_chord_ringer_spare12_level_1 = TextField(column_name='@tone.chord.ringer.spare12.level.1', null=True)
    _tone_chord_ringer_spare12_level_2 = TextField(column_name='@tone.chord.ringer.spare12.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare12.level'

class Tonechordringerspare13(BaseModel):
    _tone_chord_ringer_spare13_off_dur = TextField(column_name='@tone.chord.ringer.spare13.offDur', null=True)
    _tone_chord_ringer_spare13_on_dur = TextField(column_name='@tone.chord.ringer.spare13.onDur', null=True)
    _tone_chord_ringer_spare13_repeat = TextField(column_name='@tone.chord.ringer.spare13.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare13'

class Tonechordringerspare13Freq(BaseModel):
    _tone_chord_ringer_spare13_freq_1 = TextField(column_name='@tone.chord.ringer.spare13.freq.1', null=True)
    _tone_chord_ringer_spare13_freq_2 = TextField(column_name='@tone.chord.ringer.spare13.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare13.freq'

class Tonechordringerspare13Level(BaseModel):
    _tone_chord_ringer_spare13_level_1 = TextField(column_name='@tone.chord.ringer.spare13.level.1', null=True)
    _tone_chord_ringer_spare13_level_2 = TextField(column_name='@tone.chord.ringer.spare13.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare13.level'

class Tonechordringerspare14(BaseModel):
    _tone_chord_ringer_spare14_off_dur = TextField(column_name='@tone.chord.ringer.spare14.offDur', null=True)
    _tone_chord_ringer_spare14_on_dur = TextField(column_name='@tone.chord.ringer.spare14.onDur', null=True)
    _tone_chord_ringer_spare14_repeat = TextField(column_name='@tone.chord.ringer.spare14.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare14'

class Tonechordringerspare14Freq(BaseModel):
    _tone_chord_ringer_spare14_freq_1 = TextField(column_name='@tone.chord.ringer.spare14.freq.1', null=True)
    _tone_chord_ringer_spare14_freq_2 = TextField(column_name='@tone.chord.ringer.spare14.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare14.freq'

class Tonechordringerspare14Level(BaseModel):
    _tone_chord_ringer_spare14_level_1 = TextField(column_name='@tone.chord.ringer.spare14.level.1', null=True)
    _tone_chord_ringer_spare14_level_2 = TextField(column_name='@tone.chord.ringer.spare14.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare14.level'

class Tonechordringerspare15(BaseModel):
    _tone_chord_ringer_spare15_off_dur = TextField(column_name='@tone.chord.ringer.spare15.offDur', null=True)
    _tone_chord_ringer_spare15_on_dur = TextField(column_name='@tone.chord.ringer.spare15.onDur', null=True)
    _tone_chord_ringer_spare15_repeat = TextField(column_name='@tone.chord.ringer.spare15.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare15'

class Tonechordringerspare15Freq(BaseModel):
    _tone_chord_ringer_spare15_freq_1 = TextField(column_name='@tone.chord.ringer.spare15.freq.1', null=True)
    _tone_chord_ringer_spare15_freq_2 = TextField(column_name='@tone.chord.ringer.spare15.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare15.freq'

class Tonechordringerspare15Level(BaseModel):
    _tone_chord_ringer_spare15_level_1 = TextField(column_name='@tone.chord.ringer.spare15.level.1', null=True)
    _tone_chord_ringer_spare15_level_2 = TextField(column_name='@tone.chord.ringer.spare15.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare15.level'

class Tonechordringerspare16(BaseModel):
    _tone_chord_ringer_spare16_off_dur = TextField(column_name='@tone.chord.ringer.spare16.offDur', null=True)
    _tone_chord_ringer_spare16_on_dur = TextField(column_name='@tone.chord.ringer.spare16.onDur', null=True)
    _tone_chord_ringer_spare16_repeat = TextField(column_name='@tone.chord.ringer.spare16.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare16'

class Tonechordringerspare16Freq(BaseModel):
    _tone_chord_ringer_spare16_freq_1 = TextField(column_name='@tone.chord.ringer.spare16.freq.1', null=True)
    _tone_chord_ringer_spare16_freq_2 = TextField(column_name='@tone.chord.ringer.spare16.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare16.freq'

class Tonechordringerspare16Level(BaseModel):
    _tone_chord_ringer_spare16_level_1 = TextField(column_name='@tone.chord.ringer.spare16.level.1', null=True)
    _tone_chord_ringer_spare16_level_2 = TextField(column_name='@tone.chord.ringer.spare16.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare16.level'

class Tonechordringerspare17(BaseModel):
    _tone_chord_ringer_spare17_off_dur = TextField(column_name='@tone.chord.ringer.spare17.offDur', null=True)
    _tone_chord_ringer_spare17_on_dur = TextField(column_name='@tone.chord.ringer.spare17.onDur', null=True)
    _tone_chord_ringer_spare17_repeat = TextField(column_name='@tone.chord.ringer.spare17.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare17'

class Tonechordringerspare17Freq(BaseModel):
    _tone_chord_ringer_spare17_freq_1 = TextField(column_name='@tone.chord.ringer.spare17.freq.1', null=True)
    _tone_chord_ringer_spare17_freq_2 = TextField(column_name='@tone.chord.ringer.spare17.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare17.freq'

class Tonechordringerspare17Level(BaseModel):
    _tone_chord_ringer_spare17_level_1 = TextField(column_name='@tone.chord.ringer.spare17.level.1', null=True)
    _tone_chord_ringer_spare17_level_2 = TextField(column_name='@tone.chord.ringer.spare17.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare17.level'

class Tonechordringerspare18(BaseModel):
    _tone_chord_ringer_spare18_off_dur = TextField(column_name='@tone.chord.ringer.spare18.offDur', null=True)
    _tone_chord_ringer_spare18_on_dur = TextField(column_name='@tone.chord.ringer.spare18.onDur', null=True)
    _tone_chord_ringer_spare18_repeat = TextField(column_name='@tone.chord.ringer.spare18.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare18'

class Tonechordringerspare18Freq(BaseModel):
    _tone_chord_ringer_spare18_freq_1 = TextField(column_name='@tone.chord.ringer.spare18.freq.1', null=True)
    _tone_chord_ringer_spare18_freq_2 = TextField(column_name='@tone.chord.ringer.spare18.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare18.freq'

class Tonechordringerspare18Level(BaseModel):
    _tone_chord_ringer_spare18_level_1 = TextField(column_name='@tone.chord.ringer.spare18.level.1', null=True)
    _tone_chord_ringer_spare18_level_2 = TextField(column_name='@tone.chord.ringer.spare18.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare18.level'

class Tonechordringerspare19(BaseModel):
    _tone_chord_ringer_spare19_off_dur = TextField(column_name='@tone.chord.ringer.spare19.offDur', null=True)
    _tone_chord_ringer_spare19_on_dur = TextField(column_name='@tone.chord.ringer.spare19.onDur', null=True)
    _tone_chord_ringer_spare19_repeat = TextField(column_name='@tone.chord.ringer.spare19.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare19'

class Tonechordringerspare19Freq(BaseModel):
    _tone_chord_ringer_spare19_freq_1 = TextField(column_name='@tone.chord.ringer.spare19.freq.1', null=True)
    _tone_chord_ringer_spare19_freq_2 = TextField(column_name='@tone.chord.ringer.spare19.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare19.freq'

class Tonechordringerspare19Level(BaseModel):
    _tone_chord_ringer_spare19_level_1 = TextField(column_name='@tone.chord.ringer.spare19.level.1', null=True)
    _tone_chord_ringer_spare19_level_2 = TextField(column_name='@tone.chord.ringer.spare19.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare19.level'

class Tonechordringerspare2(BaseModel):
    _tone_chord_ringer_spare2_off_dur = TextField(column_name='@tone.chord.ringer.spare2.offDur', null=True)
    _tone_chord_ringer_spare2_on_dur = TextField(column_name='@tone.chord.ringer.spare2.onDur', null=True)
    _tone_chord_ringer_spare2_repeat = TextField(column_name='@tone.chord.ringer.spare2.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare2'

class Tonechordringerspare2Freq(BaseModel):
    _tone_chord_ringer_spare2_freq_1 = TextField(column_name='@tone.chord.ringer.spare2.freq.1', null=True)
    _tone_chord_ringer_spare2_freq_2 = TextField(column_name='@tone.chord.ringer.spare2.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare2.freq'

class Tonechordringerspare2Level(BaseModel):
    _tone_chord_ringer_spare2_level_1 = TextField(column_name='@tone.chord.ringer.spare2.level.1', null=True)
    _tone_chord_ringer_spare2_level_2 = TextField(column_name='@tone.chord.ringer.spare2.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare2.level'

class Tonechordringerspare3(BaseModel):
    _tone_chord_ringer_spare3_off_dur = TextField(column_name='@tone.chord.ringer.spare3.offDur', null=True)
    _tone_chord_ringer_spare3_on_dur = TextField(column_name='@tone.chord.ringer.spare3.onDur', null=True)
    _tone_chord_ringer_spare3_repeat = TextField(column_name='@tone.chord.ringer.spare3.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare3'

class Tonechordringerspare3Freq(BaseModel):
    _tone_chord_ringer_spare3_freq_1 = TextField(column_name='@tone.chord.ringer.spare3.freq.1', null=True)
    _tone_chord_ringer_spare3_freq_2 = TextField(column_name='@tone.chord.ringer.spare3.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare3.freq'

class Tonechordringerspare3Level(BaseModel):
    _tone_chord_ringer_spare3_level_1 = TextField(column_name='@tone.chord.ringer.spare3.level.1', null=True)
    _tone_chord_ringer_spare3_level_2 = TextField(column_name='@tone.chord.ringer.spare3.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare3.level'

class Tonechordringerspare4(BaseModel):
    _tone_chord_ringer_spare4_off_dur = TextField(column_name='@tone.chord.ringer.spare4.offDur', null=True)
    _tone_chord_ringer_spare4_on_dur = TextField(column_name='@tone.chord.ringer.spare4.onDur', null=True)
    _tone_chord_ringer_spare4_repeat = TextField(column_name='@tone.chord.ringer.spare4.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare4'

class Tonechordringerspare4Freq(BaseModel):
    _tone_chord_ringer_spare4_freq_1 = TextField(column_name='@tone.chord.ringer.spare4.freq.1', null=True)
    _tone_chord_ringer_spare4_freq_2 = TextField(column_name='@tone.chord.ringer.spare4.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare4.freq'

class Tonechordringerspare4Level(BaseModel):
    _tone_chord_ringer_spare4_level_1 = TextField(column_name='@tone.chord.ringer.spare4.level.1', null=True)
    _tone_chord_ringer_spare4_level_2 = TextField(column_name='@tone.chord.ringer.spare4.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare4.level'

class Tonechordringerspare5(BaseModel):
    _tone_chord_ringer_spare5_off_dur = TextField(column_name='@tone.chord.ringer.spare5.offDur', null=True)
    _tone_chord_ringer_spare5_on_dur = TextField(column_name='@tone.chord.ringer.spare5.onDur', null=True)
    _tone_chord_ringer_spare5_repeat = TextField(column_name='@tone.chord.ringer.spare5.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare5'

class Tonechordringerspare5Freq(BaseModel):
    _tone_chord_ringer_spare5_freq_1 = TextField(column_name='@tone.chord.ringer.spare5.freq.1', null=True)
    _tone_chord_ringer_spare5_freq_2 = TextField(column_name='@tone.chord.ringer.spare5.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare5.freq'

class Tonechordringerspare5Level(BaseModel):
    _tone_chord_ringer_spare5_level_1 = TextField(column_name='@tone.chord.ringer.spare5.level.1', null=True)
    _tone_chord_ringer_spare5_level_2 = TextField(column_name='@tone.chord.ringer.spare5.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare5.level'

class Tonechordringerspare6(BaseModel):
    _tone_chord_ringer_spare6_off_dur = TextField(column_name='@tone.chord.ringer.spare6.offDur', null=True)
    _tone_chord_ringer_spare6_on_dur = TextField(column_name='@tone.chord.ringer.spare6.onDur', null=True)
    _tone_chord_ringer_spare6_repeat = TextField(column_name='@tone.chord.ringer.spare6.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare6'

class Tonechordringerspare6Freq(BaseModel):
    _tone_chord_ringer_spare6_freq_1 = TextField(column_name='@tone.chord.ringer.spare6.freq.1', null=True)
    _tone_chord_ringer_spare6_freq_2 = TextField(column_name='@tone.chord.ringer.spare6.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare6.freq'

class Tonechordringerspare6Level(BaseModel):
    _tone_chord_ringer_spare6_level_1 = TextField(column_name='@tone.chord.ringer.spare6.level.1', null=True)
    _tone_chord_ringer_spare6_level_2 = TextField(column_name='@tone.chord.ringer.spare6.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare6.level'

class Tonechordringerspare7(BaseModel):
    _tone_chord_ringer_spare7_off_dur = TextField(column_name='@tone.chord.ringer.spare7.offDur', null=True)
    _tone_chord_ringer_spare7_on_dur = TextField(column_name='@tone.chord.ringer.spare7.onDur', null=True)
    _tone_chord_ringer_spare7_repeat = TextField(column_name='@tone.chord.ringer.spare7.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare7'

class Tonechordringerspare7Freq(BaseModel):
    _tone_chord_ringer_spare7_freq_1 = TextField(column_name='@tone.chord.ringer.spare7.freq.1', null=True)
    _tone_chord_ringer_spare7_freq_2 = TextField(column_name='@tone.chord.ringer.spare7.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare7.freq'

class Tonechordringerspare7Level(BaseModel):
    _tone_chord_ringer_spare7_level_1 = TextField(column_name='@tone.chord.ringer.spare7.level.1', null=True)
    _tone_chord_ringer_spare7_level_2 = TextField(column_name='@tone.chord.ringer.spare7.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare7.level'

class Tonechordringerspare8(BaseModel):
    _tone_chord_ringer_spare8_off_dur = TextField(column_name='@tone.chord.ringer.spare8.offDur', null=True)
    _tone_chord_ringer_spare8_on_dur = TextField(column_name='@tone.chord.ringer.spare8.onDur', null=True)
    _tone_chord_ringer_spare8_repeat = TextField(column_name='@tone.chord.ringer.spare8.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare8'

class Tonechordringerspare8Freq(BaseModel):
    _tone_chord_ringer_spare8_freq_1 = TextField(column_name='@tone.chord.ringer.spare8.freq.1', null=True)
    _tone_chord_ringer_spare8_freq_2 = TextField(column_name='@tone.chord.ringer.spare8.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare8.freq'

class Tonechordringerspare8Level(BaseModel):
    _tone_chord_ringer_spare8_level_1 = TextField(column_name='@tone.chord.ringer.spare8.level.1', null=True)
    _tone_chord_ringer_spare8_level_2 = TextField(column_name='@tone.chord.ringer.spare8.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare8.level'

class Tonechordringerspare9(BaseModel):
    _tone_chord_ringer_spare9_off_dur = TextField(column_name='@tone.chord.ringer.spare9.offDur', null=True)
    _tone_chord_ringer_spare9_on_dur = TextField(column_name='@tone.chord.ringer.spare9.onDur', null=True)
    _tone_chord_ringer_spare9_repeat = TextField(column_name='@tone.chord.ringer.spare9.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare9'

class Tonechordringerspare9Freq(BaseModel):
    _tone_chord_ringer_spare9_freq_1 = TextField(column_name='@tone.chord.ringer.spare9.freq.1', null=True)
    _tone_chord_ringer_spare9_freq_2 = TextField(column_name='@tone.chord.ringer.spare9.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare9.freq'

class Tonechordringerspare9Level(BaseModel):
    _tone_chord_ringer_spare9_level_1 = TextField(column_name='@tone.chord.ringer.spare9.level.1', null=True)
    _tone_chord_ringer_spare9_level_2 = TextField(column_name='@tone.chord.ringer.spare9.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.spare9.level'

class Tonechordringersplash(BaseModel):
    _tone_chord_ringer_splash_off_dur = TextField(column_name='@tone.chord.ringer.splash.offDur', null=True)
    _tone_chord_ringer_splash_on_dur = TextField(column_name='@tone.chord.ringer.splash.onDur', null=True)
    _tone_chord_ringer_splash_repeat = TextField(column_name='@tone.chord.ringer.splash.repeat', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.splash'

class Tonechordringersplashfreq(BaseModel):
    _tone_chord_ringer_splash_freq_1 = TextField(column_name='@tone.chord.ringer.splash.freq.1', null=True)
    _tone_chord_ringer_splash_freq_2 = TextField(column_name='@tone.chord.ringer.splash.freq.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.splash.freq'

class Tonechordringersplashlevel(BaseModel):
    _tone_chord_ringer_splash_level_1 = TextField(column_name='@tone.chord.ringer.splash.level.1', null=True)
    _tone_chord_ringer_splash_level_2 = TextField(column_name='@tone.chord.ringer.splash.level.2', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'tone.chord.ringer.splash.level'

class Twampportudp(BaseModel):
    _twamp_port_udp__port_range_end = TextField(column_name='@twamp.port.udp.PortRangeEnd', null=True)
    _twamp_port_udp__port_range_start = TextField(column_name='@twamp.port.udp.PortRangeStart', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'twamp.port.udp'

class Twampudp(BaseModel):
    _twamp_udp_max_session = TextField(column_name='@twamp.udp.maxSession', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'twamp.udp'

class Up(BaseModel):
    _up_headset_only_alerting = TextField(column_name='@up.headsetOnlyAlerting', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'up'

class Upefk(BaseModel):
    _up_efk_flk_index_required = TextField(column_name='@up.EFK.FLKIndexRequired', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'up.EFK'

class Upringer(BaseModel):
    _up_ringer_minimum_volume = TextField(column_name='@up.ringer.minimumVolume', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'up.ringer'

class UpsoftkeytransferTypeOption(BaseModel):
    _up_softkey_transfer_type_option_enabled = TextField(column_name='@up.softkey.transferTypeOption.enabled', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'up.softkey.transferTypeOption'

class UpstaticBlf(BaseModel):
    _up_static_blf_flk_index_required = TextField(column_name='@up.staticBLF.FLKIndexRequired', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'up.staticBLF'

class Upgradecustomserver(BaseModel):
    _upgrade_custom_server_url = TextField(column_name='@upgrade.custom.server.url', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'upgrade.custom.server'

class Upgradeplcmserver(BaseModel):
    _upgrade_plcm_server_url = TextField(column_name='@upgrade.plcm.server.url', null=True)
    _upgrade_plcm_server_url_cx5500 = TextField(column_name='@upgrade.plcm.server.url.CX5500', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'upgrade.plcm.server'

class VoIpProtobpdhcpv4(BaseModel):
    _vo_ip_prot_obp_dhcpv4_option = TextField(column_name='@voIpProt.OBP.dhcpv4.option', null=True)
    _vo_ip_prot_obp_dhcpv4_type = TextField(column_name='@voIpProt.OBP.dhcpv4.type', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voIpProt.OBP.dhcpv4'

class VoIpProtobpdhcpv6(BaseModel):
    _vo_ip_prot_obp_dhcpv6_option = TextField(column_name='@voIpProt.OBP.dhcpv6.option', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voIpProt.OBP.dhcpv6'

class VoIpProtsipspecialEventcheckSync(BaseModel):
    _vo_ip_prot_sip_special_event_check_sync_always_reboot = TextField(column_name='@voIpProt.SIP.specialEvent.checkSync.alwaysReboot', null=True)
    _vo_ip_prot_sip_special_event_check_sync_download_call_list = TextField(column_name='@voIpProt.SIP.specialEvent.checkSync.downloadCallList', null=True)
    _vo_ip_prot_sip_special_event_check_sync_download_directory = TextField(column_name='@voIpProt.SIP.specialEvent.checkSync.downloadDirectory', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voIpProt.SIP.specialEvent.checkSync'

class VoIpProtserverdhcp(BaseModel):
    _vo_ip_prot_server_dhcp_available = TextField(column_name='@voIpProt.server.dhcp.available', null=True)
    _vo_ip_prot_server_dhcp_option = TextField(column_name='@voIpProt.server.dhcp.option', null=True)
    _vo_ip_prot_server_dhcp_type = TextField(column_name='@voIpProt.server.dhcp.type', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voIpProt.server.dhcp'

class Voice(BaseModel):
    _voice_plc_cn_enable = TextField(column_name='@voice.plcCnEnable', null=True)
    _voice_plc_cn_gain = TextField(column_name='@voice.plcCnGain', null=True)
    _voice_rx_packet_filter = TextField(column_name='@voice.rxPacketFilter', null=True)
    _voice_tx_packet_delay = TextField(column_name='@voice.txPacketDelay', null=True)
    _voice_tx_packet_filter = TextField(column_name='@voice.txPacketFilter', null=True)
    _voice_vad_enable = TextField(column_name='@voice.vadEnable', null=True)
    _voice_vad_rx_gain = TextField(column_name='@voice.vadRxGain', null=True)
    _voice_vad_thresh = TextField(column_name='@voice.vadThresh', null=True)
    _voice_vad_tx_gain = TextField(column_name='@voice.vadTxGain', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice'

class VoiceaudioProfileOpus(BaseModel):
    _voice_audio_profile__opus__bit_rate = TextField(column_name='@voice.audioProfile.Opus.BitRate', null=True)
    _voice_audio_profile__opus__bitrate_mode = TextField(column_name='@voice.audioProfile.Opus.BitrateMode', null=True)
    _voice_audio_profile__opus__complexity = TextField(column_name='@voice.audioProfile.Opus.Complexity', null=True)
    _voice_audio_profile__opus_dt_xset = TextField(column_name='@voice.audioProfile.Opus.DTXset', null=True)
    _voice_audio_profile__opus_ls_bdepth = TextField(column_name='@voice.audioProfile.Opus.LSBdepth', null=True)
    _voice_audio_profile__opus__max_bandwidth = TextField(column_name='@voice.audioProfile.Opus.MaxBandwidth', null=True)
    _voice_audio_profile__opus__max_capture_rate = TextField(column_name='@voice.audioProfile.Opus.MaxCaptureRate', null=True)
    _voice_audio_profile__opus__max_p_time = TextField(column_name='@voice.audioProfile.Opus.MaxPTime', null=True)
    _voice_audio_profile__opus__min_p_time = TextField(column_name='@voice.audioProfile.Opus.MinPTime', null=True)
    _voice_audio_profile__opus__packet_loss_percentage = TextField(column_name='@voice.audioProfile.Opus.PacketLossPercentage', null=True)
    _voice_audio_profile__opus__sample_rate = TextField(column_name='@voice.audioProfile.Opus.SampleRate', null=True)
    _voice_audio_profile__opus_app_type = TextField(column_name='@voice.audioProfile.Opus.appType', null=True)
    _voice_audio_profile__opus_num_of_channels = TextField(column_name='@voice.audioProfile.Opus.numOfChannels', null=True)
    _voice_audio_profile__opus_p_time = TextField(column_name='@voice.audioProfile.Opus.pTime', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.Opus'

class VoiceaudioProfilesilk(BaseModel):
    _voice_audio_profile_silk__max_p_time = TextField(column_name='@voice.audioProfile.SILK.MaxPTime', null=True)
    _voice_audio_profile_silk__min_p_time = TextField(column_name='@voice.audioProfile.SILK.MinPTime', null=True)
    _voice_audio_profile_silk_enc_complexity = TextField(column_name='@voice.audioProfile.SILK.encComplexity', null=True)
    _voice_audio_profile_silk_enc_dtx_enable = TextField(column_name='@voice.audioProfile.SILK.encDTXEnable', null=True)
    _voice_audio_profile_silk_enc_expected_pkt_loss_percent = TextField(column_name='@voice.audioProfile.SILK.encExpectedPktLossPercent', null=True)
    _voice_audio_profile_silk_enc_inband_fec_enable = TextField(column_name='@voice.audioProfile.SILK.encInbandFECEnable', null=True)
    _voice_audio_profile_silk_p_time = TextField(column_name='@voice.audioProfile.SILK.pTime', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.SILK'

class VoiceaudioProfilesilk12Ksps(BaseModel):
    _voice_audio_profile_silk_12ksps_enc_max_avg_bitrate_kbps = TextField(column_name='@voice.audioProfile.SILK.12ksps.encMaxAvgBitrateKbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.SILK.12ksps'

class VoiceaudioProfilesilk16Ksps(BaseModel):
    _voice_audio_profile_silk_16ksps_enc_max_avg_bitrate_kbps = TextField(column_name='@voice.audioProfile.SILK.16ksps.encMaxAvgBitrateKbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.SILK.16ksps'

class VoiceaudioProfilesilk24Ksps(BaseModel):
    _voice_audio_profile_silk_24ksps_enc_max_avg_bitrate_kbps = TextField(column_name='@voice.audioProfile.SILK.24ksps.encMaxAvgBitrateKbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.SILK.24ksps'

class VoiceaudioProfilesilk8Ksps(BaseModel):
    _voice_audio_profile_silk_8ksps_enc_max_avg_bitrate_kbps = TextField(column_name='@voice.audioProfile.SILK.8ksps.encMaxAvgBitrateKbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.audioProfile.SILK.8ksps'

class Voicecnhs(BaseModel):
    _voice_cn_hs_attn = TextField(column_name='@voice.cn.hs.attn', null=True)
    _voice_cn_hs_enable = TextField(column_name='@voice.cn.hs.enable', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.cn.hs'

class VoicecodecPref(BaseModel):
    _voice_codec_pref_g711_a = TextField(column_name='@voice.codecPref.G711_A', null=True)
    _voice_codec_pref_g711_mu = TextField(column_name='@voice.codecPref.G711_Mu', null=True)
    _voice_codec_pref_g722 = TextField(column_name='@voice.codecPref.G722', null=True)
    _voice_codec_pref_g729_ab = TextField(column_name='@voice.codecPref.G729_AB', null=True)
    _voice_codec_pref__opus = TextField(column_name='@voice.codecPref.Opus', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref'

class VoicecodecPrefg719(BaseModel):
    _voice_codec_pref_g719_32kbps = TextField(column_name='@voice.codecPref.G719.32kbps', null=True)
    _voice_codec_pref_g719_48kbps = TextField(column_name='@voice.codecPref.G719.48kbps', null=True)
    _voice_codec_pref_g719_64kbps = TextField(column_name='@voice.codecPref.G719.64kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.G719'

class VoicecodecPrefg7221(BaseModel):
    _voice_codec_pref_g7221_16kbps = TextField(column_name='@voice.codecPref.G7221.16kbps', null=True)
    _voice_codec_pref_g7221_24kbps = TextField(column_name='@voice.codecPref.G7221.24kbps', null=True)
    _voice_codec_pref_g7221_32kbps = TextField(column_name='@voice.codecPref.G7221.32kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.G7221'

class VoicecodecPrefg7221C(BaseModel):
    _voice_codec_pref_g7221_c_24kbps = TextField(column_name='@voice.codecPref.G7221_C.24kbps', null=True)
    _voice_codec_pref_g7221_c_32kbps = TextField(column_name='@voice.codecPref.G7221_C.32kbps', null=True)
    _voice_codec_pref_g7221_c_48kbps = TextField(column_name='@voice.codecPref.G7221_C.48kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.G7221_C'

class VoicecodecPrefLin16(BaseModel):
    _voice_codec_pref__lin16_16ksps = TextField(column_name='@voice.codecPref.Lin16.16ksps', null=True)
    _voice_codec_pref__lin16_32ksps = TextField(column_name='@voice.codecPref.Lin16.32ksps', null=True)
    _voice_codec_pref__lin16_44_1ksps = TextField(column_name='@voice.codecPref.Lin16.44_1ksps', null=True)
    _voice_codec_pref__lin16_48ksps = TextField(column_name='@voice.codecPref.Lin16.48ksps', null=True)
    _voice_codec_pref__lin16_8ksps = TextField(column_name='@voice.codecPref.Lin16.8ksps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.Lin16'

class VoicecodecPrefsilk(BaseModel):
    _voice_codec_pref_silk_12ksps = TextField(column_name='@voice.codecPref.SILK.12ksps', null=True)
    _voice_codec_pref_silk_16ksps = TextField(column_name='@voice.codecPref.SILK.16ksps', null=True)
    _voice_codec_pref_silk_24ksps = TextField(column_name='@voice.codecPref.SILK.24ksps', null=True)
    _voice_codec_pref_silk_8ksps = TextField(column_name='@voice.codecPref.SILK.8ksps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.SILK'

class VoicecodecPrefSiren14(BaseModel):
    _voice_codec_pref__siren14_24kbps = TextField(column_name='@voice.codecPref.Siren14.24kbps', null=True)
    _voice_codec_pref__siren14_32kbps = TextField(column_name='@voice.codecPref.Siren14.32kbps', null=True)
    _voice_codec_pref__siren14_48kbps = TextField(column_name='@voice.codecPref.Siren14.48kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.Siren14'

class VoicecodecPrefSiren22(BaseModel):
    _voice_codec_pref__siren22_32kbps = TextField(column_name='@voice.codecPref.Siren22.32kbps', null=True)
    _voice_codec_pref__siren22_48kbps = TextField(column_name='@voice.codecPref.Siren22.48kbps', null=True)
    _voice_codec_pref__siren22_64kbps = TextField(column_name='@voice.codecPref.Siren22.64kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.Siren22'

class VoicecodecPrefSiren7(BaseModel):
    _voice_codec_pref__siren7_16kbps = TextField(column_name='@voice.codecPref.Siren7.16kbps', null=True)
    _voice_codec_pref__siren7_24kbps = TextField(column_name='@voice.codecPref.Siren7.24kbps', null=True)
    _voice_codec_pref__siren7_32kbps = TextField(column_name='@voice.codecPref.Siren7.32kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.Siren7'

class VoicecodecPrefiLbc(BaseModel):
    _voice_codec_pref_i_lbc_13_33kbps = TextField(column_name='@voice.codecPref.iLBC.13_33kbps', null=True)
    _voice_codec_pref_i_lbc_15_2kbps = TextField(column_name='@voice.codecPref.iLBC.15_2kbps', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.codecPref.iLBC'

class VoicerxQos(BaseModel):
    _voice_rx_qos_avg_jitter = TextField(column_name='@voice.rxQos.avgJitter', null=True)
    _voice_rx_qos_max_jitter = TextField(column_name='@voice.rxQos.maxJitter', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.rxQos'

class VoicerxQosmr(BaseModel):
    _voice_rx_qos_mr_avg_jitter = TextField(column_name='@voice.rxQos.mr.avgJitter', null=True)
    _voice_rx_qos_mr_max_jitter = TextField(column_name='@voice.rxQos.mr.maxJitter', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.rxQos.mr'

class VoicerxQosptt(BaseModel):
    _voice_rx_qos_ptt_avg_jitter = TextField(column_name='@voice.rxQos.ptt.avgJitter', null=True)
    _voice_rx_qos_ptt_max_jitter = TextField(column_name='@voice.rxQos.ptt.maxJitter', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.rxQos.ptt'

class VoicerxQoswireless(BaseModel):
    _voice_rx_qos_wireless_avg_jitter = TextField(column_name='@voice.rxQos.wireless.avgJitter', null=True)
    _voice_rx_qos_wireless_max_jitter = TextField(column_name='@voice.rxQos.wireless.maxJitter', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.rxQos.wireless'

class Voicevad(BaseModel):
    _voice_vad_signal_annex_b = TextField(column_name='@voice.vad.signalAnnexB', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.vad'

class Voicevolumepersist(BaseModel):
    _voice_volume_persist_handset = TextField(column_name='@voice.volume.persist.handset', null=True)
    _voice_volume_persist_handsfree = TextField(column_name='@voice.volume.persist.handsfree', null=True)
    _voice_volume_persist_headset = TextField(column_name='@voice.volume.persist.headset', null=True)
    _voice_volume_persist_usb_headset = TextField(column_name='@voice.volume.persist.usbHeadset', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.volume.persist'

class Voicevolumepersistbluetooth(BaseModel):
    _voice_volume_persist_bluetooth_headset = TextField(column_name='@voice.volume.persist.bluetooth.headset', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.volume.persist.bluetooth'

class Voicevolumepersistusb(BaseModel):
    _voice_volume_persist_usb_handsfree = TextField(column_name='@voice.volume.persist.usb.handsfree', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'voice.volume.persist.usb'

class Webutilitylanguage(BaseModel):
    _webutility_language_plcm_server_url = TextField(column_name='@webutility.language.plcmServerUrl', null=True)
    client = ForeignKeyField(column_name='ClientID', field='id', model=Client, null=True)
    expansion = ForeignKeyField(column_name='ExpansionID', field='id', model=Expansion, null=True)
    id = AutoField(column_name='ID')
    phone = ForeignKeyField(column_name='PhoneID', field='id', model=Phone, null=True)
    site = ForeignKeyField(column_name='SiteID', field='id', model=Site, null=True)

    class Meta:
        table_name = 'webutility.language'


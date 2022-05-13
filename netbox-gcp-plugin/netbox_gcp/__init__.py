from extras.plugins import PluginConfig


class NetBoxGcpConfig(PluginConfig):
    name = 'netbox_gcp'
    verbose_name = ' NetBox GCP'
    description = 'GCP NetBox ingegration'
    version = '0.1'
    base_url = 'netbox_gcp'


config = NetBoxGcpConfig

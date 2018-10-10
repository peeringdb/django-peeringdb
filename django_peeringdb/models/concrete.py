
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_peeringdb import settings
from django_peeringdb.models import (
    OrganizationBase,
    FacilityBase,
    NetworkBase,
    InternetExchangeBase,
    InternetExchangeFacilityBase,
    IXLanBase,
    IXLanPrefixBase,
    ContactBase,
    NetworkFacilityBase,
    NetworkIXLanBase,
)


all_models = []
tag_dict = {}

def expose_model(cls):
    all_models.append(cls)
    tag_dict[cls._handleref.tag] = cls
    return cls

class URLField(models.URLField):
    """
    local defaults for URLField
    """
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        super(URLField, self).__init__(*args, **kwargs)

@expose_model
class Organization(OrganizationBase):
    pass

@expose_model
class Facility(FacilityBase):
    org = models.ForeignKey(Organization, related_name="fac_set",
                            verbose_name=_('organization'),
                            on_delete=models.CASCADE)

@expose_model
class Network(NetworkBase):
    org = models.ForeignKey(Organization, related_name="net_set",
                            verbose_name=_('organization'),
                            on_delete=models.CASCADE)


@expose_model
class InternetExchange(InternetExchangeBase):
    org = models.ForeignKey(Organization, related_name="ix_set",
                            verbose_name=_('organization'),
                            on_delete=models.CASCADE)

    @property
    def fac_set(self):
        return [ixfac.fac for ixfac in self.ixfac_set]

@expose_model
class InternetExchangeFacility(InternetExchangeFacilityBase):
    ix = models.ForeignKey(InternetExchange, related_name="ixfac_set",
                           verbose_name=_('internet exchange'),
                           on_delete=models.CASCADE)
    fac = models.ForeignKey(Facility, default=0, related_name="ixfac_set",
                            verbose_name=_('facility'),
                            on_delete=models.CASCADE)

    class Meta(InternetExchangeFacilityBase.Meta):
        unique_together = ('ix', 'fac')
        db_table = '%six_facility' % settings.TABLE_PREFIX

    def __str__(self):
        return '{} at {}'.format(self.ix, self.fac)

@expose_model
class IXLan(IXLanBase):
    ix = models.ForeignKey(InternetExchange, default=0, related_name="ixlan_set",
                           verbose_name=_('internet exchange'),
                           on_delete=models.CASCADE)

    def __str__(self):
        return '{} LAN for {}'.format(self.name, self.ix)


@expose_model
class IXLanPrefix(IXLanPrefixBase):
    ixlan = models.ForeignKey(IXLan, default=0, related_name="ixpfx_set",
                              verbose_name=_('internet exchange LAN'),
                              on_delete=models.CASCADE)

@expose_model
class NetworkContact(ContactBase):
    net = models.ForeignKey(Network, default=0, related_name="poc_set",
                            verbose_name=_('network'),
                            on_delete=models.CASCADE)

    def __str__(self):
        return '{} contact for {}'.format(self.role, self.net)

@expose_model
class NetworkFacility(NetworkFacilityBase):
    net = models.ForeignKey(Network, default=0, related_name="netfac_set",
                            verbose_name=_('network'),
                            on_delete=models.CASCADE)
    fac = models.ForeignKey(Facility, default=0, related_name="netfac_set",
                            verbose_name=_('facility'),
                            on_delete=models.CASCADE)

    class Meta(NetworkFacilityBase.Meta):
        unique_together = ('net', 'fac', 'local_asn')
        db_table = '%snetwork_facility' % settings.TABLE_PREFIX

    def __str__(self):
        return '{} at {}'.format(self.net, self.fac)

@expose_model
class NetworkIXLan(NetworkIXLanBase):
    net = models.ForeignKey(Network, default=0, related_name="netixlan_set",
                            verbose_name=_('network'),
                            on_delete=models.CASCADE)
    ixlan = models.ForeignKey(IXLan, default=0, related_name="netixlan_set",
                              verbose_name=_('internet exchange LAN'),
                              on_delete=models.CASCADE)

    def __str__(self):
        return '{} at {}'.format(self.net, self.ixlan)

__all__ = [m.__name__ for m in all_models]
# other required vars
__all__.append('all_models')
__all__.append('tag_dict')


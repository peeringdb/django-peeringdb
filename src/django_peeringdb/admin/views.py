from django.contrib import admin

from django_peeringdb.models import (
    Facility,
    InternetExchange,
    InternetExchangeFacility,
    IXLan,
    IXLanPrefix,
    Network,
    NetworkContact,
    NetworkFacility,
    NetworkIXLan,
    Organization,
)


class HandleRefAdminMixIn:
    """Dummy MixIn that just hides HandleRef's fields."""

    exclude = ("status", "version")


class ModelAdminBase(HandleRefAdminMixIn, admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        """Make everything read-only, as this is PeeringDB's data."""
        return False


# Organization view
class NetworkInline(HandleRefAdminMixIn, admin.TabularInline):
    model = Network
    fields = ("asn", "name", "aka")
    show_change_link = True


@admin.register(Organization)
class OrganizationAdmin(ModelAdminBase):
    search_fields = ("name",)
    list_display = ("name", "website")
    inlines = [
        NetworkInline,
    ]


# Facility view
@admin.register(Facility)
class FacilityAdmin(ModelAdminBase):
    search_fields = ("name", "address1")
    list_display = ("name", "org", "city", "address1")


# Network views
class NetworkContactInline(HandleRefAdminMixIn, admin.TabularInline):
    model = NetworkContact


class NetworkFacilityInline(HandleRefAdminMixIn, admin.TabularInline):
    model = NetworkFacility


class NetworkIXLanInline(HandleRefAdminMixIn, admin.TabularInline):
    model = NetworkIXLan


@admin.register(Network)
class NetworkAdmin(ModelAdminBase):
    search_fields = ("name", "aka", "asn")
    list_display = ("name", "aka", "asn")
    inlines = [
        NetworkFacilityInline,
        NetworkContactInline,
        NetworkIXLanInline,
    ]


# IX views
class IXLanInline(HandleRefAdminMixIn, admin.StackedInline):
    model = IXLan
    show_change_link = True


class InternetExchangeFacilityInline(HandleRefAdminMixIn, admin.TabularInline):
    model = InternetExchangeFacility


@admin.register(InternetExchange)
class InternetExchangeAdmin(ModelAdminBase):
    search_fields = (
        "name",
        "name_long",
    )
    list_display = ("name", "name_long", "city")
    inlines = [
        InternetExchangeFacilityInline,
        IXLanInline,
    ]


# IXLan views
class IXLanPrefixInline(HandleRefAdminMixIn, admin.StackedInline):
    model = IXLanPrefix


@admin.register(IXLan)
class IXLanAdmin(ModelAdminBase):
    search_fields = ("name", "ix__name")
    list_display = ("__str__", "ix")
    inlines = [
        IXLanPrefixInline,
    ]

# #1742: netixlan status absorbs operational-ness.
#
# status gains the value "not-operational"; existing non-operational rows are
# migrated from the boolean. Scoped to status="ok" on purpose -- pending and
# deleted rows keep their lifecycle status regardless of the boolean, otherwise
# the migration would resurrect deleted connections.
#
# The `operational` boolean stays writable at the model level for now; it
# becomes read-only at the API layer (server-side serializer) and is dropped
# from the schema in a later release, after the announced deprecation window.

from django.db import migrations


def forwards(apps, schema_editor):
    # _default_manager: on historical models the only manager kept is the
    # first-declared one (handleref), so there is no `objects` here.
    NetworkIXLan = apps.get_model("django_peeringdb", "NetworkIXLan")
    NetworkIXLan._default_manager.filter(status="ok", operational=False).update(
        status="not-operational"
    )


def backwards(apps, schema_editor):
    NetworkIXLan = apps.get_model("django_peeringdb", "NetworkIXLan")
    # not-operational rows all came from status="ok" (see forwards); their
    # operational boolean was never touched, so this restores the exact
    # pre-migration state.
    NetworkIXLan._default_manager.filter(status="not-operational").update(status="ok")


class Migration(migrations.Migration):
    dependencies = [
        ("django_peeringdb", "0041_network_meta_networkixlan_meta"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]

from io import StringIO

from django.core.management import call_command


def test_pdb_sync_removed_message():
    # pdb_sync no longer syncs; it only prints a removal/redirect notice
    out = StringIO()
    call_command("pdb_sync", stdout=out)
    output = out.getvalue()
    assert "has been removed" in output
    assert "peeringdb client" in output

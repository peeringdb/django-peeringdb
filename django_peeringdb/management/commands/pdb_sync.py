from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            "In an effort to split sync logic from schema definition, the pdb_sync functionality has been removed from this module."
        )
        self.stdout.write("")
        self.stdout.write(
            "Use the peeringdb client to sync your database going forward."
        )
        self.stdout.write("")
        self.stdout.write("Please find instructions on how to do so at: ")
        self.stdout.write(
            "https://github.com/peeringdb/django-peeringdb/blob/master/docs/sync.md"
        )

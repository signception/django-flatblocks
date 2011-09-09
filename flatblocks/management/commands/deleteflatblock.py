from django.core.management import BaseCommand, CommandError
from django.conf import settings
from django.contrib.sites.models import Site

from flatblocks.models import FlatBlock


class Command(BaseCommand):
    help = "Delete a flatblock with the given slug and optional LANGUAGE_CODE and SITE_ID"

    def handle(self, *args, **options):
        if len(args) == 0 or len(args) > 3:
            raise CommandError, "arguments: slug [LANGUAGE_CODE] [SITE_ID]"

        slug = args[0]
        
        if len(args) >= 2:
            lang = args[1]
        else:
            lang = settings.LANGUAGE_CODE

        if len(args) >= 3:
            site = Site.objects.get(id=args[2])
        else:
            site = Site.objects.get_current()

        try:
            FlatBlock.objects.get(slug=slug, lang_code=lang, site=site).delete()
        except FlatBlock.DoesNotExist, e:
            raise CommandError, "The requested flatblock doesn't exist"


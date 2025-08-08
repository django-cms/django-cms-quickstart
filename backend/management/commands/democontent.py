import os
import json

from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cms.api import create_page
from cms.models.contentmodels import PageContent
from cms.constants import TEMPLATE_INHERITANCE_MAGIC

from djangocms_transfer.importer import import_plugins_to_page
from djangocms_transfer.datastructures import ArchivedPlaceholder, ArchivedPlugin


LANGUAGE = "en"
DEMOCONTENT = settings.BASE_DIR / "democontent"
User = get_user_model()


class Command(BaseCommand):
    help = "Create Demo content."

    def add_arguments(self, parser):
        parser.add_argument(
            "filepath", metavar="FILE_PATH", nargs="?", help="Input file to load from."
        )
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            dest="force",
            help="Force add page to the page tree."
        )

    def _page_create_details(self) -> dict:
        user, created = User.objects.get_or_create(username="demo")
        if created:
            self.stdout.write("User with username, 'demo' created")

        return {
            "title": f"{self.title.title()}",
            "template": TEMPLATE_INHERITANCE_MAGIC,
            "created_by": user,
            "in_navigation": True,
            "language": LANGUAGE,
        }

    def loaddata(self, abs_filepath):
        def parse_data(data):
            if not data:
                return data
            if "plugins" in data:
                return ArchivedPlaceholder(
                    slot=data["placeholder"],
                    plugins=data["plugins"],
                )
            if "plugin_type" in data:
                return ArchivedPlugin(**data)
            return data

        with abs_filepath.open() as fixture:
            try:
                placeholders: list = json.loads(fixture.read(), object_hook=parse_data)

                # create page and get pagecontent
                page = create_page(**self._page_create_details())
                page_content = page.get_admin_content(language=LANGUAGE)

                # import plugin to page
                import_plugins_to_page(
                    placeholders=placeholders,
                    pagecontent=page_content,
                    language=LANGUAGE,
                )
            except Exception as e:
                e.args = (f"Problem installing fixture {fixture}: {e}",)
                raise

    def handle(self, *args, **options):
        filepath = options["filepath"]
        force = options["force"]

        if not filepath:
            for file in DEMOCONTENT.iterdir():
                self.stdout.write("---> %s" % file.name)
            return

        file = os.path.basename(filepath)
        self.title = file.split(".")[0]

        # skip title check if force option is provided
        if not force:
            all_page_content = PageContent.admin_manager.all()
            for page_content in all_page_content:
                if page_content.title.lower() == self.title.lower():
                    self.stdout.write(
                        "Page with title('%s') already exists" % self.title
                    )
                    return

        abs_filepath = DEMOCONTENT / file
        with transaction.atomic():
            self.loaddata(abs_filepath)

        self.stdout.write("Page with title('%s') created" % self.title)

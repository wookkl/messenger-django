from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models


class Command(BaseCommand):

    help = "This command generated users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default=1, type=int, help="How many users do you wanna create?"
        )

    def handle(self, *args, **options):
        number = int(options.get("--numbers", 1))
        seeder = Seed.seeder()
        seeder.add_entity(
            user_models.User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
                "bio": seeder.faker.text(),
                "avatar": None,
                "username": seeder.faker.email(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} user's created successfully!"))

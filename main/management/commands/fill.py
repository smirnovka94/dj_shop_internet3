from django.core.management import BaseCommand
from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Одежда', 'description': 'Товары для дома'},
            {'name': 'Строительная техника', 'description': ',Крупное бензооборудование'},
            {'name': 'Книги', 'description': 'Товары образования и досуга'},
        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)
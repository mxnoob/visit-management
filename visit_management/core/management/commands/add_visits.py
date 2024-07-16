import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Worker, Shop, Visit

fake = Faker()


def create_workers(count: int):
    workers = [
        Worker(name=fake.name(), phone_number=fake.phone_number())
        for _ in range(count)
    ]
    [worker.save() for worker in workers]
    return workers


def create_shops(workers, count: int):
    shops = [
        Shop(name=fake.company(), worker=random.choice(workers))
        for _ in range(count)
    ]
    [shop.save() for shop in shops]
    return shops


def create_visits(workers, shops, count: int):
    visits = [
        Visit(
            shop=random.choice(shops),
            worker=random.choice(workers),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
        )
        for _ in range(count)
    ]
    [visit.save() for visit in visits]
    return visits


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--workers",
            type=int,
            default=5,
            help="Number of workers",
        )
        parser.add_argument(
            "--shops",
            type=int,
            default=25,
            help="Number of shops",
        )
        parser.add_argument(
            "--visits",
            type=int,
            default=100,
            help="Number of visits",
        )

    def handle(self, *args, **options):
        workers = create_workers(options["workers"])
        shops = create_shops(workers, options["shops"])
        create_visits(workers, shops, options["visits"])
        self.stdout.write(self.style.SUCCESS("Done"))

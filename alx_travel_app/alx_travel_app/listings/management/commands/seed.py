from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "name": "Luxury Beachside Villa",
                "description": "A beautiful villa by the beach.",
                "price_per_night": 300.00,
                "location": "Miami, Florida",
            },
            {
                "name": "Cozy Mountain Cabin",
                "description": "A cozy cabin in the mountains.",
                "price_per_night": 150.00,
                "location": "Aspen, Colorado",
            },
            {
                "name": "Modern City Apartment",
                "description": "A modern apartment in the heart of the city.",
                "price_per_night": 200.00,
                "location": "New York City, New York",
            },
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings data."))

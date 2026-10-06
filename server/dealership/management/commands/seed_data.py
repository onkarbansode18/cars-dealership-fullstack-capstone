import json
import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dealership.models import Dealership, Review, CarMake, CarModel

class Command(BaseCommand):
    help = 'Seed initial dealership, car, and review data'

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent.parent
        data_dir = base_dir / 'data'

        # Seed Superuser / Admin
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created successfully with password 'admin123'."))

        # Seed Test User for evidence
        if not User.objects.filter(username='testuser').exists():
            u = User.objects.create_user('testuser', 'testuser@example.com', 'password123')
            u.first_name = 'Test'
            u.last_name = 'User'
            u.save()
            self.stdout.write(self.style.SUCCESS("Test user 'testuser' created successfully."))

        # Seed Dealers
        dealers_file = data_dir / 'dealers.json'
        if dealers_file.exists():
            with open(dealers_file, 'r', encoding='utf-8') as f:
                dealers_data = json.load(f)
                for item in dealers_data:
                    Dealership.objects.update_or_create(
                        dealer_id=item['id'],
                        defaults={
                            'name': item['name'],
                            'city': item['city'],
                            'state': item['state'],
                            'address': item['address'],
                            'zip': item['zip'],
                            'phone': item.get('phone', ''),
                            'website': item.get('website', ''),
                            'image': item.get('image', ''),
                            'description': item.get('description', '')
                        }
                    )
            self.stdout.write(self.style.SUCCESS(f"Seeded {len(dealers_data)} dealerships."))

        # Seed Cars
        cars_file = data_dir / 'cars.json'
        if cars_file.exists():
            with open(cars_file, 'r', encoding='utf-8') as f:
                cars_data = json.load(f)
                for item in cars_data:
                    make_obj, _ = CarMake.objects.get_or_create(
                        name=item['make'],
                        defaults={'description': f"{item['make']} Automobiles", 'country': 'Global'}
                    )
                    CarModel.objects.get_or_create(
                        car_make=make_obj,
                        name=item['model'],
                        defaults={'type': item.get('type', 'Sedan'), 'year': item.get('year', 2024)}
                    )
            self.stdout.write(self.style.SUCCESS(f"Seeded cars data."))

        # Seed Reviews
        reviews_file = data_dir / 'reviews.json'
        if reviews_file.exists():
            with open(reviews_file, 'r', encoding='utf-8') as f:
                reviews_data = json.load(f)
                for item in reviews_data:
                    dealer_obj = Dealership.objects.filter(dealer_id=item['dealer_id']).first()
                    if dealer_obj:
                        Review.objects.get_or_create(
                            dealer=dealer_obj,
                            name=item['name'],
                            review=item['review'],
                            defaults={
                                'purchase': item.get('purchase', True),
                                'purchase_date': item.get('purchase_date', None),
                                'car_make': item.get('car_make', ''),
                                'car_model': item.get('car_model', ''),
                                'car_year': item.get('car_year', None),
                                'sentiment': item.get('sentiment', 'positive')
                            }
                        )
            self.stdout.write(self.style.SUCCESS(f"Seeded reviews data."))

from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Coupe', 'Coupe'),
        ('Truck', 'Truck'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=CAR_TYPES, default='Sedan')
    year = models.IntegerField(default=2024)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

class Dealership(models.Model):
    dealer_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

class Review(models.Model):
    dealer = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=150)
    review = models.TextField()
    purchase = models.BooleanField(default=True)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    car_year = models.IntegerField(null=True, blank=True)
    sentiment = models.CharField(max_length=50, default='neutral')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} for {self.dealer.name}"

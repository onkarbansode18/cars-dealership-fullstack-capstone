from rest_framework import serializers
from .models import CarMake, CarModel, Dealership, Review

class CarModelSerializer(serializers.ModelSerializer):
    make_name = serializers.CharField(source='car_make.name', read_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'type', 'year', 'make_name']

class CarMakeSerializer(serializers.ModelSerializer):
    models = CarModelSerializer(many=True, read_only=True)

    class Meta:
        model = CarMake
        fields = ['id', 'name', 'description', 'country', 'models']

class DealershipSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='dealer_id', read_only=True)

    class Meta:
        model = Dealership
        fields = ['id', 'dealer_id', 'name', 'city', 'state', 'address', 'zip', 'phone', 'website', 'image', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    dealer_id = serializers.IntegerField(source='dealer.dealer_id', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'dealer_id', 'name', 'review', 'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year', 'sentiment', 'created_at']

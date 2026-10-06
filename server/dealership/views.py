import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Dealership, Review, CarMake, CarModel
from .serializers import DealershipSerializer, ReviewSerializer, CarMakeSerializer
from .sentiment import analyze_sentiment

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers(request):
    state = request.GET.get('state', None)
    if state:
        dealers = Dealership.objects.filter(state__iexact=state)
    else:
        dealers = Dealership.objects.all()
    serializer = DealershipSerializer(dealers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request, dealer_id):
    try:
        dealer = Dealership.objects.get(dealer_id=dealer_id)
        serializer = DealershipSerializer(dealer)
        return Response(serializer.data)
    except Dealership.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_reviews(request, dealer_id):
    try:
        dealer = Dealership.objects.get(dealer_id=dealer_id)
        reviews = Review.objects.filter(dealer=dealer).order_by('-created_at')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Dealership.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_review(request, dealer_id):
    try:
        dealer = Dealership.objects.get(dealer_id=dealer_id)
    except Dealership.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    review_text = data.get('review', '')
    if not review_text:
        return Response({'error': 'Review text is required'}, status=status.HTTP_400_BAD_REQUEST)

    user_name = data.get('name', '')
    if not user_name and request.user.is_authenticated:
        user_name = request.user.username
    elif not user_name:
        user_name = 'Anonymous'

    sentiment = analyze_sentiment(review_text)

    review_obj = Review.objects.create(
        dealer=dealer,
        name=user_name,
        review=review_text,
        purchase=data.get('purchase', True),
        purchase_date=data.get('purchase_date', None),
        car_make=data.get('car_make', ''),
        car_model=data.get('car_model', ''),
        car_year=data.get('car_year', None),
        sentiment=sentiment
    )

    serializer = ReviewSerializer(review_obj)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_cars(request):
    makes = CarMake.objects.all()
    serializer = CarMakeSerializer(makes, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data if request.data else json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    email = data.get('email', '')

    if not username or not password:
        return JsonResponse({'status': 'Failed', 'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'status': 'Failed', 'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.save()
    login(request, user)
    return JsonResponse({'status': 'Authenticated', 'username': username, 'message': 'User registered successfully'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data if request.data else json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'Authenticated', 'username': username})
    else:
        return JsonResponse({'status': 'Failed', 'error': 'Invalid credentials'}, status=400)

@csrf_exempt
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def logout_user(request):
    logout(request)
    return JsonResponse({'status': 'Logged out', 'message': 'User logged out successfully'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def analyze_review_sentiment(request):
    data = request.data if request.data else json.loads(request.body)
    text = data.get('text', '') or data.get('review', '')
    sentiment = analyze_sentiment(text)
    return JsonResponse({'sentiment': sentiment, 'status': '200'})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'is_authenticated': True, 'username': request.user.username})
    return JsonResponse({'is_authenticated': False, 'username': ''})

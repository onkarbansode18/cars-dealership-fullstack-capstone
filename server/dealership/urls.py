from django.urls import path
from . import views

urlpatterns = [
    path('dealers/', views.get_dealers, name='get_dealers'),
    path('dealers/<int:dealer_id>/', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('dealers/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('dealers/<int:dealer_id>/add_review/', views.add_review, name='add_review'),
    path('cars/', views.get_cars, name='get_cars'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('analyze-review/', views.analyze_review_sentiment, name='analyze_review_sentiment'),
    path('user/', views.get_user_status, name='get_user_status'),
]

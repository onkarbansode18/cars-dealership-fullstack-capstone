from django.test import TestCase, Client
from django.contrib.auth.models import User
from dealership.models import Dealership, Review, CarMake, CarModel

class DealershipAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password123')
        self.dealer = Dealership.objects.create(
            dealer_id=1,
            name='Kansas City Motors',
            city='Kansas City',
            state='Kansas',
            address='1010 Grand Blvd',
            zip='64106',
            phone='816-555-0101',
            website='https://kcmotors.example.com',
            description='Test Kansas dealer'
        )
        self.carmake = CarMake.objects.create(name='Toyota', country='Japan')
        self.carmodel = CarModel.objects.create(car_make=self.carmake, name='Camry', type='Sedan', year=2024)

    def test_get_all_dealers(self):
        response = self.client.get('/api/dealers/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_get_dealer_by_id(self):
        response = self.client.get('/api/dealers/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Kansas City Motors')

    def test_get_dealers_by_state(self):
        response = self.client.get('/api/dealers/?state=Kansas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['state'], 'Kansas')

    def test_get_cars(self):
        response = self.client.get('/api/cars/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_sentiment_analysis_api(self):
        response = self.client.post(
            '/api/analyze-review/',
            data={'text': 'Fantastic services'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['sentiment'], 'positive')

    def test_user_registration(self):
        response = self.client.post(
            '/api/register/',
            data={
                'username': 'newuser',
                'first_name': 'New',
                'last_name': 'User',
                'email': 'newuser@example.com',
                'password': 'password123'
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'Authenticated')

    def test_user_login_logout(self):
        login_res = self.client.post(
            '/api/login/',
            data={'username': 'testuser', 'password': 'password123'},
            content_type='application/json'
        )
        self.assertEqual(login_res.status_code, 200)

        logout_res = self.client.post('/api/logout/')
        self.assertEqual(logout_res.status_code, 200)

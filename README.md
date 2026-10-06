# Cars Dealership Full-Stack Application

[![CI/CD Pipeline](https://github.com/USERNAME/cars-dealership-fullstack-capstone/actions/workflows/cicd.yml/badge.svg)](https://github.com/USERNAME/cars-dealership-fullstack-capstone/actions)

## Project Overview

A responsive full-stack dealership application for browsing dealers, viewing dealer details, reading/submitting reviews, and performing sentiment analysis. Developed for the IBM & Coursera Full-Stack Web Development Capstone Project.

The platform provides nationwide car buyers with branch lookup across U.S. states (including Kansas, Texas, California, New York, Illinois, and Florida), vehicle make and model browsing, user registration, authentication, review submission, and automated sentiment analysis on customer reviews.

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.11 / Django 4.2+ / Django REST Framework
- **Frontend Framework**: React 18 / Vite / Vanilla CSS (Responsive Layout)
- **Database**: SQLite3 (Production convertible to PostgreSQL/DB2)
- **Sentiment Analysis**: VADER / Lightweight Natural Language Processing
- **Containerization**: Docker & Docker Compose
- **CI/CD Automation**: GitHub Actions
- **Cloud Deployment**: IBM Cloud Code Engine / IBM Container Registry

---

## ✨ Features

- **Dealership Branch Listing**: Browse nationwide dealership locations with photos, contact numbers, address, and state metadata.
- **State Filtering**: Dynamically filter dealership branches by U.S. state (e.g. `Kansas`, `Texas`, `California`).
- **Dealer Detail View**: View dealership overview, location details, website links, and customer review lists.
- **User Authentication**: Complete registration, login, and logout workflows with session management.
- **Review Submission**: Authenticated users can post dealership reviews, purchase date, and vehicle specs.
- **Automated Sentiment Analysis**: Instant NLP sentiment scoring (`positive`, `neutral`, `negative`) for review text.
- **Car Makes & Models API**: REST endpoint returning automotive manufacturer and model classifications.
- **Django Administration**: Built-in Django Admin portal for managing dealerships, models, and customer reviews.
- **Automated CI/CD**: Workflow automation running unit tests, linting, and production frontend compilation on push.

---

## 📁 Project Structure

```
cars-dealership-capstone/
│
├── README.md
├── .gitignore
├── LICENSE
├── generate_screenshots.py
│
├── server/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── .env.example
│   │
│   ├── server/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── dealership/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── sentiment.py
│   │   └── tests.py
│   │
│   └── frontend/
│       ├── static/
│       │   ├── About.html
│       │   ├── Contact.html
│       │   └── css/style.css
│       └── src/
│           ├── components/
│           │   ├── Register/Register.jsx
│           │   ├── Login/Login.jsx
│           │   ├── Logout/Logout.jsx
│           │   ├── Dealers/Dealers.jsx
│           │   ├── Dealer/DealerDetail.jsx
│           │   ├── Review/AddReview.jsx
│           │   └── Navbar/Navbar.jsx
│           ├── App.jsx
│           └── index.css
│
├── data/
│   ├── dealers.json
│   ├── reviews.json
│   └── cars.json
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── evidence/
│   ├── django_server
│   ├── loginuser
│   ├── logoutuser
│   ├── getdealerreviews
│   ├── getalldealers
│   ├── getdealerbyid
│   ├── getdealersbyState
│   ├── getallcarmakes
│   ├── analyzereview
│   ├── CICD
│   └── deploymentURL
│
├── screenshots/
│   ├── admin_login.png
│   ├── admin_logout.png
│   ├── get_dealers.png
│   ├── get_dealers_loggedin.png
│   ├── dealersbystate.png
│   ├── dealer_id_reviews.png
│   ├── dealership_review_submission.png
│   ├── added_review.png
│   ├── deployed_landingpage.png
│   ├── deployed_loggedin.png
│   ├── deployed_dealer_detail.png
│   └── deployed_add_review.png
│
└── FINAL_SUBMISSION/
    ├── README.md
    ├── SUBMISSION_GUIDE.md
    ├── evidence/
    └── screenshots/
```

---

## 🚀 Local Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js 18+ & npm
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/USERNAME/cars-dealership-fullstack-capstone.git
cd cars-dealership-fullstack-capstone
```

### 2. Backend Setup
```bash
# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install Python requirements
pip install -r server/requirements.txt

# Run migrations and seed dataset
python server/manage.py makemigrations dealership
python server/manage.py migrate
python server/manage.py seed_data
```

### 3. Frontend Setup
```bash
cd server/frontend
npm install
npm run build
cd ../..
```

### 4. Run Development Server
```bash
python server/manage.py runserver 127.0.0.1:8000
```
Access the application at: `http://127.0.0.1:8000/`

---

## 🧪 Testing Instructions

Run the Django unit test suite:
```bash
python server/manage.py test dealership
```

---

## 🐳 Docker Setup

Build and run using Docker Compose:
```bash
docker-compose -f server/docker-compose.yml up --build
```
Access the containerized application at `http://localhost:8000/`.

---

## ☁️ Deployment Instructions (IBM Cloud Code Engine)

1. **Log in to IBM Cloud CLI**:
   ```bash
   ibmcloud login -a https://cloud.ibm.com -u <USER> -p <PASSWORD>
   ibmcloud cr login
   ```

2. **Build and Push Container Image**:
   ```bash
   docker build -t us.icr.io/<NAMESPACE>/cars-dealership-app:latest -f server/Dockerfile .
   docker push us.icr.io/<NAMESPACE>/cars-dealership-app:latest
   ```

3. **Deploy to IBM Cloud Code Engine**:
   ```bash
   ibmcloud ce application create --name cars-dealership --image us.icr.io/<NAMESPACE>/cars-dealership-app:latest --port 8000
   ```

---

## 📡 REST API Documentation

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/dealers/` | `GET` | Retrieve all dealerships (Optional query `?state=Kansas`) |
| `/api/dealers/<id>/` | `GET` | Retrieve dealership details by ID |
| `/api/dealers/<id>/reviews/` | `GET` | Retrieve reviews for a specific dealership |
| `/api/dealers/<id>/add_review/` | `POST` | Post a review for a dealership |
| `/api/cars/` | `GET` | Retrieve list of all car makes and models |
| `/api/register/` | `POST` | Register a new user |
| `/api/login/` | `POST` | User login |
| `/api/logout/` | `POST` | User logout |
| `/api/analyze-review/` | `POST` | Analyze review text sentiment (`positive`, `neutral`, `negative`) |
| `/api/user/` | `GET` | Get current authenticated user session status |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

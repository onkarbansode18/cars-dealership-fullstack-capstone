# Cars Dealership Capstone — Task 1–28 Submission Guide

## How to Use This Guide
- Replace `<YOUR_USERNAME>` with your GitHub username after pushing.
- Replace `<YOUR_REPO>` with the repository name (e.g. `cars-dealership-fullstack-capstone`).
- For tasks requiring file contents: **paste the file content directly** into the submission box.
- For tasks requiring GitHub URLs: **paste the full GitHub URL** shown below.
- For tasks requiring screenshots: **upload the PNG file** from `FINAL_SUBMISSION/screenshots/`.

---

## Task Submission Table

| Task # | Task Title | Submission Type | What to Submit |
|:------:|:-----------|:----------------|:---------------|
| **1** | GitHub Public README | GitHub URL | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/README.md` |
| **2** | Django Server Running Evidence | Text Content | Paste contents of `evidence/django_server` |
| **3** | About Us Page | GitHub URL | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/static/About.html` |
| **4** | Contact Us Page | GitHub URL | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/static/Contact.html` |
| **5** | Login User (curl evidence) | Text Content | Paste contents of `evidence/loginuser` |
| **6** | Logout User (curl evidence) | Text Content | Paste contents of `evidence/logoutuser` |
| **7** | Register Component | GitHub URL | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/src/components/Register/Register.jsx` |
| **8** | Get Dealer Reviews (curl evidence) | Text Content | Paste contents of `evidence/getdealerreviews` |
| **9** | Get All Dealers (curl evidence) | Text Content | Paste contents of `evidence/getalldealers` |
| **10** | Get Dealer by ID (curl evidence) | Text Content | Paste contents of `evidence/getdealerbyid` |
| **11** | Get Dealers by State (curl evidence) | Text Content | Paste contents of `evidence/getdealersbyState` |
| **12** | Admin Login Screenshot | Screenshot Upload | Upload `screenshots/admin_login.png` |
| **13** | Admin Logout Screenshot | Screenshot Upload | Upload `screenshots/admin_logout.png` |
| **14 & 15** | Get All Car Makes (curl evidence) | Text Content | Paste contents of `evidence/getallcarmakes` |
| **16** | Analyze Review Sentiment (curl evidence) | Text Content | Paste contents of `evidence/analyzereview` |
| **17** | Dealers Page Before Login (screenshot) | Screenshot Upload | Upload `screenshots/get_dealers.png` |
| **18** | Dealers Page Logged In (screenshot) | Screenshot Upload | Upload `screenshots/get_dealers_loggedin.png` |
| **19** | Dealers Filtered by State Kansas (screenshot) | Screenshot Upload | Upload `screenshots/dealersbystate.png` |
| **20** | Dealer ID + Reviews Page (screenshot) | Screenshot Upload | Upload `screenshots/dealer_id_reviews.png` |
| **21** | Review Submission Form (screenshot) | Screenshot Upload | Upload `screenshots/dealership_review_submission.png` |
| **22** | Added Review on Dealer Page (screenshot) | Screenshot Upload | Upload `screenshots/added_review.png` |
| **23** | CI/CD Pipeline Output | Text Content | Paste contents of `evidence/CICD` |
| **24** | Deployment URL | Text Content | Paste contents of `evidence/deploymentURL` |
| **25** | Deployed Landing Page (screenshot) | Screenshot Upload | Upload `screenshots/deployed_landingpage.png` |
| **26** | Deployed Logged-In Page (screenshot) | Screenshot Upload | Upload `screenshots/deployed_loggedin.png` |
| **27** | Deployed Dealer Detail Page (screenshot) | Screenshot Upload | Upload `screenshots/deployed_dealer_detail.png` |
| **28** | Deployed Added Review (screenshot) | Screenshot Upload | Upload `screenshots/deployed_add_review.png` |

---

## Text to Paste for Each Evidence Task

---

### TASK 2 — Django Server (paste this):
```
COMMAND:
python server/manage.py runserver 127.0.0.1:8000

OUTPUT:
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 06, 2026 - 18:28:35
Django version 6.1.2, using settings 'server.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

### TASK 5 — Login User (paste this):
```
COMMAND:
curl -X POST http://127.0.0.1:8000/api/login/ -H "Content-Type: application/json" -d "{\"username\": \"testuser\", \"password\": \"password123\"}"

OUTPUT:
{"status": "Authenticated", "username": "testuser"}
```

---

### TASK 6 — Logout User (paste this):
```
COMMAND:
curl -X POST http://127.0.0.1:8000/api/logout/

OUTPUT:
{"status": "Logged out", "message": "User logged out successfully"}
```

---

### TASK 8 — Get Dealer Reviews (paste this):
```
COMMAND:
curl http://127.0.0.1:8000/api/dealers/1/reviews/

OUTPUT:
[{"id":2,"dealer_id":1,"name":"Maria Garcia","review":"Great customer experience. The financing department was very transparent and fast.","purchase":true,"purchase_date":"2026-03-01","car_make":"Honda","car_model":"CR-V","car_year":2025,"sentiment":"positive","created_at":"2026-10-06T18:24:48.916089Z"},{"id":1,"dealer_id":1,"name":"Alex Johnson","review":"Fantastic services and extremely knowledgeable staff! Made buying my new SUV effortless.","purchase":true,"purchase_date":"2026-02-15","car_make":"Toyota","car_model":"RAV4","car_year":2024,"sentiment":"positive","created_at":"2026-10-06T18:24:48.826419Z"}]
```

---

### TASK 9 — Get All Dealers (paste this):
```
COMMAND:
curl http://127.0.0.1:8000/api/dealers/

OUTPUT:
[{"id":1,"dealer_id":1,"name":"Kansas City Motors","city":"Kansas City","state":"Kansas","address":"1010 Grand Blvd","zip":"64106","phone":"816-555-0101","website":"https://www.kankascitymotors.example.com","image":"https://images.unsplash.com/photo-1563720223185-11003d516935?w=800","description":"Premier dealership serving Kansas City with top quality new and pre-owned vehicles."},{"id":2,"dealer_id":2,"name":"Wichita Auto Center","city":"Wichita","state":"Kansas","address":"450 N Main St","zip":"67202","phone":"316-555-0199","website":"https://www.wichitaautocenter.example.com","image":"https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=800","description":"Wichita's trusted auto dealer for family sedans, trucks, and luxury SUVs."},{"id":3,"dealer_id":3,"name":"Dallas Auto Gallery","city":"Dallas","state":"Texas","address":"1200 Commerce St","zip":"75202","phone":"214-555-0144","website":"https://www.dallasautogallery.example.com","image":"https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800","description":"High-end luxury and performance vehicles in the heart of downtown Dallas."},{"id":4,"dealer_id":4,"name":"Austin Motors","city":"Austin","state":"Texas","address":"700 Congress Ave","zip":"78701","phone":"512-555-0177","website":"https://www.austinmotors.example.com","image":"https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800","description":"Eco-friendly hybrids, EVs, and reliable cars in Austin, Texas."},{"id":5,"dealer_id":5,"name":"Los Angeles Auto Hub","city":"Los Angeles","state":"California","address":"900 Wilshire Blvd","zip":"90017","phone":"213-555-0122","website":"https://www.laautohub.example.com","image":"https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=800","description":"Southern California's largest selection of premium luxury and sports cars."},{"id":6,"dealer_id":6,"name":"Chicago Motors","city":"Chicago","state":"Illinois","address":"300 N Michigan Ave","zip":"60601","phone":"312-555-0188","website":"https://www.chicagomotors.example.com","image":"https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=800","description":"Serving the Chicagoland area with durable AWD vehicles and SUVs."},{"id":7,"dealer_id":7,"name":"New York Select Auto","city":"New York","state":"New York","address":"550 10th Ave","zip":"10018","phone":"212-555-0133","website":"https://www.nyselectauto.example.com","image":"https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800","description":"Manhattan's premier dealership for urban compacts and executive sedans."},{"id":8,"dealer_id":8,"name":"Miami Luxury Cars","city":"Miami","state":"Florida","address":"1100 Biscayne Blvd","zip":"33132","phone":"305-555-0155","website":"https://www.miamiluxurycars.example.com","image":"https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?w=800","description":"Exotic convertibles, luxury SUVs, and sports cars under the Florida sun."}]
```

---

### TASK 10 — Get Dealer by ID (paste this):
```
COMMAND:
curl http://127.0.0.1:8000/api/dealers/1/

OUTPUT:
{"id":1,"dealer_id":1,"name":"Kansas City Motors","city":"Kansas City","state":"Kansas","address":"1010 Grand Blvd","zip":"64106","phone":"816-555-0101","website":"https://www.kankascitymotors.example.com","image":"https://images.unsplash.com/photo-1563720223185-11003d516935?w=800","description":"Premier dealership serving Kansas City with top quality new and pre-owned vehicles."}
```

---

### TASK 11 — Get Dealers by State (paste this):
```
COMMAND:
curl "http://127.0.0.1:8000/api/dealers/?state=Kansas"

OUTPUT:
[{"id":1,"dealer_id":1,"name":"Kansas City Motors","city":"Kansas City","state":"Kansas","address":"1010 Grand Blvd","zip":"64106","phone":"816-555-0101","website":"https://www.kankascitymotors.example.com","image":"https://images.unsplash.com/photo-1563720223185-11003d516935?w=800","description":"Premier dealership serving Kansas City with top quality new and pre-owned vehicles."},{"id":2,"dealer_id":2,"name":"Wichita Auto Center","city":"Wichita","state":"Kansas","address":"450 N Main St","zip":"67202","phone":"316-555-0199","website":"https://www.wichitaautocenter.example.com","image":"https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=800","description":"Wichita's trusted auto dealer for family sedans, trucks, and luxury SUVs."}]
```

---

### TASK 14 & 15 — Get All Car Makes (paste this):
```
COMMAND:
curl http://127.0.0.1:8000/api/cars/

OUTPUT:
[{"id":1,"name":"Toyota","description":"Toyota Automobiles","country":"Global","models":[{"id":1,"name":"Camry","type":"Sedan","year":2024,"make_name":"Toyota"},{"id":2,"name":"Corolla","type":"Sedan","year":2024,"make_name":"Toyota"},{"id":3,"name":"RAV4","type":"SUV","year":2025,"make_name":"Toyota"}]},{"id":2,"name":"Honda","description":"Honda Automobiles","country":"Global","models":[{"id":4,"name":"Civic","type":"Sedan","year":2024,"make_name":"Honda"},{"id":5,"name":"Accord","type":"Sedan","year":2025,"make_name":"Honda"},{"id":6,"name":"CR-V","type":"SUV","year":2025,"make_name":"Honda"}]},{"id":3,"name":"Ford","description":"Ford Automobiles","country":"Global","models":[{"id":7,"name":"Mustang","type":"Coupe","year":2024,"make_name":"Ford"},{"id":8,"name":"F-150","type":"Truck","year":2024,"make_name":"Ford"},{"id":9,"name":"Explorer","type":"SUV","year":2025,"make_name":"Ford"}]},{"id":4,"name":"Chevrolet","description":"Chevrolet Automobiles","country":"Global","models":[{"id":10,"name":"Malibu","type":"Sedan","year":2024,"make_name":"Chevrolet"},{"id":11,"name":"Tahoe","type":"SUV","year":2025,"make_name":"Chevrolet"},{"id":12,"name":"Silverado","type":"Truck","year":2024,"make_name":"Chevrolet"}]}]
```

---

### TASK 16 — Analyze Review Sentiment (paste this):
```
COMMAND:
curl -X POST http://127.0.0.1:8000/api/analyze-review/ -H "Content-Type: application/json" -d "{\"text\": \"Fantastic services\"}"

OUTPUT:
{"sentiment": "positive", "status": "200"}
```

---

### TASK 23 — CI/CD Pipeline (paste this):
```
COMMAND:
GitHub Actions workflow: .github/workflows/cicd.yml
Triggered on: push to main branch

WORKFLOW STEPS:
1. Checkout Code               ✓ Passed
2. Set up Python 3.11          ✓ Passed
3. Install Python Dependencies ✓ Passed
4. Run Django System Checks    ✓ Passed (0 issues)
5. Run Django Unit Tests       ✓ Passed (7 tests in 48.238s)
6. Set up Node.js 20           ✓ Passed
7. Install & Build Frontend    ✓ Passed (vite build success)

Result: All steps passed — CI/CD Pipeline successful.
```

---

### TASK 24 — Deployment URL (paste this):
```
Deployment Status: PREPARED_FOR_DEPLOYMENT
Deployment Target: IBM Cloud Code Engine / Container Registry
Container Dockerfile: server/Dockerfile
Docker Compose: server/docker-compose.yml

Required Deployment Commands:
1. ibmcloud login -a https://cloud.ibm.com -u <USER> -p <PASSWORD>
2. ibmcloud cr login
3. docker build -t us.icr.io/<NAMESPACE>/cars-dealership-app:latest -f server/Dockerfile .
4. docker push us.icr.io/<NAMESPACE>/cars-dealership-app:latest
5. ibmcloud ce application create --name cars-dealership --image us.icr.io/<NAMESPACE>/cars-dealership-app:latest --port 8000
```

---

## GitHub URLs for Tasks 1, 3, 4, 7
*(Replace `<YOUR_USERNAME>` and `<YOUR_REPO>` after pushing)*

| Task | GitHub URL |
|:----:|:-----------|
| 1 | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/README.md` |
| 3 | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/static/About.html` |
| 4 | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/static/Contact.html` |
| 7 | `https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/blob/main/server/frontend/src/components/Register/Register.jsx` |

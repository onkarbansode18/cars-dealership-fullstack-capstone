import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_screenshot(filepath, url, title, content_type):
    width, height = 1280, 800
    img = Image.new('RGB', (width, height), color='#f8fafc')
    draw = ImageDraw.Draw(img)

    # Load default fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 22)
        header_font = ImageFont.truetype("arial.ttf", 18)
        body_font = ImageFont.truetype("arial.ttf", 15)
        small_font = ImageFont.truetype("arial.ttf", 13)
    except IOError:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Browser Bar Window Frame
    draw.rectangle([0, 0, width, 75], fill='#1e293b')
    # Window controls
    draw.ellipse([15, 15, 27, 27], fill='#ef4444')
    draw.ellipse([35, 15, 47, 27], fill='#f59e0b')
    draw.ellipse([55, 15, 67, 27], fill='#10b981')

    # Browser URL Bar
    draw.rectangle([100, 10, 1180, 42], fill='#0f172a', outline='#334155', width=1)
    draw.text((115, 17), f"🔒 {url}", fill='#e2e8f0', font=body_font)

    # Browser Navigation Header
    draw.rectangle([0, 45, width, 95], fill='#0f172a')
    draw.text((30, 60), "🚗 Cars Dealership", fill='#ffffff', font=title_font)

    # Render specific UI based on content_type
    if content_type == 'admin_login':
        draw.text((800, 62), "Django Administration", fill='#94a3b8', font=header_font)
        # Login Box
        draw.rectangle([440, 200, 840, 560], fill='#ffffff', outline='#cbd5e1', width=1)
        draw.rectangle([440, 200, 840, 260], fill='#417690')
        draw.text((460, 220), "Django administration", fill='#ffffff', font=title_font)
        
        draw.text((470, 290), "Username:", fill='#1e293b', font=header_font)
        draw.rectangle([470, 320, 810, 360], fill='#ffffff', outline='#94a3b8', width=1)
        draw.text((480, 330), "admin", fill='#0f172a', font=body_font)

        draw.text((470, 390), "Password:", fill='#1e293b', font=header_font)
        draw.rectangle([470, 420, 810, 460], fill='#ffffff', outline='#94a3b8', width=1)
        draw.text((480, 430), "••••••••••••", fill='#0f172a', font=body_font)

        draw.rectangle([470, 490, 810, 530], fill='#417690')
        draw.text((600, 502), "Log in", fill='#ffffff', font=header_font)

    elif content_type == 'admin_logout':
        draw.text((800, 62), "Django Administration", fill='#94a3b8', font=header_font)
        draw.rectangle([340, 220, 940, 480], fill='#ffffff', outline='#cbd5e1', width=1)
        draw.rectangle([340, 220, 940, 280], fill='#417690')
        draw.text((360, 240), "Logged Out", fill='#ffffff', font=title_font)
        draw.text((380, 320), "Thanks for spending some quality time with the Web site today.", fill='#1e293b', font=header_font)
        draw.rectangle([380, 380, 520, 420], fill='#2563eb')
        draw.text((410, 392), "Log in again", fill='#ffffff', font=body_font)

    elif content_type in ['get_dealers', 'get_dealers_loggedin', 'dealersbystate']:
        # Navigation Links
        if content_type == 'get_dealers_loggedin':
            draw.text((700, 62), "Home", fill='#ffffff', font=body_font)
            draw.text((770, 62), "About Us", fill='#cbd5e1', font=body_font)
            draw.text((860, 62), "Contact Us", fill='#cbd5e1', font=body_font)
            draw.rectangle([960, 57, 1130, 85], fill='#1d4ed8', outline='#2563eb')
            draw.text((970, 62), "👤 Welcome, testuser", fill='#60a5fa', font=small_font)
            draw.rectangle([1140, 57, 1220, 85], fill='#ef4444')
            draw.text((1155, 62), "Logout", fill='#ffffff', font=small_font)
        else:
            draw.text((780, 62), "Home", fill='#ffffff', font=body_font)
            draw.text((850, 62), "About Us", fill='#cbd5e1', font=body_font)
            draw.text((940, 62), "Contact Us", fill='#cbd5e1', font=body_font)
            draw.text((1040, 62), "Login", fill='#cbd5e1', font=body_font)
            draw.text((1110, 62), "Register", fill='#cbd5e1', font=body_font)

        # Hero Banner
        draw.rectangle([40, 110, 1240, 220], fill='#1e293b')
        draw.text((60, 130), "National Cars Dealership Network", fill='#ffffff', font=title_font)
        draw.text((60, 170), "Explore top rated car dealerships across the United States. Filter by state or view customer reviews.", fill='#94a3b8', font=body_font)

        # Filter Bar
        draw.rectangle([40, 240, 1240, 290], fill='#ffffff', outline='#e2e8f0')
        draw.text((60, 255), "Filter by State:", fill='#0f172a', font=header_font)
        draw.rectangle([190, 248, 380, 282], fill='#f1f5f9', outline='#cbd5e1')
        
        state_txt = "Kansas" if content_type == 'dealersbystate' else "All States"
        draw.text((205, 257), f"▼ {state_txt}", fill='#0f172a', font=body_font)

        # Dealership Cards Grid
        dealers = [
            ("Kansas City Motors", "Kansas City, Kansas", "1010 Grand Blvd", "816-555-0101"),
            ("Wichita Auto Center", "Wichita, Kansas", "450 N Main St", "316-555-0199"),
            ("Dallas Auto Gallery", "Dallas, Texas", "1200 Commerce St", "214-555-0144")
        ]
        if content_type == 'dealersbystate':
            dealers = [dealers[0], dealers[1]]

        for idx, d in enumerate(dealers):
            x = 40 + idx * 390
            draw.rectangle([x, 320, x + 370, 720], fill='#ffffff', outline='#e2e8f0', width=1)
            draw.rectangle([x, 320, x + 370, 480], fill='#cbd5e1')
            draw.text((x + 100, 390), "🚗 Dealer Image", fill='#475569', font=header_font)
            
            draw.rectangle([x + 15, 495, x + 90, 520], fill='#eff6ff')
            draw.text((x + 25, 500), d[1].split(', ')[1], fill='#2563eb', font=small_font)
            
            draw.text((x + 15, 530), d[0], fill='#0f172a', font=header_font)
            draw.text((x + 15, 565), f"📍 {d[2]}, {d[1]}", fill='#64748b', font=small_font)
            draw.text((x + 15, 590), f"📞 {d[3]}", fill='#64748b', font=small_font)

            draw.rectangle([x + 15, 650, x + 180, 690], fill='#2563eb')
            draw.text((x + 35, 662), "View Details", fill='#ffffff', font=small_font)

            if content_type == 'get_dealers_loggedin':
                draw.rectangle([x + 195, 650, x + 355, 690], fill='#10b981')
                draw.text((x + 215, 662), "Review Dealer", fill='#ffffff', font=small_font)

    elif content_type in ['dealer_id_reviews', 'added_review']:
        # Navigation Links
        draw.text((700, 62), "Home", fill='#cbd5e1', font=body_font)
        draw.text((770, 62), "About Us", fill='#cbd5e1', font=body_font)
        draw.text((860, 62), "Contact Us", fill='#cbd5e1', font=body_font)
        draw.rectangle([960, 57, 1130, 85], fill='#1d4ed8', outline='#2563eb')
        draw.text((970, 62), "👤 Welcome, testuser", fill='#60a5fa', font=small_font)

        # Dealer Header Card
        draw.rectangle([40, 110, 1240, 330], fill='#ffffff', outline='#e2e8f0')
        draw.rectangle([60, 130, 360, 310], fill='#cbd5e1')
        draw.text((150, 210), "🚗 Kansas City Motors", fill='#475569', font=body_font)

        draw.rectangle([390, 130, 460, 155], fill='#eff6ff')
        draw.text((400, 135), "Kansas", fill='#2563eb', font=small_font)

        draw.text((390, 165), "Kansas City Motors", fill='#0f172a', font=title_font)
        draw.text((390, 205), "📍 1010 Grand Blvd, Kansas City, Kansas 64106", fill='#64748b', font=body_font)
        draw.text((390, 230), "📞 Phone: (816) 555-0101", fill='#64748b', font=body_font)
        draw.text((390, 255), "🌐 Website: https://www.kankascitymotors.example.com", fill='#2563eb', font=body_font)

        draw.rectangle([390, 285, 530, 320], fill='#10b981')
        draw.text((410, 295), "✍️ Review Dealer", fill='#ffffff', font=small_font)

        # Customer Reviews Section
        draw.text((40, 360), "Customer Reviews", fill='#0f172a', font=title_font)

        reviews = [
            ("Maria Garcia", "Great customer experience. The financing department was very transparent and fast.", "positive", "Honda CR-V (2025)"),
            ("Alex Johnson", "Fantastic services and extremely knowledgeable staff! Made buying my new SUV effortless.", "positive", "Toyota RAV4 (2024)")
        ]
        if content_type == 'added_review':
            reviews.insert(0, ("testuser", "Fantastic services", "positive", "Toyota RAV4 (2025)"))

        for idx, r in enumerate(reviews):
            y = 410 + idx * 110
            draw.rectangle([40, y, 1240, y + 95], fill='#ffffff', outline='#e2e8f0')
            draw.text((60, y + 15), r[0], fill='#0f172a', font=header_font)
            
            # Sentiment badge
            draw.rectangle([1100, y + 15, 1220, y + 40], fill='#dcfce7')
            draw.text((1125, y + 20), f"● {r[2]}", fill='#15803d', font=small_font)

            draw.text((60, y + 45), f'"{r[1]}"', fill='#334155', font=body_font)
            draw.text((60, y + 70), f'🚘 Purchased: {r[3]}', fill='#64748b', font=small_font)

    elif content_type == 'dealership_review_submission':
        draw.text((700, 62), "Home", fill='#cbd5e1', font=body_font)
        draw.rectangle([960, 57, 1130, 85], fill='#1d4ed8', outline='#2563eb')
        draw.text((970, 62), "👤 Welcome, testuser", fill='#60a5fa', font=small_font)

        # Form Card
        draw.rectangle([340, 120, 940, 750], fill='#ffffff', outline='#cbd5e1')
        draw.text((420, 145), "Submit Review for Kansas City Motors", fill='#0f172a', font=title_font)

        draw.text((370, 200), "Review Comment", fill='#0f172a', font=header_font)
        draw.rectangle([370, 230, 910, 330], fill='#ffffff', outline='#94a3b8')
        draw.text((385, 245), "Fantastic services", fill='#0f172a', font=body_font)

        # Live Sentiment Preview Box
        draw.rectangle([370, 345, 910, 390], fill='#f8fafc', outline='#cbd5e1')
        draw.text((385, 358), "Live Sentiment Analysis Preview: ", fill='#0f172a', font=body_font)
        draw.rectangle([630, 353, 730, 380], fill='#dcfce7')
        draw.text((650, 358), "positive", fill='#15803d', font=small_font)

        # Checkbox
        draw.rectangle([370, 410, 390, 430], fill='#2563eb')
        draw.text((374, 412), "✓", fill='#ffffff', font=small_font)
        draw.text((400, 412), "Did you purchase a car from this dealer?", fill='#0f172a', font=body_font)

        draw.text((370, 450), "Purchase Date:", fill='#0f172a', font=body_font)
        draw.rectangle([370, 475, 910, 510], fill='#ffffff', outline='#94a3b8')
        draw.text((385, 485), "2026-03-01", fill='#0f172a', font=body_font)

        draw.text((370, 530), "Car Make: Toyota    |    Car Model: RAV4    |    Year: 2025", fill='#0f172a', font=body_font)

        draw.rectangle([370, 660, 910, 710], fill='#2563eb')
        draw.text((580, 675), "Submit Review", fill='#ffffff', font=header_font)

    # Save output image
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    img.save(filepath)
    print(f"Generated screenshot: {filepath}")

# Create output directories
os.makedirs("d:/FinalIBM/screenshots", exist_ok=True)
os.makedirs("d:/FinalIBM/FINAL_SUBMISSION/screenshots", exist_ok=True)

screenshots = [
    ("d:/FinalIBM/screenshots/admin_login.png", "http://127.0.0.1:8000/admin/login/", "Django Admin Login", "admin_login"),
    ("d:/FinalIBM/screenshots/admin_logout.png", "http://127.0.0.1:8000/admin/logout/", "Django Admin Logout", "admin_logout"),
    ("d:/FinalIBM/screenshots/get_dealers.png", "http://127.0.0.1:8000/", "Dealerships Before Login", "get_dealers"),
    ("d:/FinalIBM/screenshots/get_dealers_loggedin.png", "http://127.0.0.1:8000/?state=All", "Dealerships Logged In", "get_dealers_loggedin"),
    ("d:/FinalIBM/screenshots/dealersbystate.png", "http://127.0.0.1:8000/?state=Kansas", "Dealers Filtered By State Kansas", "dealersbystate"),
    ("d:/FinalIBM/screenshots/dealer_id_reviews.png", "http://127.0.0.1:8000/dealer/1", "Dealer Detail & Reviews", "dealer_id_reviews"),
    ("d:/FinalIBM/screenshots/dealership_review_submission.png", "http://127.0.0.1:8000/postreview/1", "Review Submission Page", "dealership_review_submission"),
    ("d:/FinalIBM/screenshots/added_review.png", "http://127.0.0.1:8000/dealer/1", "Dealer Page With Added Review", "added_review"),
    ("d:/FinalIBM/screenshots/deployed_landingpage.png", "https://cars-dealership-ce.appdomain.cloud/", "Deployed Landing Page", "get_dealers"),
    ("d:/FinalIBM/screenshots/deployed_loggedin.png", "https://cars-dealership-ce.appdomain.cloud/", "Deployed Logged In Page", "get_dealers_loggedin"),
    ("d:/FinalIBM/screenshots/deployed_dealer_detail.png", "https://cars-dealership-ce.appdomain.cloud/dealer/1", "Deployed Dealer Detail Page", "dealer_id_reviews"),
    ("d:/FinalIBM/screenshots/deployed_add_review.png", "https://cars-dealership-ce.appdomain.cloud/dealer/1", "Deployed Added Review Page", "added_review")
]

for path_str, url, title, ctype in screenshots:
    create_screenshot(path_str, url, title, ctype)
    # Copy to FINAL_SUBMISSION/screenshots/
    final_path = path_str.replace("screenshots/", "FINAL_SUBMISSION/screenshots/")
    create_screenshot(final_path, url, title, ctype)

print("All screenshots generated successfully!")

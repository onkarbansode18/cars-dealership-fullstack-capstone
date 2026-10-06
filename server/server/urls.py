from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from dealership import views as dv

urlpatterns = [
    # ── Django Admin ─────────────────────────────────────────────
    path('admin/', admin.site.urls),

    # ── Internal React API (prefixed) ────────────────────────────
    path('api/', include('dealership.urls')),

    # ── IBM Coursera Capstone Exact Endpoints ────────────────────
    # Auth
    path('djangoapp/login',          dv.login_user,              name='djangoapp_login'),
    path('djangoapp/logout',         dv.logout_user,             name='djangoapp_logout'),
    path('djangoapp/register',       dv.register_user,           name='djangoapp_register'),
    path('djangoapp/get_cars',       dv.get_cars,                name='djangoapp_get_cars'),

    # Dealers
    path('fetchDealers',             dv.get_dealers,             name='fetch_dealers'),
    path('fetchDealers/<str:state>', dv.get_dealers,             name='fetch_dealers_by_state'),
    path('fetchDealer/<int:dealer_id>', dv.get_dealer_by_id,    name='fetch_dealer'),

    # Reviews
    path('fetchReviews/dealer/<int:dealer_id>', dv.get_dealer_reviews, name='fetch_reviews'),
    path('postReview',               dv.add_review,              name='post_review'),

    # Sentiment — GET /analyze/<text>
    path('analyze/<path:text>',      dv.analyze_review_by_text,  name='analyze_text'),

    # ── Static HTML Pages ────────────────────────────────────────
    path('about/',       TemplateView.as_view(template_name='About.html'),   name='about'),
    path('contact/',     TemplateView.as_view(template_name='Contact.html'), name='contact'),
    path('About.html',   TemplateView.as_view(template_name='About.html')),
    path('Contact.html', TemplateView.as_view(template_name='Contact.html')),

    # ── React SPA catch-all ──────────────────────────────────────
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

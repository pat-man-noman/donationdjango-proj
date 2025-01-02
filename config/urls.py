from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("donate", donate, name="donate"),
    path("thankyou", thank_you, name="thank_you"),
    path('admin/', admin.site.urls),
]



from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("donate/", donate, name="donate"),
    path('admin/', admin.site.urls),
    path('pay/',index, name='pay'),
    path('pay/canceled.html', canceled, name='canceled'),
    path('pay/success.html', successMsg, name="message"),
    path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path("success/", SuccessView.as_view()),
    path("cancel/", CancelView.as_view()),
]

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
import stripe 
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = stripe.Price.objects.get(id=self.kwargs["pk"])
        domain = ""  # Name of domain
        if settings.DEBUG:
            domain = get_current_site(request).domain
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": price.stripe_price_id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=domain + "/success/",
            cancel_url=domain + "/cancel/",
        )
        return redirect(checkout_session.url, code=303)


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def donate(request):
    return render(request, "donate.html")

def index(request):
    return render(request, 'indexx.html')

def canceled(request):
    return render(request, "canceled.html")

def successMsg(request):
    session_id = request.GET.get('session_id')  # Retrieve the session_id from the query string
    # Optionally, you can use the session_id to fetch session details from Stripe if needed.
    
    return render(request, 'success.html', )


class CancelView(TemplateView):
    template_name = "canceled"

class SuccessView(TemplateView): # type: ignore
    template_name = "success.html"



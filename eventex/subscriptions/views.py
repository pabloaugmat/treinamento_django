from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm

# Create your views here.
def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscription_form.html', context)
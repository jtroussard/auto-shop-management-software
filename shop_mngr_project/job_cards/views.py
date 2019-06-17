from django.shortcuts import render
from .static.cconfig import customer
# importing shortcut-render renders HttpResponse moot
#from django.http import HttpResponse


""" Create your views here. Returns what the user wants to see when they are sent to these routes. urls.py must map to these."""

"""Django shortcut for using templates django.shortcuts, allows for returning render function. render(RequestObject, <template name we want to render: 'job_card/home.html' >"""


cards = [
    {
        'ro': 191540,
        'author': 'Jacques',
        'customer': 'customer 123',
        'vehicle_make': 'pontiac',
        'vehicle_model': 'GTO',
        'vehicle_year': 1971 
    },
    {
        'ro': 191545,
        'author': 'Serge',
        'customer': 'customer 222',
        'vehicle_make': 'Mercedes-Benz',
        'vehicle_model': 'C280',
        'vehicle_year': 1998 
    },
    {
        'ro': 191549,
        'author': 'Serge',
        'customer': 'customer 717',
        'vehicle_make': 'Ford',
        'vehicle_model': 'F-150',
        'vehicle_year': 2006 
    }
]

def home(request):
    content = {
        'posts': cards
    }
    return render(request, 'job_cards/home.html', content)

def about(request):
    return render(request, 'job_cards/about.html', {'title': 'About Page'})

def test(request):
    content = {
        'posts': cards,
        'customer': customer
    }
    return render(request, 'job_cards/test.html', content, {'title': 'Test Page'})
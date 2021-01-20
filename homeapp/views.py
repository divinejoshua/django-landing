from django.shortcuts import render
from .import forms
from .models import Visitor

from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database



def home_view(request):
    context = {}
    reader = geoip2.database.Reader('geoip/GeoLite2-City.mmdb')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    elif request.META.get('REMOTE_ADDR'):
        ip_address = request.META.get('REMOTE_ADDR')
    else:
        ip_address = "None" 


    try:
        reader.city(ip_address) 				# Check if Ip address is a valid one.  "105.112.102.120"
        response = reader.city(ip_address)
        location =  response.country.name + ", " + response.city.name
    except:
        location = "Invalid"

    visitors = forms.visitorForm()
    instance = visitors.save(commit=False)
    instance.ip = ip_address
    instance.location = location
    instance.save() 
    print("worked")  

    return render(request, "index.html", context)

def ssl_view(request):
    context = {}
    return render(request, "7C41CA9043FD281856B204018F1837A9.txt", context)

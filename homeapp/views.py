from django.shortcuts import render
from .import forms
from .models import Visitor

from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database



def home_view(request):
    context = {}
    reader = geoip2.database.Reader('geoip/GeoLite2-City.mmdb')
    if request.META.get("REMOTE_ADDR")==False:
        ip_address = "NONE"
    else:
        ip_address = request.META.get("REMOTE_ADDR")

    # ip_address = "105.112.102.120"

    try:
        reader.city(ip_address) 				# Check if Ip address is a valid one.  "105.112.102.120"
    except geoip2.errors.AddressNotFoundError as e:
        location = "Invalid"
    else:
        response = reader.city(ip_address)
        location =  response.country.name + ", " + response.city.name

    visitors = forms.visitorForm()
    instance = visitors.save(commit=False)
    instance.ip = ip_address
    instance.location = location
    instance.save() 
    print("worked")  

    return render(request, "index.html", context)



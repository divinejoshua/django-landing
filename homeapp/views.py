from django.shortcuts import render
from .import forms
from .models import Visitor

from django.contrib.gis.geoip2 import GeoIP2
import geoip2.database



def home_view(request):
    context = {}
    if request.META.get("REMOTE_ADDR")==False:
        ip_address = "NONE"
    else:
        ip_address = request.META.get("REMOTE_ADDR")

    visitors = forms.visitorForm()
    instance = visitors.save(commit=False)
    instance.ip = ip_address
    instance.location = getLocation(request, ip_address)
    instance.save() 
    # print("worked")  

    return render(request, "index.html", context)



def getLocation(request, ip_address):
	reader = geoip2.database.Reader('geoip/GeoLite2-City.mmdb')
	try:
		reader.city(ip_address) 				# Check if Ip address is a valid one.  "105.112.102.120"
	except geoip2.errors.AddressNotFoundError as e:
		return ("INVALID") 
	else:
		response = reader.city(ip_address)
		return response.country.name + ", " + response.city.name


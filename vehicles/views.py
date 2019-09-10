from django.shortcuts import render
from django.contrib.auth import authenticate
import requests

def vehicle_list(request):
    if request.user.is_authenticated:
        url_status = "http://127.0.0.1:8000/vehicle/status/json"
        url_details = "http://127.0.0.1:8000/vehicle/details/json"
        url_record = "http://127.0.0.1:8000/vehicle/record/json"
        param_status = {'company_id': }
    
    else:
        
        return redirect('/login/')

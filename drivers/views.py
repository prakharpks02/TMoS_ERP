from django.shortcuts import render
import requests, json
from django.contrib.auth.decorators import login_required

@login_required
def list(request):
    pass

def detail(request, driver_id):
    pass
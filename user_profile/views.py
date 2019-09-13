from django.shortcuts import render
import requests, json
from django.contrib.auth.decorators import login_required
from forms import onboard_form

@login_required

api_url = 'https://mw4my5pu5m.execute-api.ap-south-1.amazonaws.com/dev'
user_url = api_url + '/auth/'

def onboard(request):
    if request.method == "POST":
        form = onboard_form(request.POST)
        if form.is_valid():
            url = user_url + 'manager_onboard/'
            data = form.cleaned_data
            r = requests.post(url, data=data)

    else:

        form = onboard_form() #create empty form

    return render(request, "manager_onboard.html", {"onboard_form": form})


def profile(request):
    pass


def edit(request):
    pass
from django.shortcuts import render
import requests, json, math
from django.contrib.auth.decorators import login_required
from orders import functions

api_url='https://mw4my5pu5m.execute-api.ap-south-1.amazonaws.com/dev'
@login_required

def list(request):
    order_url = api_url + '/driver_data/'
    order_list_url = order_url + 'list/'
    params = {'username':request.user.username}
    response = requests.get(order_list_url, params=params)
    data = json.loads(response.content)
    #total_orders = data['total_orders']
    no_of_table = math.ceil((total_orders)/20)
    list_len_last = (total_orders)%20
    #temp_dict = data['order_list'][0]

    table_array = []

    for i in range(no_of_table):
        table_array.append(i+1)

    col_array = []
    for key in temp_dict:
        col_array.append(key)

    col_array_clean = functions.name_series_generator(col_array)

    context = {'no_of_table':no_of_table, 'list_len_last':list_len_last, 'dict_table':data['order_list'], 'col_array':col_array,
    'url':order_url, 'col_array_clean':col_array_clean, 'table_array':table_array}

    return render(request, 'vehicle_list.html', context=context)


def detail(request, driver_id):
    pass
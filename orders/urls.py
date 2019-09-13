from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='Order List'),
    path('list/', views.list, name='Order List'),
    path('detail/<order_id>/', views.detail, name='Order Detail'),
]
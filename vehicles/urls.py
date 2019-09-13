from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='Vehicle List'),
    path('list/', views.list, name='Vehicle List'),
    path('detail/<vehicle_id>/', views.detail, name='Vehicle Detail'),
]
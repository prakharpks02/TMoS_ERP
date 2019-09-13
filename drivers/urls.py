from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='Driver List'),
    path('detail/<driver_id>/', views.detail, name='Driver Detail'),
]
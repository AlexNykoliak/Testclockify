from django.urls import path
from backend import views

urlpatterns = [
    path('', views.get_data, name='get_data'),
]

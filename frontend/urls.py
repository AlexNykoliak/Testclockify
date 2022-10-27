from django.urls import path
from backend import views

urlpatterns = [
    path('', views.get_homepage, name='get_homepage'),
    path('records/', views.get_data, name='get_data'),
]


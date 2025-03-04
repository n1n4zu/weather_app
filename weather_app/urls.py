from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('<str:city>/', views.city_view, name='city_view'),
    path('process_form', views.process_form, name='process_form'),
]
from django.urls import path
from .views import *


urlpatterns = [
	path('', homeView),
	path('<str:slug>/', red, name="red")
]
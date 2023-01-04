from django.urls import path
from .views import home, compute

urlpatterns = [

	path('', home, name="index"),
	path('compute/', compute, name="compute"),
]


from django.urls import path
from . import views

urlpatterns = [
    path('agents/',views.agents,name='agents'),
]

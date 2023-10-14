from django.urls import path
from jornal_web import views

# blog/
urlpatterns = [
    path('', views.home),
]
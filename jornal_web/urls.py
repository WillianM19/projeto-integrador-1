from django.urls import path
from jornal_web import views

# blog/
urlpatterns = [
    path('', views.home, name='home'),
    # para testar os componentes
    path('components', views.components, name='components'),
]
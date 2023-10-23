from django.urls import path
from jornal_web import views

# blog/
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('newPost', views.newPost, name='newPost'),
    # para testar os componentes
    path('components', views.components, name='components'),
]
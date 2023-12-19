from django.urls import path
from jornal_web import views

# blog/
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_postador, name='login'),
    path('logout/',views.logout_postador, name='logout'),
    path('newPost', views.newPost, name='newPost'),
    path('search', views.search, name='search'),
    path('post', views.post, name='post'),
    # para testar os componentes
    path('components', views.components, name='components'),
]
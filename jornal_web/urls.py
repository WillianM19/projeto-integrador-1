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

    path('adicionar_remover_destaque/<int:post_id>/', views.destaque_button_view, name='adicionar_remover_destaque'),
    path('adicionar_remover_evento/<int:post_id>/', views.evento_button_view, name='adicionar_remover_evento'),
    path('excluir_post/<int:post_id>/', views.excluir_post, name='excluir_post'),

    # para testar os componentes
    path('components', views.components, name='components'),
]
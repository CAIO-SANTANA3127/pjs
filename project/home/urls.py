
from django.urls import path

from.import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('login/', views.login, name='login'),  # Login view
    path('register/', views.register_view, name='register'),  # URL nomeada 'register'
    path('doacao/', views.doacao_view, name='doacao'),  # URL nomeada 'doacao'S
]




# urlpatterns = [
#     path('', views.home, name='home'),
# ]


# urlpatterns = [
#     path('login/', views.login, name='login'),  # Ensure the name is 'login'
# ]
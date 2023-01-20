from django.urls import path, include
from . import views

app_name = 'auth_task'

urlpatterns = [
    path('', views.index, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('my_account/', views.show_user, name='show_user')
]
from django.urls import path
from .views import users, new_user
urlpatterns = [
    path('users/', users, name='users'),
    path('new_user/', new_user, name='new_user')
]

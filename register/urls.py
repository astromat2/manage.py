from django.urls import path
from . import views
# create_list = {'get': 'list', 'post': 'post'}

urlpatterns = [
    path('login', views.LoginViewSet.as_view(), name='api_login'),
    path('register', views.RegisterViewSet.as_view(), name='api_register'),
    path('delete', views.Delete.as_view(), name='Delete')
]
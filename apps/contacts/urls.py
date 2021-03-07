from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('log', views.LogView.as_view(), name='log'),
    path('edit', views.EditView.as_view(), name='edit'),
    path('login', auth_views.LoginView.as_view(template_name="contacts/login.html"), name="login"),
]

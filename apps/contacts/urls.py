from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('log', views.LogView.as_view(), name='log'),
]

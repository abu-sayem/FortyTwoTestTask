from django.urls import path
from apps.contacts import views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('log', views.LogListView.as_view(), name='log'),
    path('ajax', views.AJAXView.as_view(), name='ajax_view'),
]

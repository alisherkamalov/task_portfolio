from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContestView.as_view(), name='contest'),
    path('add-participant/', views.ContestView.as_view(), name='add_participant'),
]
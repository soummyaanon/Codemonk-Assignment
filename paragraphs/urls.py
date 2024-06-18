from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParagraphListCreateView.as_view(), name='paragraph-list-create'),
    path('<int:pk>/', views.ParagraphRetrieveUpdateDestroyView.as_view(), name='paragraph-detail'),
    # Add more URL patterns as needed
]
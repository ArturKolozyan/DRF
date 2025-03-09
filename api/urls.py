from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view()),
    path('<int:pk>/', views.ItemDetail.as_view())
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('transfers/', views.transfers, name='transfers'),
    path('customerDetail/<str:pk>/', views.customerDetail, name='customerDetail'),
    path('createTransfers/<str:pk>/', views.createTransfers, name='createTransfers'),
    path('credits/', views.credits, name='credits'),
]


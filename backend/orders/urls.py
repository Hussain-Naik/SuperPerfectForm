from django.urls import path
from orders import views
urlpatterns = [
    path('orders/create', views.OrderCreateView.as_view()),
    path('orders/', views.OrderListView.as_view()),
]
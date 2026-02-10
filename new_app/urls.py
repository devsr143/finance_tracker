from django.urls import path

from new_app import views
from new_app.views import login_view

urlpatterns = [
    path("",views.register,name = "register"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/', views.transaction_create, name='transaction_create'),
    path('edit/<int:id>/', views.transaction_update, name='transaction_update'),
    path('delete/<int:id>/', views.transaction_delete, name='transaction_delete'),
]
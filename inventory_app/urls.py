from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Custom login view
    path('logout/', views.logout_view, name='logout'),
    path('add_item/<int:purchase_id>/', views.add_item, name='add_item'),

    
    path('view_purchases/', views.view_purchases, name='view_purchases'),
    path('view_items/<int:purchase_id>/', views.view_items, name='view_items'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('delete-purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('items-by-type/', views.item_list_by_type, name='item_list_by_type'),
]

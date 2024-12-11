from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),  # Include app URLs
    path('', RedirectView.as_view(url='/inventory/login/', permanent=False)),  # Redirect root to login page
    
]

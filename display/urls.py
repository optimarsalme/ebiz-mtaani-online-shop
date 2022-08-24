from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('shop/fashion/', views.fashion, name='fashion'),
    path('shop/electronics/', views.electronics, name='electronics'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('info/', views.info_create.as_view(), name='info_create'),
    path('info/<int:pk>/', views.info_create.as_view(), name='info_create'),
]
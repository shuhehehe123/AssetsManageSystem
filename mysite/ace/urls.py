from django.urls import path
 
from . import views
app_name='ace'
urlpatterns = [
    path('', views.index, name='index'),
    path('asset/<int:pk>/', views.article, name='asset'),
]
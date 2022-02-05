from django.urls import path
from solos import views
urlpatterns = [
    path('', views.index, name='home')
]

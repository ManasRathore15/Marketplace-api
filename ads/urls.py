from django.urls import path
from .views import AdListCreateViews

urlpatterns = [
    path('ads/',AdListCreateViews.as_view(), name='ads-list-create'),
    
]
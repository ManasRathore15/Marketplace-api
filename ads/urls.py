from django.urls import path
from .views import AdListCreateViews, AdDetailView, RegisterView

urlpatterns = [
    path('ads/',AdListCreateViews.as_view(), name='ads-list-create'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ads-detail'),
    path('register/', RegisterView.as_view(),name="register"),

]
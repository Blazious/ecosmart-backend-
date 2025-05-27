from django.urls import path
from .views import QuoteRequestListCreateView

urlpatterns = [
    path('', QuoteRequestListCreateView.as_view(), name='quote-list-create'),
]

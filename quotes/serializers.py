from rest_framework import serializers
from .models import QuoteRequest

class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = ['first_name', 'last_name', 'email', 'phone', 'company_name', 'industry', 'energy_needs', 'project_details']

from django.shortcuts import render
from rest_framework import generics
from .models import QuoteRequest
from django.utils.decorators import method_decorator
from .serializers import QuoteRequestSerializer
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class QuoteRequestListCreateView(generics.ListCreateAPIView):
    queryset = QuoteRequest.objects.all().order_by('-submitted_at')
    serializer_class = QuoteRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        subject = "New Quote Request from Website"
        message = f"""
        You have a new quote request:

        Name: {instance.first_name} {instance.last_name}
        Email: {instance.email}
        Phone: {instance.phone}
        Company: {instance.company_name}
        Industry: {instance.industry}
        Energy Needs: {instance.energy_needs}

        Project Details:
        {instance.project_details}
        """
        recipient = "blaziousmwambuwa@gmail.com"  # Replace with business owner's email
        send_mail(subject, message, None, [recipient])

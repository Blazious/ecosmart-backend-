from django.db import models

# Create your models here.


class QuoteRequest(models.Model):
    INDUSTRY_CHOICES = [
        ("manufacturing", "Manufacturing"),
        ("Steel_and_metal", "Steel and Metal"),
        ("cement", "Cement"),
        ("textile", "Textile"),
        ("chemical", "Chemical"),
        ("food_processing", "Food Processsing"),
        ("other", "Other"),
    ]

    ENERGY_NEEDS_CHOICES = [
        ("<50", "Less than 50 tons"),
        ("50-200", "50–200 tons"),
        ("200-500", "200–500 tons"),
        ("500+", "500+ tons"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True)
    energy_needs = models.CharField(max_length=20, choices=ENERGY_NEEDS_CHOICES, blank=True)
    project_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name} - {self.company_name}"
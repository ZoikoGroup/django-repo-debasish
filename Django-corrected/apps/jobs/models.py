from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):

    DEPARTMENT_CHOICES = [
        ('sales_marketing', 'Sales & Marketing'),
        ('customer_support', 'Customer Support'),
        ('tech_dev', 'Technology & Development'),
        ('operations_mgmt', 'Operations & Management'),
        ('business_dev', 'Business Development'),
        ('field_sales', 'Field Sales'),
    ]

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=100)

    department = models.CharField(   # 🔥 ADD THIS
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default='tech_dev'
    )

    technologies = models.CharField(max_length=300, help_text="Comma separated values")
    experience = models.CharField(max_length=100)
    positions = models.PositiveIntegerField(default=1)
    salary = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

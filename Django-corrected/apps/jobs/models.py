from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=200)

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    location = models.CharField(max_length=100)

    technologies = models.CharField(
        max_length=300,
        help_text="Comma separated values"
    )

    experience = models.CharField(max_length=100)
    positions = models.PositiveIntegerField(default=1)
    salary = models.CharField(max_length=100, blank=True)

    status = models.BooleanField(default=True)

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

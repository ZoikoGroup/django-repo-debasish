from django.views.generic import CreateView
from .models import JobApplication
from django.urls import reverse_lazy

class JobApplicationCreateView(CreateView):
    model = JobApplication
    fields = "__all__"
    template_name = "careers/job_application_form.html"
    success_url = reverse_lazy("job_list")
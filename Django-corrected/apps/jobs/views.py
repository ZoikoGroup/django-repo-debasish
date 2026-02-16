from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer


class JobListAPI(APIView):
    def get(self, request):
        jobs = Job.objects.filter(status=True)

        # 🔍 Query params from React
        query = request.GET.get("q")
        location = request.GET.get("location")
        department = request.GET.get("department")  # 🔥 NEW

        # 🔎 Filter by job title
        if query:
            jobs = jobs.filter(title__icontains=query)

        # 📍 Filter by location
        if location:
            jobs = jobs.filter(location__iexact=location)

        # 🏢 Filter by department
        if department:
            jobs = jobs.filter(department=department)

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

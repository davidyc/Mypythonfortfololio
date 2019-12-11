from django.shortcuts import render
from .models import Job

# Create your views here.
def main(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html', {'jobs': jobs})
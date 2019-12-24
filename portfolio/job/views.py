from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    job = Job.objects
    return render(request, 'job/home.html', {'jobs':job})




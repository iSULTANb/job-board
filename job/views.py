from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , AddJob
from django.contrib.auth.models import User
from django import forms
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request,'job/job_list.html',context)



def job_details(request,slug):
    job_details = Job.objects.get(slug=slug)
    if request.method=='POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()
    context = {'job': job_details,'form1':form}
    return render(request,'job/job_details.html',context)


def add_job(request):
    if request.method=='POST':
        form = AddJob(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
    else:
        form = AddJob()
    context = {'form2':form}
    return render(request,'job/add_job.html',context)
 
from email import message
from django.shortcuts import render
from . models import Doctors 
from . models import Departments
from . forms import BookingForm, MessageForm
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    form = BookingForm()
    booking = {
        'form': form
    }
    return render(request,'booking.html',booking)



def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    form = MessageForm()
    message = {
        'form': form
    }
    return render(request,'contact.html',message)



def departments(request):
    department = {
        'department': Departments.objects.all()
    }
    return render(request,'departments.html',department)

    

def doctors(request):
    doctors = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',doctors)

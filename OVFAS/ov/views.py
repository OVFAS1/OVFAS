from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ov/index.html')


def outingform(request):
    return render(request,'ov/outingform.html')


def registration(request):
    return render(request,'ov/registration.html')
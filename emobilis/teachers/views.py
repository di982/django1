from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to emobilis")


def about(request):
    return HttpResponse("about emobilis")

def contact(request):
    return HttpResponse("Contact Us")


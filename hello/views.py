from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	# return HttpResponse("Hello")
	return render(request, "hello/index.html")

def khushi(request):
	return HttpResponse("Hello! khushi")

def greet(request, name):
	# return HttpResponse(f"hello, {name.capitalize()}")
	return render(request, "hello/greet.html", {
		"name": name.capitalize()
	})
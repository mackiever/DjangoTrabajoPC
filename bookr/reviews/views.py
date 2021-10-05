from django.shortcuts import render

def index(request):
    #viewvar = "Max Macavilca"
    return render(request, "base.html")
    #page 67

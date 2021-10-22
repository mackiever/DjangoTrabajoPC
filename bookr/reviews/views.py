from django.shortcuts import render

def index(request):
    #viewvar = "Max Macavilca"
    return render(request, "base.html")
    #page 67

def search_view(request):
    user_search = request.GET.get("user_search") or "Please enter a book title in order to search."
    return render(request, "search_result.html", {"search_result" : user_search})
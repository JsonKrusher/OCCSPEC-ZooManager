from django.shortcuts import render

# Create your views here.

def attractions_page(request):
    return render(request, 'about/attractions.html', {})

def facilities_page(request):
    return render(request, 'about/facilities.html', {})

def educational_visits_page(request):
    return render(request, 'about/educational-visits.html', {})

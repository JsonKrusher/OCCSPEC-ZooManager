from django.shortcuts import render

# Create your views here.

def attractions_page(request):
    # Render the page to the user
    return render(request, 'about/attractions.html', {})

def facilities_page(request):
    # Render the page to the user
    return render(request, 'about/facilities.html', {})

def educational_visits_page(request):
    # Render the page to the user
    return render(request, 'about/educational-visits.html', {})

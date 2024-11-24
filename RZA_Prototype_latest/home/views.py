from django.shortcuts import render

# Create your views here.

def index_page(request):
    # Render the page to the user
    return render(request, 'home/index.html', {})

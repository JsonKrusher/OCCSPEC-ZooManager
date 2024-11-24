from django.urls import path
from . import views


urlpatterns = [
    path('attractions', views.attractions_page, name='attractions_page'),
    path('facilities', views.facilities_page, name='facilities_page'),
    path('educational-visits', views.educational_visits_page, name='educational_visits_page'),
]

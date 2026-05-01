from django.urls import path
from twinpeak.views import home, services, how_we_work, insights, about_us, work_with_us

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('howwework', how_we_work, name='howwework'),
    path('insights', insights, name='insights'),
    path('aboutus', about_us, name='aboutus'),
    path('workwithus', work_with_us, name='workwithus'),
]

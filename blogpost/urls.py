from django.urls import path
from .views import GreetingView

app_name = "blogpost"
urlpatterns = [

    path('greet/', GreetingView.as_view(greeting="blogpost greet Good Day")),
    
]

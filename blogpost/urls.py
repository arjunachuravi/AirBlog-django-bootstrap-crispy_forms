from django.urls import path
from .views import GreetingView,postlistView

app_name = "blogpost"
urlpatterns = [

    path('greet/', GreetingView.as_view(greeting="blogpost greet Good Day")),
    path('list/', postlistView.as_view()),
    
]

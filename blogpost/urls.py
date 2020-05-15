from django.urls import path
from .views import GreetingView,blogpostView

app_name = "blogpost"
urlpatterns = [

    path('greet/', GreetingView.as_view(greeting="blogpost greet Good Day")),
    path('<int:id>/detail/',blogpostView.as_view()),

]

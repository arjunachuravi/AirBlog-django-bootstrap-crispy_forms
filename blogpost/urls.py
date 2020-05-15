from django.urls import path
from .views import GreetingView,blogpostView
from .views import postlistView,postcreateview

app_name = "blogpost"

urlpatterns = [
    
    path('greet/', GreetingView.as_view(
        greeting="blogpost greet Good Day"
    )),
    path('<int:id>/detail/',blogpostView.as_view()),
    path('list/', postlistView.as_view(),name="list"),
    path('create/', postcreateview.as_view(),name="create"),
    
]

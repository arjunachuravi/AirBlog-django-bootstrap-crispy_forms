from django.urls import path
from .views import CreateThePost,ReadThePost

app_name = "relations"

urlpatterns = [
    
    path('create/', CreateThePost.as_view(),name="create"),
    path('read/', ReadThePost.as_view(),name="read"),
]

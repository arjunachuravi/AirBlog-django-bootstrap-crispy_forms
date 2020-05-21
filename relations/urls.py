from django.urls import path
from .views import (
    CreateThePost,
    ReadThePost,
    UpdateThePost,
    DeleteThePost,
    RetriveThePost
)

app_name = "relations"

urlpatterns = [
    
    path('create/', CreateThePost.as_view(),name="create"),
    path('read/', ReadThePost.as_view(),name="read"),
    path('<int:pk>/update', UpdateThePost.as_view(),name ="update"),
    path('<int:pk>/delete', DeleteThePost.as_view(),name ="delete"),
    path('<int:pk>/detail', RetriveThePost.as_view() ,name ="detail"),

]

from django.urls import path
from .views import UserRegistration,UserSignin,user_logout,index

app_name = "authbasic"

urlpatterns = [
    
    # path('create/', postcreateview.as_view(),name="create"),
    path("index/",index,name="index"),
    path("signup/",UserRegistration.as_view(),name="signup"),
    path("signin/",UserSignin.as_view(),name="signin"),
    path("logout/",user_logout,name="logout")
    
]

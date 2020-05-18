
from django.contrib import admin
from django.urls import path,include
from .view import GreetingView

from django.conf import settings
from django.conf.urls.static import static

from blogpost import urls as blogurl

from authbasic import urls as authurl

urlpatterns = [

    path('admin/', admin.site.urls),
    path('greet/', GreetingView.as_view(greeting="Good Day")),

    path('blogpost/', include(blogurl,namespace="blogpost")),
    
    path('authbasic/',include(authurl,namespace="authbasic"))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

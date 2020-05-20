
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from authbasic import urls as authurl
from relations import urls as relurl

urlpatterns = [

    path('admin/', admin.site.urls),
   
    path('authbasic/',include(authurl,namespace="authbasic")),
    path('relations/',include(relurl,namespace="relations")),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

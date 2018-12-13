from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ventas.urls')),
    
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


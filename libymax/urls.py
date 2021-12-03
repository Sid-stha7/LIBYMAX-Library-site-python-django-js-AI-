from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('libymaxapp.urls')),
    path('admin/', admin.site.urls),
    

]

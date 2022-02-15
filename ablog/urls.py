
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # this url for admin panele
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
     path('app/', include('pages.urls')),
]

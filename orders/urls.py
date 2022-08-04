from django.contrib import admin
from django.urls  importpath, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('shops.urls', namespace='shops')),
    path('accounts/', include('allauth.urls')),
]

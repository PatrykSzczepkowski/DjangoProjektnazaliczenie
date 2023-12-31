
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("cars/", include("cars.urls")),
    path("admin/", admin.site.urls),
    path('admin-tools/', include('admin_tools.urls'),),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', view = include('polls.urls')),
    url(r'^admin/', view = admin.site.urls),
]

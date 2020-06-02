from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from MyAppIADS.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'MyAppIADS/', include('MyAppIADS.urls')),
    path(r'', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view() ,name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
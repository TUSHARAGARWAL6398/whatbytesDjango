from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your URL patterns
     path('admin/', admin.site.urls),
         path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('', include('myapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
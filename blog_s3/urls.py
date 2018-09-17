from django.urls import include, path
from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static
from posts import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home_views, name='home'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

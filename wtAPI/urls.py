from django.urls import path
from django.conf.urls.static import static
from . import settings
from APIServer.api import Test
from APIServer.context_summary import Context_summary

urlpatterns = [
    path('test', Test.as_view()),
    path('test2', Context_summary.as_view()),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)











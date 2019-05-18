from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API Lists')

from .views import JournalAPIView


urlpatterns = [
    path('',JournalAPIView.as_view()),
    url(r'^swagger/', schema_view),
]
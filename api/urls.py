from django.urls import path

from api.views import HelloApiView, SavedTest

urlpatterns = [
    path('', HelloApiView.as_view(), name='hello'),
    path('saved', SavedTest.as_view(), name='saved')
]

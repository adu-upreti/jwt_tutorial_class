from rest_framework import routers
from django.urls import path,include
from .viewsets import BookViewsets


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'book', BookViewsets,basename="BookViewsets")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
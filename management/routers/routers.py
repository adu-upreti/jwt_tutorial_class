from rest_framework.routers import DefaultRouter
from ..viewsets.sook_viewsets import sookViewsets
from ..viewsets.book_viewsets import bookViewsets


router = DefaultRouter()




router.register('sook', sookViewsets, basename="sookViewsets")
router.register('book', bookViewsets, basename="bookViewsets")

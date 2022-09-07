from rest_framework import routers
from .api import AuthorViewSet, BookViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('authors', AuthorViewSet, 'authors')

router.register('books', BookViewSet, 'books')

urlpatterns = router.urls
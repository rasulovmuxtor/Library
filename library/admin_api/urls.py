from rest_framework.routers import DefaultRouter
from admin_api.views import EbookAdminViewSet, BookAdminViewSet, StudentAdminViewSet, BorrowingAdminViewSet
from rest_framework.routers import DefaultRouter

app_name = 'admin-api'

router = DefaultRouter()

router.register('ebooks',EbookAdminViewSet,basename='ebook')
router.register('books',BookAdminViewSet,basename='book')
router.register('students',StudentAdminViewSet,basename='student')
router.register('borrowing',BorrowingAdminViewSet,basename='borrowing')

urlpatterns = router.urls
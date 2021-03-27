from rest_framework.routers import DefaultRouter
from admin_api.views import EbookAdminViewSet
from rest_framework.routers import DefaultRouter

app_name = 'admin-api'

router = DefaultRouter()

router.register('ebooks/',EbookAdminViewSet,basename='ebook')

urlpatterns = router.urls
from ebooks.views import EbookViewSet
from rest_framework.routers import DefaultRouter

app_name = 'ebooks'

router = DefaultRouter()
router.register('',EbookViewSet,basename='ebook')


urlpatterns = router.urls
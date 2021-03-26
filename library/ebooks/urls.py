from django.urls import path
from ebooks.views import EbookViewSet


app_name = 'ebooks'

ebook_list = EbookViewSet.as_view({
    'get':'list',
    'post':'create'
})

ebook_detail = EbookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('',ebook_list,name='list'),
    path('<slug:slug>/',ebook_detail,name='detail')
]
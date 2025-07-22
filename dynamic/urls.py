from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_page, name='notifications'),
    path('mark-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('get-unread-count/', views.get_unread_count, name='get_unread_count'),
]
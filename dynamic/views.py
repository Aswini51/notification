from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification

def notification_page(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})

def get_unread_count(request):
    if request.user.is_authenticated:
        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return JsonResponse({'unread_count': count})
    return JsonResponse({'unread_count': 0})
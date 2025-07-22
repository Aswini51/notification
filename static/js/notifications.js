// Fetch unread count every 30 seconds
function updateUnreadCount() {
    fetch('/notifications/get-unread-count/')
        .then(response => response.json())
        .then(data => {
            const badge = document.getElementById('unread-badge');
            if (data.unread_count > 0) {
                badge.innerText = data.unread_count;
                badge.style.display = 'inline-block';
            } else {
                badge.style.display = 'none';
            }
        });
}

// Mark notification as read
function markAsRead(notificationId) {
    fetch(`/notifications/mark-read/${notificationId}/`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    }).then(() => {
        updateUnreadCount();
        document.querySelector(`.list-group-item[onclick="markAsRead(${notificationId})"]`)
                .classList.remove('list-group-item-warning');
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateUnreadCount();
    setInterval(updateUnreadCount, 30000);  // Update every 30 seconds
});
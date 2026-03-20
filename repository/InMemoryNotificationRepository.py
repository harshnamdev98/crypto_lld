from interfaces.NotificationRepository import NotificationRepository

class InMemoryNotificationRepository(NotificationRepository):
	def __init__(self):
		self.store = {} # notification_id -> Notifications

	def save(self, notification):
		self.store[notification.id] = notification

	def update(self, notification_id, channel_type, status):
		notification = self.store.get(notification_id)

		if not notification:
			return

		for ch in notification.channels:
			if ch.channel_type == channel_type:
				ch.status = status

	def get_notification_by_status(self, status):
		result = []
		for notif in self.store.values():
			for ch in notif.channels:
				if ch.status == status:
					result.append((notif.id, ch.channel_type))
		return result

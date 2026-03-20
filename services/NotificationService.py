from factory.SenderFactory import SenderFactory
from models.models import Notification

class NotificationService:
	def __init__(self, repo):
		self.repo = repo


	def create_notification(self, notification):
		self.repo.save(notification)

	def proces_notification(self, notification: Notification):
		for channel in notification.channels:
			sender = SenderFactory.get_sender(channel.channel_type)

			try:
				sender.send(channel.payload)
				self.repo.update(notification.id, channel.channel_type, "SENT")
			except Exception:
				self.repo.update(notification.id, channel.channel_type, "FAILED")

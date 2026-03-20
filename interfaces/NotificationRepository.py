from abc import ABC, abstractmethod

class NotificationRepository(ABC):
	@abstractmethod
	def save(self, notification):
		pass

	@abstractmethod
	def update(self, id, status):
		pass

	@abstractmethod
	def get_notification_by_status(self, status):
		pass

from interfaces.NotificationSender import NotificationSender

class SmsSender(NotificationSender):
	def send(self, pyload):
		print("sending sms:", payload)

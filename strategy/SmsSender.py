from interfaces.NotificationSender import NotificationSender

class SmsSender(NotificationSender):
	def send(self, payload):
		print("sending sms:", payload)

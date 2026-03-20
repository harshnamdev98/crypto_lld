from interfaces.NotificationSender import NotificationSender

class EmailSender(NotificationSender):
	def send(self, payload):
		print("sending email:", payload)

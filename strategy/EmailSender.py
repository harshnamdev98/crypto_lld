from interfaces.NotificationSender import NotificationSender

class EmailSender(NotificationSender):
	def send(self, pyload):
		print("sending email:", payload)

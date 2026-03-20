from strategy.EmailSender import EmailSender
from strategy.SmsSender import SmsSender

class SenderFactory:
	def get_sender(channel_type):
		if channel_type == "SMS":
			return SmsSender()
		elif channel_type == "EMAIL":
			return EmailSender()

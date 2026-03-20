class Notification:
	def __init__(self, id, content):
		self.id = id
		self.content = content
		self.channels = []

class NotificationChannel:
	def __init__(self, channel_type, payload):
		self.channel_type = channel_type
		self.payload = payload
		self.status = "PENDING"
		

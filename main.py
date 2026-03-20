from repository.InMemoryNotificationRepository import InMemoryNotificationRepository
from services.NotificationService import NotificationService
from models.models import Notification, NotificationChannel

def main():
	repo = InMemoryNotificationRepository()
	service = NotificationService(repo)


	# create notification
	notification = Notification(1, "BTC Price Alert")

	# add email channel
	email_channel = NotificationChannel("EMAIL", {"email": "user1@test.com"})
	sms_channel = NotificationChannel("SMS", {"phone": "+91000029292"})


	notification.channels.append(email_channel)
	notification.channels.append(sms_channel)

	service.create_notification(notification)
	# print(notification)
	print("pending", repo.get_notification_by_status("PENDING"))


	service.process_notification(notification)

	print("failed", repo.get_notification_by_status("FAILED"))

	print("sent",repo.get_notification_by_status("SENT"))

main()

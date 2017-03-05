from __future__ import absolute_import, unicode_literals
from celery import shared_task

#Below task will send the notifications to the userids received
# user_ids: 			contain the userid to whom notifications need to be sent
#notification_payload:	contains the below elements
#{
#	'header': "Username who is sending the notification",
#	'content': "message of notfication",
#	'image_url': 'path of image'
#}

@shared_task(bind=True)
def send_notification(self,user_id, notification_payload):
	return True

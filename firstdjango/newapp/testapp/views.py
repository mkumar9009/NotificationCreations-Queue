from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Users
from testapp.forms import NotificationsForm
from testapp.tasks import send_notification

def index(request):
	form = NotificationsForm
	#execute below instructions when we are receiving the form data from user	
	if request.method == 'POST':
		form = NotificationsForm(request.POST)
		if form.is_valid():
			payload = form.save()
			users_to_send_notification = Users.objects.filter(user_type=payload.user_type)
			base_notification_payload = {
				"content": payload.content,
				"notification_time": payload.deliver_time
			}
			send_notification_to_users(users_to_send_notification, base_notification_payload)
			return HttpResponse("Notifications send in queue")			
				
	ctx = {
		'form':form
	}
	tpl = 'index.html'
	return render(request,tpl,ctx)


def send_notification_to_users(users_to_send_notification, base_notification_payload):
	for user in users_to_send_notification:
		notification_payload = {}
		notification_payload.update({
			"content": base_notification_payload["content"],
			"header": user.firstname,
			"image_url": user.user_img.url
		})
		#calling the send_notification function which is scheduled at the deliver time entered by the user
		send_notification.apply_async((user.id,notification_payload),eta=base_notification_payload["notification_time"])
	return HttpResponse("Notifcation added in the queue")
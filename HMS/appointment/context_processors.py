from hospital.models import *

def get_notification(request):
	count = Appointment.objects.filter(accepted=False).count()
	data = {
	    "count":count


	}
	return data


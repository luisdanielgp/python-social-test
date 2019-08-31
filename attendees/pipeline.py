from .models import Attendee

def save_profile(backend, user, **kwargs):
    Attendee.objects.create(
        user=user,
        first_name = kwargs['details']['first_name'],
        last_name = kwargs['details']['last_name'],
        email = kwargs['details']['email']
    )

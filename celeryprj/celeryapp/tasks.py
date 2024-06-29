from celery import shared_task
from django.core.mail import send_mail
from celeryprj import settings


@shared_task(bind=True)
def send_mail_func(self):
    #operations
        mail_subject="Hi from celery"
        message="I have completed this task by celery!!"
        to_email='sainuzsainu123@gmail.com'
        send_mail(
            subject= mail_subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
            fail_silently=False,
        )
        return "Done"


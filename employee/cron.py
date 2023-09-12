from employee import models
from send_email import settings
from datetime import date, datetime 
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_event_mail(event, employee):
    for emp in employee:
        today = date.today()
        subject = 'Happy ' + event.name
        html_message = render_to_string(event.template, {'name': emp.name})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = emp.email
        sent_success = None
        for i in range(3):
            # In case of failure, will try to send mail 3 times
            result = mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            if result == 1:
                # mail sent successfully
                sent_success = True
                log = models.log(date=today, log_message=f"SUCCESS: {event.name} mail sent to {emp.name}")
                log.save()
                break
        if not sent_success:
            # sending mail failed
            log = models.log(date=today, log_message=f"FAILURE: {event.name} mail failed to send to {emp.name}")
            log.save()


def cron_fun():
    events = models.event.objects.all()
    if not events:
        log = models.log(date=today, log_message=f"INFO: No events scheduled for today")
        log.save()
    for event in events:
        if event.repeat == "yearly":
            if event.name == 'birthday':
                employee = models.employee.objects.filter(birthday__day=datetime.now().day, birthday__month=datetime.now().month)
                send_event_mail(event, employee)
            if event.name == 'Work anniversary':
                employee = models.employee.objects.filter(joining_date__day=datetime.now().day, joining_date__month=datetime.now().month)
                send_event_mail(event, employee)
        if event.repeat == "monthly":
            # Add logic for monthly events
            pass
        if event.repeat == "daily":
            # Add logic for daily events
            pass
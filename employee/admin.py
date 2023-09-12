from django.contrib import admin
from employee.models import employee, event, log
# Register your models here.

admin.site.register(employee)
admin.site.register(event)
admin.site.register(log)
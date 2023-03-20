from django.contrib import admin
from .models import Task
from .models import SalesOrder
from .models import Payments
from .models import DateOrder


admin.site.register(Task)
admin.site.register(SalesOrder)
admin.site.register(Payments)
admin.site.register(DateOrder)


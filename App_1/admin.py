from django.contrib import admin

# Register your models here.
from .models import *

class ListGiayAdmin(admin.ModelAdmin):
    list_display = ('id', 'GiayName', 'GiayCode', 'GiaySize', 'GiayAnh', 'Borrow', 'GiayStatus', 'GiayNote', 'TimeBorrow', 'TimeReturn', 'BorrowTimes', 'TotalTimeUsing',)

admin.site.register(ListGiay, ListGiayAdmin)

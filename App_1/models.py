from django.db import models

# Create your models here.

class ListGiay(models.Model):
    id = models.AutoField(primary_key=True)
    GiayName = models.CharField(max_length = 100, null = True, blank = True)
    GiayCode = models.CharField(max_length = 20)
    GiaySize = models.IntegerField(default = 0)
    GiayAnh  = models.FileField(upload_to = "./AnhGiay")
    Borrow   = models.IntegerField(default = 0)
    GiayStatus = models.CharField(max_length = 100, null = True, blank = True)
    GiayNote   = models.CharField(max_length = 100, null = True, blank = True)
    TimeBorrow = models.DateTimeField('Time borrows', null = True, blank = True)
    TimeReturn = models.DateTimeField('Time returns', null = True, blank = True)
    BorrowTimes = models.IntegerField(default = 0)
    TotalTimeUsing = models.DateTimeField('Used time', null = True, blank = True)

    def __str__(self):
        return self.GiayCode

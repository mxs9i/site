from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Treners(models.Model) :
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}" 
    first_name = models.CharField(max_length=200, blank=True, null=False,  verbose_name='Имя тренера')
    last_name = models.CharField(max_length=200, blank=True, null=False,  verbose_name='Фамилия тренера')
    phone = models.CharField(max_length=200, blank=True, null=False,  verbose_name='Телефон тренера')
    mail = models.CharField(max_length=200, blank=True, null=False,  verbose_name='Майл тренера')
    photos = models.ImageField(null=True)

class Halls(models.Model) : 
    def __str__(self) -> str:
        return f"{self.Adres}"
    title = models.CharField(max_length=120, null=True)
    Adres = models.CharField(max_length=255, null=False)
    area = models.CharField(max_length=120)
    photos = models.ImageField(null=True)

class Abonements(models.Model) :
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    days = models.IntegerField()
    countTrenagers = models.IntegerField()

class Trenings(models.Model) :
    trener = models.ForeignKey(Treners, on_delete=models.DO_NOTHING, null=True, verbose_name= 'Тренер')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, verbose_name= 'Юзер')
    hall = models.ForeignKey(Halls, on_delete=models.DO_NOTHING, null=False, verbose_name= 'Зал')
    dt = models.DateTimeField(verbose_name= 'Дата и время')

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    company = models.CharField('Название клиента', max_length=100)

    contact_name = models.CharField('ФИО ЛПР-а', max_length=150)
    position = models.CharField('Должность', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    email = models.EmailField('Е-мэил', blank=True)
    address = models.CharField('Адрес', max_length=255)
    commentary = models.TextField('Коментарии')
    publish = models.DateTimeField('Дата создания', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_clients')

    def get_absolute_url(self):
        return f'/detail_client/{self.id}'

    def __str__(self):
        return self.company


class Deal(models.Model):
    client = models.ForeignKey(Client, related_name='deals', on_delete=models.CASCADE)
    commentary = models.TextField('Сделка')
    publish = models.DateField('Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/detail_deal/{self.id}'


class Call(models.Model):
    client = models.ForeignKey(Client, related_name='calls', on_delete=models.CASCADE)
    commentary = models.TextField('Коментарии')
    publish = models.DateField('Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/detail_call/{self.id}'


class Reminder(models.Model):
    client = models.ForeignKey(Client, related_name='reminders', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOISE_EVENT = (
        ('call', 'Звонок'),
        ('deal', 'Сделка'),
        ('meeting', 'Встреча'),
    )
    event_type = models.CharField(max_length=50, choices=CHOISE_EVENT)
    commentary = models.TextField('Коментарии')
    deadline = models.DateTimeField('Сроки')

    def get_absolute_url(self):
        return f'/detail_reminder/{self.id}'

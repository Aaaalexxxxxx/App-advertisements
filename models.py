from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#объект пользователя
User = get_user_model()

#описываем поля для будущих моделей
class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте, если торг уместен')
    created_at = models.DateTimeField('создано ', auto_now_add=True)
    updated_at = models.DateTimeField('последнее обновление', auto_now=True)
    #cascade - ссылка на пользователя (удалится пользователь - удалятся объявления)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    #изображение объявления 
    image = models.ImageField('изображение', upload_to='advertisements')
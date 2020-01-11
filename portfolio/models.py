from django.db import models
from profiles.models import Profile


class PortfolioItem(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=255, null=True,
                                 help_text='Подзаголовок написанный серым цветом.')
    short_description = models.TextField(verbose_name='Краткое описание', null=True,
                                         help_text='Краткое описание видное при просмотре в списке.')
    body = models.TextField(verbose_name='Подробное описание',
                            help_text='Полноценное описание проекта со всеми подробностями.')
    img = models.FileField(verbose_name='Картинка', upload_to='portfolio/', null=True, blank=True, help_text='Картинка')
    owner = models.ForeignKey(Profile, verbose_name='Владелец', related_name='items', null=True,
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент портфолио'
        verbose_name_plural = 'Элементы портфолио'

    def __str__(self):
        return self.title

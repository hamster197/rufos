from django.db import models
from mutagen.mp3 import MP3

class page(models.Model):
    title = models.TextField(verbose_name='“заголовок” (title)')

    def nazv(self):
        nazv = str(self.pk) + ' page'
        return nazv

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Страница (Page)'
        verbose_name_plural='Страница (Page)'



class content(models.Model):
    idd = models.ForeignKey(page, related_name='pages', verbose_name='Страница (Page)', on_delete=models.CASCADE)
    video_url = models.FileField(verbose_name='ссылка на видеофайл', upload_to='video/%Y/%m/%d', blank=False)
    video_sub_url = models.FileField(verbose_name='ссылка на файл субтитров', upload_to='video/%Y/%m/%d/sub',
                                     blank=False)
    audio_url = models.FileField(verbose_name='ссылка на аудиофайл', upload_to='audio/%Y/%m/%d', blank=False)
    text = models.TextField(verbose_name='текст', blank=False)
    counter = models.IntegerField(verbose_name='счетчик просмотров', default=0)
    title = models.TextField(verbose_name='“заголовок” (title)', blank=False)
    tip_contenta = models.CharField(verbose_name='тип контента', max_length=65, default='')

    def save(self, *args, **kwargs):
        if self.video_url:
            self.tip_contenta = 'video'
        if self.audio_url:
            self.tip_contenta = 'audio'
        if self.text:
            self.tip_contenta = 'text'
        super(content, self).save(*args, **kwargs)


    def bitrade(self):
        f = MP3(self.audio_url)
        bitrate = f.info.bitrate / 1000
        return bitrate

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Контент'
        verbose_name_plural='Контент'




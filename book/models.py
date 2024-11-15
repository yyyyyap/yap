from django.db import models
from django.contrib.auth.models import User

class Book(models.Model) :
    title = models.CharField(max_length=100, verbose_name="书名")
    description = models.TextField(verbose_name="书籍简介")
    image = models.ImageField(upload_to='book/images/', verbose_name="书籍封面" )
    url = models.URLField(blank=True, verbose_name="电子书链接")

    class Meta:
        verbose_name = "读书"
        verbose_name_plural = "读书"

class Reviews(models.Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text
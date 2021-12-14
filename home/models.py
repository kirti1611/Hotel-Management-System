from django.db import models

class Contact(models.Model):
    name=models.CharField(default='',max_length=123)
    phone=models.CharField(default='',max_length=12)
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self) -> str:
        return self.name

class HotelCard(models.Model):
    card_id=models.AutoField(primary_key=True)
    card_name=models.CharField(default='',max_length=123)
    location=models.CharField(default='',max_length=123)
    av_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="card/images",default="")

    def __str__(self) -> str:
        return self.card_name

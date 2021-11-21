from django.db import models


# Create your models here.
class TopAd(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=128,blank=True,null=True,default="javascript:void(0)")
    image = models.ImageField(upload_to='images/ads')
    display_upto = models.DateField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(TopAd, self).delete(*args, **kwargs)
        storage.delete(path)


class PostAd(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=128,blank=True,null=True,default="javascript:void(0)")
    image = models.ImageField(upload_to='images/ads')
    display_upto = models.DateField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(PostAd, self).delete(*args, **kwargs)
        storage.delete(path)


class MiddleAd(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=128,blank=True,null=True,default="javascript:void(0)")
    image = models.ImageField(upload_to='images/ads')
    display_upto = models.DateField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(MiddleAd, self).delete(*args, **kwargs)
        storage.delete(path)


class BottomAd(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=128,blank=True,null=True,default="javascript:void(0)")
    image = models.ImageField(upload_to='images/ads')
    display_upto = models.DateField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(BottomAd, self).delete(*args, **kwargs)
        storage.delete(path)

from django.db import models
class BaseModel(models.Model):
    add_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    class Meta:
        abstract = True
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    chat_id = models.IntegerField()

    first_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)

    is_admin = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f"User(chat_id={self.chat_id}, first_name={self.first_name})"


class Word(BaseModel):

    text_uz = models.CharField(max_length=31)
    text_en = models.CharField(max_length=31)

    objects = models.Manager()

    def __str__(self):
        return f"Word(pk={self.pk})"





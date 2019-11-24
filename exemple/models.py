from django.db import models

class TimesStamtedModels(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Exemple(TimesStamtedModels):
    title = models.CharField(max_length=225)
    body = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title
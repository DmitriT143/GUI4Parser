from django.db import models

# Create your models here.


class Resume(models.Model):
    ID = models.Field(help_text="resume hyperlink as its ID")



from django.db import models


class GenerateTest(models.Model):
    question = models.TextField()
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Document(models.Model):
    document = models.FileField(upload_to='document')

    def __str__(self):
        return self.document.name


class TestUpload(models.Model):
    user_id = models.IntegerField()
    pdf = models.FileField(upload_to='document/pdf_files')

    def __str__(self):
        return self.user_id

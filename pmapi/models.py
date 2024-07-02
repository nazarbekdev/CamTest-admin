from django.db import models


class PMSubjectCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PMSubjectCategory'
        verbose_name_plural = 'PMSubjectCategories'


class PMSubject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PMGenerateFile(models.Model):
    count = models.IntegerField()
    user = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} / {self.count}'


class PMDownloadFile(models.Model):
    user = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/pm_dwn_file')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} / {self.file}'


class PMCheckedFile(models.Model):
    user = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/pm_checked_file')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} / {self.file}'


class PMDatabaseFile(models.Model):
    subject = models.ForeignKey(PMSubject, on_delete=models.CASCADE)
    category = models.ForeignKey(PMSubjectCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/pm_db_file')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} / {self.category}'

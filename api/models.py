from django.db import models


class CTUser(models.Model):
    name = models.CharField(max_length=255)
    limit = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CallNumber(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Document(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.name


class SubjectTest(models.Model):
    subject_id = models.IntegerField()
    language_id = models.IntegerField()
    question = models.TextField()
    answers = models.TextField()
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class GenerateTest(models.Model):
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_1')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_2')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    number_books = models.IntegerField()
    user_id = models.ForeignKey(CTUser, on_delete=models.CASCADE, related_name='user_id')

    def __str__(self):
        return self.subject1_id


class AnswerTest(models.Model):
    book_code = models.IntegerField()
    answers = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book_code)


class UserFile(models.Model):
    user = models.ForeignKey(CTUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='tests/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CheckSheet(models.Model):
    user = models.ForeignKey(CTUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='tests/inputfile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CheckSheetResult(models.Model):
    user = models.ForeignKey(CTUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='tests/outputfile')
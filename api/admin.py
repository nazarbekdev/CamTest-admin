from django.contrib import admin
from api.models import Document, SubjectTest, Subject, Language, GenerateTest, CTUser, AnswerTest, UserFile


class AnswerTestAdmin(admin.ModelAdmin):
    search_fields = ('book_code',)
    list_display = ('book_code', 'answers')


class UserFileAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('user', 'file')


class CTUserAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'limit')


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ('document',)
    list_display = ('document', 'language', 'subject')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('question', 'subject_id', 'language_id')
    search_fields = ('question',)


admin.site.register((Subject, Language, GenerateTest))
admin.site.register(Document, DocumentAdmin)
admin.site.register(SubjectTest, SubjectAdmin)
admin.site.register(CTUser, CTUserAdmin)
admin.site.register(AnswerTest, AnswerTestAdmin)
admin.site.register(UserFile, UserFileAdmin)

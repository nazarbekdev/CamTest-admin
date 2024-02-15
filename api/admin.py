from django.contrib import admin

from api.models import GenerateTest, Document

# Register your models here.
admin.site.register((GenerateTest, Document))

from rest_framework import serializers
from api.models import Document, Subject, GenerateTest, Language, CTUser, CallNumber, CheckSheet, GenerateTestData
from api.models import UserFile


class CamTestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTUser
        fields = ('id', 'name', 'limit')


class CallNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallNumber
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GenerateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class GenerateTestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateTestData
        fields = '__all__'


class TestGeneratePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateTest
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['user', 'file']


class CheckSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckSheet
        fields = ['user', 'file', 'book_id']
        # read_only_fields = ['book_id']

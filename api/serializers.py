from rest_framework import serializers
from api.models import Document, GenerateTest, TestUpload


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GenerateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateTest
        fields = '__all__'


class GeneratePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUpload
        fields = '__all__'

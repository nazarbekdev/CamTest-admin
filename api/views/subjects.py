from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from api.models import Subject
from api.serializers import SubjectSerializer


"""
    Bu Api barcha fanlarni qaytarish uchun.
"""


class SubjectsView(GenericAPIView):
    serializer_class = SubjectSerializer

    def get(self, request):
        data = Subject.objects.all()
        data_serializer = SubjectSerializer(data, many=True)
        return Response({'data': data_serializer.data})

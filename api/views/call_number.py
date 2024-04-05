from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import CallNumber
from api.serializers import CallNumberSerializer


class CallNumberView(APIView):
    def get(self, request):
        number = CallNumber.objects.all()
        serializer = CallNumberSerializer(number, many=True)
        return Response(serializer.data)
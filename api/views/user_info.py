from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import CTUser
from api.serializers import CamTestUserSerializer  # Import your serializer


class UserInfo(APIView):

    def get(self, request, id):
        try:
            user = CTUser.objects.get(id=id)
            serializer = CamTestUserSerializer(user)  # Serialize the user object
            return Response(serializer.data)
        except CTUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

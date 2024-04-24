from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import CTUser

"""
    Bu Api CamTest apk ga birinchi bor tashfif buyurgan foydalanuvchilarni ro'yxatga olish uchun.
"""


class CamTestUserView(APIView):

    def post(self, request):
        user_name = CTUser.objects.order_by('name').last()
        user_id = user_name.id
        user_num = int(str(user_name)[2:])
        user_n = f'AA{user_num+1}'
        user_i = int(user_id) + 1
        serializer = CTUser(name=user_n)
        serializer.save()
        return Response({'id': user_i, 'name': user_n}, status=200)
        
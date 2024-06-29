import os
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.models import CheckSheet, AnswerTest, GenerateTestData, CheckSheetResult
from api.serializers import CheckSheetSerializer
from api.functions.test_api import omr_response, compare_answers
from api.functions.result import PDF


class CheckSheetView(GenericAPIView):
    serializer_class = CheckSheetSerializer
    queryset = CheckSheet.objects.all()

    def post(self, request):
        serializer = CheckSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = CheckSheet.objects.latest('created_at')
            user_id = user_data.user
            user_file_url = user_data.file
            user_book_id = user_data.book_id

            if user_book_id == '':
                data_resp = omr_response(user_file_url.url)  # Use the URL for processing the image
                user_answer = data_resp['testResult']
                book_id = data_resp['id']
                language = data_resp['language']
                book_number = ''.join(book_id)
                if len(book_number) == 7:
                    """ Agarda book_number uzunligi 7 ga teng bo'lsagina abiturent 
                        tomonidan belgilangan javoblar varaqasi to'g'ri bo'yalgan deb qaraladi, 
                        aksi bo'lsa (7 ga teng bo'lmasa) bu javoblar varaqasini kitob id si qo'lda
                        kiritilgan holatda teshrilishi kerak bo'ladi.
                    """
                    try:
                        data_ans = AnswerTest.objects.get(book_code=int(book_number))
                        correct_answers = data_ans.answers
                        result_compare = compare_answers(user_answer, correct_answers)
                        get_subjects = GenerateTestData.objects.get(number_books=int(book_number))
                        subject1 = get_subjects.subject1
                        subject2 = get_subjects.subject2
                        result_compare['subject1'] = subject1
                        result_compare['subject2'] = subject2
                        # Get the path of the image file
                        image_path = user_file_url.path  # Use .path to get the filesystem path
                        if not os.path.exists(image_path):
                            raise FileNotFoundError(f"Rasm fayli mavjud emas: {image_path}")
                        result_compare['image_path'] = image_path
                        result_compare['book_number'] = book_number
                        file = PDF.pdf_create(result_compare, language)
                        check_sheet = CheckSheetResult(user=user_id.name, file=f"check_file/outputfile/{file}")
                        check_sheet.save()
                        result = {'success': True}
                    except Exception as e:
                        result = {'success': False, 'error': str(e), 'message': 'xatolik'}
                else:
                    result = {'success': False,
                              'message': "Ehtimol test kitobcha raqami noto'g'ri bo'yalgan. "
                                         "Test kitobcha raqamini qo'lda kiritib tekshirib ko'ring!"}
                return Response(result, status=200)
            else:
                try:
                    data_resp = omr_response(user_file_url.url)  # Use the URL for processing the image
                    user_answer = data_resp['testResult']
                    language = data_resp['language']
                    if len(user_book_id) == 7:
                        data_ans = AnswerTest.objects.get(book_code=int(user_book_id))
                        correct_answers = data_ans.answers
                        result_compare = compare_answers(user_answer, correct_answers)
                        print('user name: ', user_id.name)
                        get_subjects = GenerateTestData.objects.get(number_books=int(user_book_id))
                        subject1 = get_subjects.subject1
                        subject2 = get_subjects.subject2
                        result_compare['subject1'] = subject1
                        result_compare['subject2'] = subject2

                        # Get the path of the image file
                        image_path = user_file_url.path  # Use .path to get the filesystem path
                        if not os.path.exists(image_path):
                            raise FileNotFoundError(f"Rasm fayli mavjud emas: {image_path}")
                        result_compare['image_path'] = image_path
                        result_compare['book_number'] = user_book_id
                        file = PDF.pdf_create(result_compare, language)

                        check_sheet = CheckSheetResult(user=user_id.name, file=f"check_file/outputfile/{file}")
                        check_sheet.save()
                        result = {'success': True}
                    else:
                        result = {'success': False,
                                  'message': "Iltimos, test kitob raqamini to'g'ri kiriting!"}
                except Exception as e:
                    result = {'success': False, 'error': str(e)}
                return Response(result, status=200)
        return Response(serializer.errors, status=400)

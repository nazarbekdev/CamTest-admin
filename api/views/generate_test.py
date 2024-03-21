import os
import random
from PyPDF2 import PdfReader, PdfWriter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from api.functions.merge_pdf import merge_pdf
from api.functions.placement_of_numbers import placement_of_numbers
from api.functions.random_name import generate_random_name
from api.functions.revome_file import revome_file
from api.models import SubjectTest, Subject, AnswerTest, UserFile
from api.serializers import TestGeneratePDFSerializer


"""
    Bu Api foydalanuvchi tomonidan talab qilingan fanlan majmuasi uchun test generatsiya qilish uchun.
"""

styles = getSampleStyleSheet()
custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=10)
custom_style1 = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=15)


class GenerateTest(GenericAPIView):
    serializer_class = TestGeneratePDFSerializer

    def add_subject_heading(self, elements, subject_name):
        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)
        elements.append(Paragraph(subject_name, centered_style))
        elements.append(Spacer(1, 20))

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        maj_ona_tili = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=3).order_by('?')[
                       :10]
        maj_matem = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=4).order_by('?')[
                    :10]
        maj_tarix = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=5).order_by('?')[
                    :10]
        sub_1 = SubjectTest.objects.filter(language_id=serializer.data['language'],
                                           subject_id=serializer.data['subject1']).order_by('?')[:30]
        sub_2 = SubjectTest.objects.filter(language_id=serializer.data['language'],
                                           subject_id=serializer.data['subject2']).order_by('?')[:30]
        number_books = serializer.data['number_books']
        user_name = serializer.data['user_id']

        file_path = 'subject_test.pdf'
        pdf = SimpleDocTemplate(file_path, pagesize=letter)
        elements = []

        subject_name1 = Subject.objects.get(pk=serializer.data['subject1']).name
        subject_name2 = Subject.objects.get(pk=serializer.data['subject2']).name

        subject_list = ['Majburiy Fanlar Ona tili', 'Matematika', 'Tarix', subject_name1, subject_name2]
        subjects = [maj_ona_tili, maj_matem, maj_tarix, sub_1, sub_2]

        numbering_ranges = [range(1, 11), range(11, 21), range(21, 31), range(31, 61), range(61, 91)]
        all_tests = []
        full_answers = []
        start_index = 0
        end_index = 90
        for num in range(number_books):
            for subject_name, tests, numbering_range in zip(subject_list, subjects, numbering_ranges):
                self.add_subject_heading(elements, subject_name)

                for i, test in enumerate(tests):
                    test_text = f"{numbering_range[i]}. {test.question.replace('@', '')}\n\n" if '@' in test.question else f"{numbering_range[i]}. {test.question}\n\n"
                    elements.append(Spacer(1, 5))
                    elements.append(Paragraph(test_text, custom_style))
                    if test.image:
                        print('test image path:   ', test.image)
                        test_image = Image(f'/home/nazarbek/CamTest-admin/{test.image}', width=110, height=70)
                        elements.append(test_image)
                        elements.append(Spacer(1, 20))

                    len_ = len(test.answers) - 1
                    tests_ = test.answers[:len_]
                    shuffled_answers = random.sample(tests_.split('#'), len(tests_.split('#')))
                    if shuffled_answers[0] == test.answer:
                        f_a = {
                            numbering_range[i]: 'A'
                        }
                        full_answers.append(f_a)
                    elif shuffled_answers[1] == test.answer:
                        f_a = {
                            numbering_range[i]: 'B'
                        }
                        full_answers.append(f_a)
                    elif shuffled_answers[2] == test.answer:
                        f_a = {
                            numbering_range[i]: 'C'
                        }
                        full_answers.append(f_a)
                    elif shuffled_answers[3] == test.answer:
                        f_a = {
                            numbering_range[i]: 'D'
                        }
                        full_answers.append(f_a)
                    else:
                        f_a = {
                            numbering_range[i]: 'Null'
                        }
                        full_answers.append(f_a)
                    answers_str = f"A) {shuffled_answers[0]}\n\nB) {shuffled_answers[1]}\n\nC) {shuffled_answers[2]}\n\nD) {shuffled_answers[3]}\n\n"

                    elements.append(Paragraph(answers_str, custom_style))
                    # elements.append(Spacer(1, 5))
                elements.append(Spacer(1, 20))

            pdf.build(elements)

            data_muqova = placement_of_numbers()
            muqova = data_muqova[0]
            test = 'subject_test.pdf'

            def merge_pdfs(input_paths, output_path):
                pdf_writer = PdfWriter()

                for path in input_paths:
                    with open(path, 'rb') as file:
                        pdf_reader = PdfReader(file)
                        for page in pdf_reader.pages:
                            pdf_writer.add_page(page)

                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)

            all_tests.append(f'camtest-{subject_name1}-{subject_name2}{num+1}.pdf')

            # Fayllarni birlashtirish va yangi faylni saqlash
            merge_pdfs([muqova, test], f'camtest-{subject_name1}-{subject_name2}{num+1}.pdf')
            os.remove(file_path)

            book_code = data_muqova[1]
            answer = AnswerTest(book_code=book_code, answers=full_answers[start_index:end_index])
            answer.save()
            start_index += 90
            end_index += 90

        # barcha generatsiya bo'lgan test fayllarini birlashtirish
        test_book_name = generate_random_name()
        merge_pdf(all_tests, f'/home/nazarbek/CamTest-admin/tests/{test_book_name}.pdf')
        data = UserFile(user_id=user_name, file=f'{test_book_name}.pdf')
        data.save()

        revome_file(all_tests)
        return Response({'status': 'success'})

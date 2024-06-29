import os
import random
from PyPDF2 import PdfReader, PdfWriter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from api.functions.draw_horizoltal_line import draw_horizontal_line
from api.functions.merge_pdf import merge_pdf
from api.functions.placement_of_numbers import placement_of_numbers
from api.functions.random_name import generate_random_name
from api.functions.revome_file import revome_file
from api.models import SubjectTest, Subject, AnswerTest, UserFile, CTUser, GenerateTest
from api.serializers import TestGeneratePDFSerializer

"""
    Bu Api foydalanuvchi tomonidan talab qilingan fanlan majmuasi uchun test generatsiya qilish uchun.
"""

styles = getSampleStyleSheet()
custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontName='Times-Roman', fontSize=10)
custom_style.spaceAfter = 1


class GenerateTestView(GenericAPIView):
    serializer_class = TestGeneratePDFSerializer

    def add_subject_heading(self, elements, subject_name):
        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)
        elements.append(Paragraph(subject_name, centered_style))
        elements.append(Spacer(1, 10))

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Majburiy fanlar
        maj_ona_tili = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=1).order_by('?')[
                       :10]
        maj_matem = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=2).order_by('?')[:10]
        maj_tarix = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=3).order_by('?')[:10]

        # Boshqa tanlangan fanlar
        sub_1 = SubjectTest.objects.filter(language_id=serializer.data['language'],
                                           subject_id=serializer.data['subject1']).order_by('?')[:30]
        sub_2 = SubjectTest.objects.filter(language_id=serializer.data['language'],
                                           subject_id=serializer.data['subject2']).order_by('?')[:30]
        # Kitoblar soni va user id
        number_books = serializer.data['number_books']
        user_name = serializer.data['user_id']

        # Barcha generatsiya testlarni yozish uchun pdf file ochish
        file_path = 'subject_test.pdf'
        pdf = SimpleDocTemplate(file_path, pagesize=letter, leftMargin=20, bottomMargin=20, rightMargin=10,
                                topMargin=25)
        elements = []

        # # Sahifa shabloni
        # frame1 = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width / 2 - 6, pdf.height, id='col1')
        # frame2 = Frame(pdf.width / 2 + 80, pdf.bottomMargin, pdf.width / 2 - 6, pdf.height, id='col2')
        #
        # # Sahifa shablonini yaratish
        # template = PageTemplate(id='twoColumn', frames=[frame1, frame2])
        # pdf.addPageTemplates([template])

        # Asosiy fanlar nomini olish
        subject_name1 = Subject.objects.get(pk=serializer.data['subject1']).name
        subject_name2 = Subject.objects.get(pk=serializer.data['subject2']).name

        subject_list = ['Ona tili', 'Matematika', 'Tarix', subject_name1, subject_name2]
        subjects = [maj_ona_tili, maj_matem, maj_tarix, sub_1, sub_2]

        numbering_ranges = [range(1, 11), range(11, 21), range(21, 31), range(31, 61), range(61, 91)]
        all_tests = []
        full_answers = []
        start_index = 0
        end_index = 90

        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)

        # user limitini olish
        user_limit = CTUser.objects.get(id=user_name)

        if user_limit.limit >= number_books:
            user_limit.limit -= number_books
            user_limit.save()
            for num in range(number_books):
                elements.append(Paragraph('Majburiy Fanlar', centered_style))
                for subject_name, tests, numbering_range in zip(subject_list, subjects, numbering_ranges):
                    self.add_subject_heading(elements, subject_name)

                    for i, test in enumerate(tests):

                        if test.answers != '?':
                            test_text = f"{numbering_range[i]}. {test.question.replace('@', '')}\n\n" if '@' in test.question else f"{numbering_range[i]}. {test.question}\n\n"
                            elements.append(Spacer(1, 5))
                            elements.append(Paragraph(test_text, custom_style))
                            if test.image:
                                test_image = Image(f'/home/nazarbek/CamTest-admin/{test.image}', width=120, height=70)
                                elements.append(Spacer(1, 10))
                                elements.append(test_image)
                                elements.append(Spacer(1, 15))

                            tests_ = test.answers

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
                            if len(test.answer) <= 30:
                                elements.append(Spacer(1, 2))
                                elements.append(Paragraph(
                                    f"A) {shuffled_answers[0]}  B) {shuffled_answers[1]}  C) {shuffled_answers[2]}  D) {shuffled_answers[3]}",
                                    custom_style))
                            elif len(test.answer) > 30:
                                elements.append(Spacer(1, 2))
                                elements.append(
                                    Paragraph(f"A) {shuffled_answers[0]}  C) {shuffled_answers[2]}", custom_style))
                                elements.append(
                                    Paragraph(f"B) {shuffled_answers[1]}  D) {shuffled_answers[3]}", custom_style))

                        else:
                            test_text = f"{numbering_range[i]}."
                            elements.append(Spacer(1, 3))
                            elements.append(Paragraph(test_text, custom_style))
                            elements.append(Spacer(1, 5))
                            test_image = Image(f'/home/nazarbek/CamTest-admin/{test.image}', width=200, height=120)
                            elements.append(test_image)
                            elements.append(Spacer(1, 10))

                            f_a = {
                                numbering_range[i]: test.answer
                            }
                            full_answers.append(f_a)

                    elements.append(Spacer(1, 20))

                pdf.build(elements)

                data_muqova = placement_of_numbers()
                muqova = data_muqova[0]
                test = 'subject_test.pdf'
                test_res = 'draw_horizontal_line.pdf'
                draw_horizontal_line(test, test_res)

                def merge_pdfs(input_paths, output_path):
                    pdf_writer = PdfWriter()

                    for path in input_paths:
                        with open(path, 'rb') as file:
                            pdf_reader = PdfReader(file)
                            for page in pdf_reader.pages:
                                pdf_writer.add_page(page)

                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)

                all_tests.append(f'camtest-{subject_name1}-{subject_name2}{num + 1}.pdf')

                # Fayllarni birlashtirish va yangi faylni saqlash
                merge_pdfs([muqova, test_res], f'camtest-{subject_name1}-{subject_name2}{num + 1}.pdf')
                os.remove(file_path)
                os.remove(test_res)

                book_code = data_muqova[1]
                answer = AnswerTest(book_code=book_code, answers=full_answers[start_index:end_index])
                answer.save()
                start_index += 90
                end_index += 90

            # barcha generatsiya bo'lgan test fayllarini birlashtirish
            test_book_name = generate_random_name()
            merge_pdf(all_tests, f'/home/nazarbek/CamTest-admin/tests/{test_book_name}.pdf')
            data = UserFile(user_id=user_name, file=f'tests/{test_book_name}.pdf')
            data.save()

            # generate_test = GenerateTest(subject1=serializer.data['subject1'], subject2=serializer.data[
            # 'subject2'], language=serializer.data['language'], number_books=number_books, user_id=user_name)
            # generate_test.save()
            revome_file(all_tests)
            os.remove('qr_code.png')
            return Response({'success': True})
        else:
            return Response({'success': False, 'message': 'Sizda yetarlicha limit mavjud emas!'})

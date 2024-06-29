import os
import json
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
from api.models import SubjectTest, Subject, AnswerTest, UserFile, CTUser, GenerateTestData, Language
from api.serializers import TestGeneratePDFSerializer

"""
    Bu Api foydalanuvchi tomonidan talab qilingan fanlan majmuasi uchun test generatsiya qilish uchun.
"""

styles = getSampleStyleSheet()
custom_style = ParagraphStyle(name='CustomStyle', parent=styles['Normal'], fontName='Times-Roman', fontSize=10)
custom_style.spaceAfter = 1


class GenerateTestDefaultKey(GenericAPIView):
    serializer_class = TestGeneratePDFSerializer

    def add_subject_heading(self, elements, subject_name):
        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)
        elements.append(Paragraph(subject_name, centered_style))
        elements.append(Spacer(1, 10))

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Majburiy fanlar
        maj_ona_tili = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=3).order_by('?')[
                       :10]
        maj_matem = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=4).order_by('?')[:10]
        maj_tarix = SubjectTest.objects.filter(language_id=serializer.data['language'], subject_id=5).order_by('?')[:10]

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
        # frame1 = Frame(pdf.leftMargin - 40, pdf.bottomMargin - 80, pdf.width / 2 - 80, pdf.height + 140, id='col1')
        # frame2 = Frame(pdf.width / 2 + 80, pdf.bottomMargin - 40, pdf.width / 2 - 80, pdf.height + 20, id='col2')
        #
        # # Sahifa shablonini yaratish
        # template = PageTemplate(id='twoColumn', frames=[frame1])
        # pdf.addPageTemplates([template])

        # Asosiy fanlar nomini olish
        subject_name1 = Subject.objects.get(pk=serializer.data['subject1']).name
        subject_name2 = Subject.objects.get(pk=serializer.data['subject2']).name
        language_name = Language.objects.get(pk=serializer.data['language']).name
        user = CTUser.objects.get(pk=serializer.data['user_id']).name

        subject_list = ['Ona tili', 'Matematika', 'Tarix', subject_name1, subject_name2]
        subjects = [maj_ona_tili, maj_matem, maj_tarix, sub_1, sub_2]

        numbering_ranges = [range(1, 11), range(11, 21), range(21, 31), range(31, 61), range(61, 91)]
        all_tests = []

        centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Title'], alignment=1)

        # user   limitini olish
        user_limit = CTUser.objects.get(id=user_name)

        # default key lar
        keys = {
            "1": "C", "2": "C", "3": "A", "4": "C", "5": "A", "6": "B", "7": "D", "8": "B", "9": "B", "10": "D",
            "11": "D", "12": "B", "13": "D", "14": "B", "15": "A", "16": "A", "17": "B", "18": "B", "19": "D",
            "20": "B",
            "21": "C", "22": "A", "23": "B", "24": "A", "25": "C", "26": "B", "27": "A", "28": "C", "29": "B",
            "30": "B",
            "31": "D", "32": "A", "33": "B", "34": "B", "35": "A", "36": "C", "37": "A", "38": "A", "39": "B",
            "40": "B",
            "41": "D", "42": "C", "43": "B", "44": "A", "45": "A", "46": "B", "47": "D", "48": "D", "49": "D",
            "50": "A",
            "51": "A", "52": "C", "53": "C", "54": "C", "55": "A", "56": "B", "57": "A", "58": "D", "59": "A",
            "60": "B",
            "61": "D", "62": "A", "63": "B", "64": "B", "65": "A", "66": "C", "67": "A", "68": "A", "69": "B",
            "70": "B",
            "71": "D", "72": "C", "73": "B", "74": "A", "75": "A", "76": "B", "77": "D", "78": "D", "79": "D",
            "80": "A",
            "81": "A", "82": "C", "83": "C", "84": "C", "85": "A", "86": "B", "87": "A", "88": "D", "89": "A", "90": "B"
        }
        answers_json = json.dumps(keys, indent=4)

        # User limitini tekshirish
        if user_limit.limit >= number_books:
            user_limit.limit -= number_books
            user_limit.save()

            # Kitoblar soni bo'yicha generatsiya qilish
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
                                test_image = Image(f'/home/nazarbek/CamTest-admin/{test.image}', width=100, height=60)
                                elements.append(Spacer(1, 10))
                                elements.append(test_image)
                                elements.append(Spacer(1, 10))

                            tests_ = test.answers
                            answers = tests_.split('#')
                            answer_ = test.answer
                            answer = answer_.replace('\n', '')
                            answers_lst = []
                            for k in answers:
                                ans_ = k.replace('\n', '')
                                ans = ans_.strip(' ')
                                if ans != answer.strip(' '):
                                    answers_lst.append(ans)
                            answers_set = list(set(answers_lst))
                            key = str(numbering_range[i])
                            if keys[key] == 'A':
                                if len(answer) <= 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answer} B) {answers_set[0]} C) {answers_set[1]} D) {answers_set[2]}",
                                        custom_style))
                                elif len(answer) > 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answer}  C) {answers_set[1]}", custom_style))
                                    elements.append(
                                        Paragraph(f"B) {answers_set[0]}  D) {answers_set[2]}", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                            elif keys[key] == 'B':
                                if len(answer) <= 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_set[0]} B) {answer} C) {answers_set[1]} D) {answers_set[2]}",
                                        custom_style))
                                elif len(answer) > 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answers_set[0]}  C) {answers_set[1]}", custom_style))
                                    elements.append(Paragraph(f"B) {answer}  D) {answers_set[2]}", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                            elif keys[key] == 'C':
                                if len(answer) <= 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_set[0]} B) {answers_set[1]} C) {answer} D) {answers_set[2]}",
                                        custom_style))
                                elif len(answer) > 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(f"A) {answers_set[0]}  C) {answer} ", custom_style))
                                    elements.append(
                                        Paragraph(f"B) {answers_set[1]}  D) {answers_set[2]}", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                            elif keys[key] == 'D':
                                if len(answer) <= 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(Paragraph(
                                        f"A) {answers_set[0]} B) {answers_set[1]} C) {answers_set[2]} D) {answer}",
                                        custom_style))
                                elif len(answer) > 30:
                                    elements.append(Spacer(1, 2))
                                    elements.append(
                                        Paragraph(f"A) {answers_set[0]}  C) {answers_set[2]}", custom_style))
                                    elements.append(Paragraph(f"B) {answers_set[1]}  D) {answer}", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                                    # elements.append(Paragraph(f"", custom_style))
                            else:
                                elements.append(Spacer(1, 3))
                                elements.append(Paragraph(f"None"))
                        else:
                            test_text = f"{numbering_range[i]}."
                            elements.append(Spacer(1, 3))
                            elements.append(Paragraph(test_text, custom_style))
                            elements.append(Spacer(1, 5))
                            test_image = Image(f'/home/nazarbek/CamTest-admin/{test.image}', width=200, height=120)
                            elements.append(test_image)
                            elements.append(Spacer(1, 10))

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
                answer_db = AnswerTest(book_code=book_code, answers=answers_json)
                answer_db.save()

            # Barcha generatsiya bo'lgan test fayllarini birlashtirish
            test_book_name = generate_random_name()
            merge_pdf(all_tests, f'/home/nazarbek/CamTest-admin/media/userfile/{test_book_name}.pdf')
            data = UserFile(user_id=user_name, file=f'userfile/{test_book_name}.pdf')
            data.save()
            generate_data = GenerateTestData(subject1=subject_name1, subject2=subject_name2,
                                             language=language_name, number_books=book_code,
                                             user=user)
            generate_data.save()

            revome_file(all_tests)
            os.remove('qr_code.png')
            return Response({'success': True})
        else:
            return Response({'success': False, 'message': 'Sizda yetarlicha limit mavjud emas!'})

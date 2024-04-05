import fitz  # PyMuPDF
import random
from api.functions.qr_code import qr_code_img

"""
    Bu funksiya: DTM muqova faylini shakklantirish uchun qo'llaniladi.
    Qaytadigan qiymatlar: shakllangan muqova.pdf fayl va test kitob raqami.
"""


def placement_of_numbers():
    pdf_path = '/home/nazarbek/CamTest-admin/media/files/MUQOVA.pdf'
    image_path = '/home/nazarbek/CamTest-admin/media/files/qora_nuqta.jpg'
    pdf_page = fitz.open(pdf_path)
    page = pdf_page[0]
    book_number = str(random.randint(1000000, 3000000))

    first_column = {1: '61.5/358.8', 2: '61.5/372.5', 3: '61.5/386.3', 4: '61.5/400', 5: '61.5/413.3', 6: '61.5/426.5',
                    7: '61.5/440.5', 8: '61.5/454', 9: '61.5/467.5', 0: '61.5/481.5', 'b_n': '55/382'}
    second_column = {1: '82/358.8', 2: '82.4/372.5', 3: '82.4/386.3', 4: '82.4/400', 5: '82.4/413.3', 6: '82.4/426.5',
                     7: '82.4/440.5', 8: '82.4/454', 9: '82.4/467.5', 0: '82.4/481.5', 'b_n': '75/382'}
    third_column = {1: '103/358.8', 2: '103/372.5', 3: '103/386.3', 4: '103/400', 5: '103/413.3', 6: '103/426.5',
                    7: '103/440.5', 8: '103/454', 9: '103/467.5', 0: '103/481.5', 'b_n': '95/382'}
    fourth_column = {1: '123.4/358.8', 2: '123.4/372.5', 3: '123.4/386.3', 4: '123.4/400', 5: '123.4/413.3',
                     6: '123.4/426.5',
                     7: '123.4/440.5', 8: '123.4/454', 9: '123.4/467.5', 0: '123.4/481.5', 'b_n': '115/382'}
    fifth_column = {1: '143.7/358.8', 2: '143.7/372.5', 3: '143.7/386.3', 4: '143.7/400', 5: '143.7/413.3',
                    6: '143.7/426.5',
                    7: '143.7/440.5', 8: '143.7/454', 9: '143.7/467.5', 0: '143.7/481.5', 'b_n': '135/382'}
    sixth_column = {1: '163.5/358.8', 2: '163.5/372.5', 3: '163.5/386.3', 4: '163.5/400', 5: '163.5/413.3',
                    6: '163.5/426.5',
                    7: '163.5/440.5', 8: '163.5/454', 9: '163.5/467.5', 0: '163.5/481.5', 'b_n': '155/382'}
    seventh_column = {1: '182/358.8', 2: '182/372.5', 3: '182/386.3', 4: '182/400', 5: '182/413.3', 6: '182/426.5',
                      7: '182/440.5', 8: '182/454', 9: '182/467.5', 0: '182/481.5', 'b_n': '175/382'}

    for i in range(7):
        if i == 0:
            book_num = int(book_number[i])
            x = float(first_column[book_num].split('/')[0])
            y = float(first_column[book_num].split('/')[1])

            x1 = float(first_column['b_n'].split('/')[0])
            y1 = float(first_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 1:
            book_num = int(book_number[i])
            x = float(second_column[book_num].split('/')[0])
            y = float(second_column[book_num].split('/')[1])

            x1 = float(second_column['b_n'].split('/')[0])
            y1 = float(second_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 2:
            book_num = int(book_number[i])
            x = float(third_column[book_num].split('/')[0])
            y = float(third_column[book_num].split('/')[1])

            x1 = float(third_column['b_n'].split('/')[0])
            y1 = float(third_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 3:
            book_num = int(book_number[i])
            x = float(fourth_column[book_num].split('/')[0])
            y = float(fourth_column[book_num].split('/')[1])

            x1 = float(fourth_column['b_n'].split('/')[0])
            y1 = float(fourth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 4:
            book_num = int(book_number[i])
            x = float(fifth_column[book_num].split('/')[0])
            y = float(fifth_column[book_num].split('/')[1])

            x1 = float(fifth_column['b_n'].split('/')[0])
            y1 = float(fifth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 5:
            book_num = int(book_number[i])
            x = float(sixth_column[book_num].split('/')[0])
            y = float(sixth_column[book_num].split('/')[1])

            x1 = float(sixth_column['b_n'].split('/')[0])
            y1 = float(sixth_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 6:
            book_num = int(book_number[i])
            x = float(seventh_column[book_num].split('/')[0])
            y = float(seventh_column[book_num].split('/')[1])

            x1 = float(seventh_column['b_n'].split('/')[0])
            y1 = float(seventh_column['b_n'].split('/')[1])

            rect = fitz.Rect(x - 51, y + 46, x + 50, y + 60)
            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        else:
            print('Xatolik bor!!!')

    x = 115
    y = 157

    x1 = 140
    y1 = -20

    rect = fitz.Rect(x, y, x + 200, y + 50)
    page.insert_textbox(rect, book_number, fontsize=18, fill=(0, 0, 0))

    qr_code_image = qr_code_img(book_number)
    rect = fitz.Rect(x1 - 70, y1 + 50, x1 + 40, y1 + 150)
    page.insert_image(rect, filename=qr_code_image)

    pdf_page.save('/home/nazarbek/CamTest-admin/media/files/muqova.pdf')
    pdf_page.close()

    result = ['/home/nazarbek/CamTest-admin/media/files/muqova.pdf', book_number]

    return result

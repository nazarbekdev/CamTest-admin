import fitz  # PyMuPDF
import random
from api.functions.qr_code import qr_code_img

"""
    Bu funksiya: DTM muqova faylini shakklantirish uchun qo'llaniladi.
    Qaytadigan qiymatlar: shakllangan muqova.pdf fayl va test kitob raqami.
"""


def placement_of_numbers():
    pdf_page = fitz.open(pdf_path)
    page = pdf_page[0]
    book_number = str(random.randint(1000000, 5000000))


    for i in range(7):
        if i == 0:
            book_num = int(book_number[i])
            x = float(first_column[book_num].split('/')[0])
            y = float(first_column[book_num].split('/')[1])

            x1 = float(first_column['b_n'].split('/')[0])
            y1 = float(first_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 1:
            book_num = int(book_number[i])
            x = float(second_column[book_num].split('/')[0])
            y = float(second_column[book_num].split('/')[1])

            x1 = float(second_column['b_n'].split('/')[0])
            y1 = float(second_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 2:
            book_num = int(book_number[i])
            x = float(third_column[book_num].split('/')[0])
            y = float(third_column[book_num].split('/')[1])

            x1 = float(third_column['b_n'].split('/')[0])
            y1 = float(third_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 3:
            book_num = int(book_number[i])
            x = float(fourth_column[book_num].split('/')[0])
            y = float(fourth_column[book_num].split('/')[1])

            x1 = float(fourth_column['b_n'].split('/')[0])
            y1 = float(fourth_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 4:
            book_num = int(book_number[i])
            x = float(fifth_column[book_num].split('/')[0])
            y = float(fifth_column[book_num].split('/')[1])

            x1 = float(fifth_column['b_n'].split('/')[0])
            y1 = float(fifth_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 5:
            book_num = int(book_number[i])
            x = float(sixth_column[book_num].split('/')[0])
            y = float(sixth_column[book_num].split('/')[1])

            x1 = float(sixth_column['b_n'].split('/')[0])
            y1 = float(sixth_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        elif i == 6:
            book_num = int(book_number[i])
            x = float(seventh_column[book_num].split('/')[0])
            y = float(seventh_column[book_num].split('/')[1])

            x1 = float(seventh_column['b_n'].split('/')[0])
            y1 = float(seventh_column['b_n'].split('/')[1])

            page.insert_image(rect, filename=image_path)

            rect_ = fitz.Rect(x1, y1, x1 + 200, y1 + 50)
            page.insert_textbox(rect_, str(book_num), fontsize=18, fill=(0, 0, 0))
        else:
            print('Xatolik bor!!!')


    x1 = 140
    y1 = -20

    rect = fitz.Rect(x, y, x + 200, y + 50)
    page.insert_textbox(rect, book_number, fontsize=16, fill=(0, 0, 0))

    qr_code_image = qr_code_img(book_number)
    rect = fitz.Rect(x1 - 70, y1 + 50, x1 + 40, y1 + 150)
    page.insert_image(rect, filename=qr_code_image)

    pdf_page.close()



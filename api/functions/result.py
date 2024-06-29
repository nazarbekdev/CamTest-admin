from fpdf import FPDF
import requests
from datetime import datetime
from api.functions.qr_code import qr_code_img
from api.functions.score_calculation import score_calculator
import shutil
import os


def get_picture(photo_url):  # aligned_image_{chat_id}.jpg
    response = requests.get(photo_url)
    if response.status_code == 200:
        with open("detection/convertor/image_1.jpg", 'wb') as image_file:
            image_file.write(response.content)
    return True


class PDF(FPDF):
    @staticmethod
    def pdf_create(data, language):
        blok_1 = data['subject1']
        blok_2 = data['subject2']
        personid = data['book_number']
        compulsory_sub_ans, sub1_ans, sub2_ans = data['find_ans'][0], data['find_ans'][1], data['find_ans'][2]
        file = data['image_path']
        now = datetime.now().strftime("%d.%m.%Y")

        data_calculator = score_calculator(compulsory_sub_ans, sub1_ans, sub2_ans, language, blok_1, blok_2)
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Arial', size=11)
        pdf.set_text_color(63, 51, 255)
        pdf.text(138, 9, txt="Chop etilgan sanasi: {}".format(now))
        pdf.set_font("Arial", size=12, style='I')
        pdf.set_text_color(255, 0, 0)
        if data_calculator['description'] != '':
            pdf.text(25, 240, txt="{}".format(data_calculator['description']))
            pdf.text(25, 245, txt="Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.")
            pdf.text(25, 250, txt="Abiturentlardan hushyorlikni so'rab qolamiz!")
        else:
            pdf.text(10, 240, txt="")

        pdf.set_font("Arial", size=12, style='B')
        pdf.set_text_color(0, 0, 0)
        pdf.line(10, 12, 195, 12)  # Parameters: (start_x, start_y, end_x, end_y)
        photo_path = file
        qr_path = qr_code_img(personid)
        pdf.text(10, 240, txt='*Izoh:')
        pdf.text(10, 20, txt="Id raqam:   {}".format(personid))
        pdf.text(10, 26, txt="Birinchi blok:   {}".format(blok_1))
        pdf.text(10, 32, txt="Ikkinchi blok:   {}".format(blok_2))
        pdf.text(10, 40, txt="To'g'ri javoblar:   {}".format(data_calculator['correct']))
        pdf.text(10, 46, txt="Noto'g'ri javoblar:   {}".format(data_calculator['incorrect']))
        pdf.text(10, 54, txt="Umumiy ball:  {}".format(int(data_calculator['ball'])))
        pdf.image(photo_path, x=10, y=58, w=120, h=170)
        pdf.image(qr_path, x=160, y=15, w=30, h=30)
        pdf.text(165, 48, txt="#{}".format(personid))
        pdf.set_font("Arial", size=11, style='B')
        ans_cor, counter = 65, 1  # answer coordinate, counter
        os.remove(qr_path)
        if data_calculator['lan_status'] == 1:
            for i in range(30, 60):
                data['result'][i] = ['-', 1]
        elif data_calculator['lan_status'] == 2:
            for i in range(60, 90):
                data['result'][i] = ['-', 1]
        elif data_calculator['lan_status'] == 0:
            for i in range(30, 90):
                data['result'][i] = ['-', 0]

        for item in data['result']:
            if counter < 31:
                _a, _b = 138, 149
            elif counter < 61:
                if counter == 31:
                    ans_cor = 65
                _a, _b = 159, 170
            else:
                if counter == 61:
                    ans_cor = 65
                _a, _b = 180, 191
            if item[1] == 1:
                pdf.text(_a, ans_cor, txt=f"{counter}.  {item[0]}")
                pdf.image('/home/nazarbek/CamTest-admin/media/files/correct.png', x=_b, y=ans_cor - 3, w=3, h=3)
            else:
                answ = item[0]
                pdf.text(_a, ans_cor, txt=f"{counter}.  {answ}")
                pdf.image('/home/nazarbek/CamTest-admin/media/files/wrong.png', x=_b, y=ans_cor - 3, w=3, h=3)
            ans_cor += 5
            counter += 1
        d = datetime.now().day
        h = datetime.now().hour
        m = datetime.now().minute
        s = datetime.now().second
        date = f"{d}{h}{m}{s}"
        file_name = f"{blok_1}-{blok_2}{date}.pdf"
        temp_pdf_path = os.path.join("/tmp", file_name)
        final_pdf_path = os.path.join("/home/nazarbek/CamTest-admin/media/check_file/outputfile/", file_name)

        try:
            pdf.output(temp_pdf_path)

            # Check if final directory exists, if not create it
            if not os.path.exists(os.path.dirname(final_pdf_path)):
                os.makedirs(os.path.dirname(final_pdf_path))
                print(f"Created directory: {os.path.dirname(final_pdf_path)}")

            shutil.move(temp_pdf_path, final_pdf_path)
            print(f"PDF moved to final directory: {final_pdf_path}")

            # Verify that the file has been moved successfully
            if os.path.exists(final_pdf_path):
                print(f"PDF successfully moved to {final_pdf_path}")
            else:
                print(f"Failed to move PDF to {final_pdf_path}")

            return file_name
        except Exception as e:
            print(f"Error creating or moving PDF: {e}")
            return None

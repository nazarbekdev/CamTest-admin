from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# from api.models import GenerateTest
# # Ma'lumotlarni olish
# # Masalan, question, image, va answer o'zgaruvchilari ma'lum
question = "Elektron pochta qachon yaratildi? // 1969-yili     // 1972-yil    //1970-yil    // 1971-yil "
image = "/home/nazarbek/CamTest-admin/media/database_images/desktop_mage.jpeg"  # Rasm fayl manzili
answer = "// 1969-yili "

# PDF faylini yaratish
pdf_file = "/home/nazarbek/CamTest-admin/tarix_test.pdf"  # PDF fayl manzili
c = canvas.Canvas(pdf_file, pagesize=letter)

# Ma'lumotlarni PDF fayliga qo'shish
c.drawString(10, 750, "Question: " + question, wordSpace=0.5)
c.drawString(10, 720, "Answer: " + answer)
c.drawImage(image, 10, 650, width=70, height=50)  # Rasmni joylashtirish
c.save()

# Rasmlar bilan birgalikda ma'lumotlar bazasidan savolni olish
# question_data = GenerateTest.objects.filter(question="Elektron pochta qachon yaratildi?// 1969-yili // 1970-yil// 1971-yil // 1972-yil").first()
#
# if question_data:
#     image = question_data.image.path  # Rasm manzili
# else:
#     # Savol topilmadi
#     print("Savol topilmadi!")
#
# # PDF faylini yaratish
# pdf_file = "/home/nazarbek/CamTest-admin/tarix_test.pdf"  # PDF fayl manzili
# c = canvas.Canvas(pdf_file, pagesize=letter)
#
# # Ma'lumotlarni PDF fayliga qo'shish
# c.drawString(100, 750, "Question: " + question)
# c.drawString(100, 700, "Answer: " + '')
# c.drawImage(image, 100, 650, width=200, height=200)  # Rasmni joylashtirish
# c.save()

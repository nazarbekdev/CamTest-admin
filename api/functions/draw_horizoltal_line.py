import fitz


def draw_horizontal_line(pdf_path, output_path):
    # PDF faylni ochish
    pdf_doc = fitz.open(pdf_path)

    # Har bir sahifada chiziq chizish
    for page_number in range(pdf_doc.page_count):
        # Sahifani olish
        page = pdf_doc.load_page(page_number)

        # Sahifa o'lchamini olish
        width = page.rect.width
        height = page.rect.height

        # Chiziqni chizish uchun qalamni yaratish
        line_color = (0, 0, 0)  # RGB rang (qora)
        line_width = 1  # Chiziq eni
        horiz_line_start = (15, height / 2 - 370)  # Chiziqning boshlanish nuqtasi
        horiz_line_end = (width - 15, height / 2 - 370)  # Chiziqning tugash nuqtasi

        # Sahifaga chiziq chizish
        page.draw_line(horiz_line_start, horiz_line_end, color=line_color, width=line_width)

        x = 250
        y = 13
        x1 = 545
        y1 = 16
        # Sahifa yuqori qism uchun yozuv
        rect = fitz.Rect(x, y, x + 500, y + 50)
        page.insert_textbox(rect, "TALABALIK SARI OLG'A", fontsize=10, fill=(0, 0, 0))

        rect = fitz.Rect(x1, y1, x1 + 500, y1 + 50)
        page.insert_textbox(rect, "CamTest", fontsize=8, fill=(0, 0, 0))

    # Yangi PDF faylni saqlash
    pdf_doc.save(output_path)

    # PDF faylni yopish
    pdf_doc.close()


draw_horizontal_line('/home/nazarbek/CamTest-admin/tests_fzthobny.pdf', 'result.pdf')

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(file_name, data):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Kolonkalar orasidagi masofa
    column_gap = 50
    margin = 50
    line_height = 15
    max_lines_per_page = int((height - 2 * margin) / line_height)

    left_column_x = margin
    right_column_x = width / 2 + column_gap

    current_page = 1
    current_line = 0

    def draw_page_header(page_num):
        c.drawString(margin, height - margin, f"Sahifa {page_num}")

    def draw_text_in_column(text, x, y):
        c.drawString(x, y, text)

    draw_page_header(current_page)

    for i, line in enumerate(data):
        if current_line < max_lines_per_page:
            y = height - margin - line_height * current_line
            if i % 2 == 0:
                draw_text_in_column(line, left_column_x, y)
            else:
                draw_text_in_column(line, right_column_x, y)
            current_line += 1
        else:
            c.showPage()
            current_page += 1
            draw_page_header(current_page)
            current_line = 0
            y = height - margin - line_height * current_line
            if i % 2 == 0:
                draw_text_in_column(line, left_column_x, y)
            else:
                draw_text_in_column(line, right_column_x, y)
            current_line += 1

    c.save()


# Ma'lumotlar ro'yxati
data = [
    "Bu birinchi qator", "Bu ikkinchi qator", "Bu uchinchi qator",
    "Bu to'rtinchi qator", "Bu beshinchi qator", "Bu oltinchi qator",
    "Bu yettinchi qator", "Bu sakkizinchi qator", "Bu to'qqizinchi qator",
    "Bu o'ninchi qator", "Bu o'n birinchi qator", "Bu o'n ikkinchi qator",
    "Bu o'n uchinchi qator", "Bu o'n to'rtinchi qator", "Bu o'n beshinchi qator",
    "Bu o'n oltinchi qator", "Bu o'n yettinchi qator", "Bu o'n sakkizinchi qator",
    "Bu o'n to'qqizinchi qator", "Bu yigirmanchi qator", "Bu yigirma birinchi qator",
    "Bu yigirma ikkinchi qator", "Bu yigirma uchinchi qator", "Bu yigirma to'rtinchi qator",
    "Bu yigirma beshinchi qator", "Bu yigirma oltinchi qator", "Bu yigirma yettinchi qator",
    "Bu yigirma sakkizinchi qator", "Bu yigirma to'qqizinchi qator", "Bu o'ttizinchi qator",
    "Bu birinchi qator", "Bu ikkinchi qator", "Bu uchinchi qator",
    "Bu to'rtinchi qator", "Bu beshinchi qator", "Bu oltinchi qator",
    "Bu yettinchi qator", "Bu sakkizinchi qator", "Bu to'qqizinchi qator",
    "Bu o'ninchi qator", "Bu o'n birinchi qator", "Bu o'n ikkinchi qator",
    "Bu o'n uchinchi qator", "Bu o'n to'rtinchi qator", "Bu o'n beshinchi qator",
    "Bu o'n oltinchi qator", "Bu o'n yettinchi qator", "Bu o'n sakkizinchi qator",
    "Bu o'n to'qqizinchi qator", "Bu yigirmanchi qator", "Bu yigirma birinchi qator",
    "Bu yigirma ikkinchi qator", "Bu yigirma uchinchi qator", "Bu yigirma to'rtinchi qator",
    "Bu yigirma beshinchi qator", "Bu yigirma oltinchi qator", "Bu yigirma yettinchi qator",
    "Bu yigirma sakkizinchi qator", "Bu yigirma to'qqizinchi qator", "Bu o'ttizinchi qator"
]

# PDF fayl yaratish
create_pdf("example_two_columns_continued.pdf", data)

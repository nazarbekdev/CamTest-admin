import docx2txt


def image_filter(input_loc, output_loc):
    input_loc = input_loc
    output_loc = output_loc
    inp = f'"{input_loc}"'
    outp = f'"{output_loc}"'

    print(inp)

    input_parts = inp.split('"')
    output_parts = outp.split('"')

    if len(input_parts) < 2 or len(output_parts) < 2:
        print("Fayl manzilida xatolik mavjud.")
    else:
        text = docx2txt.process(input_parts[1], output_parts[1])
        print("Textdan rasm muvaffaqiyatli o'qib olindi!")

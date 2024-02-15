import os
import docx2txt


def edit_test(file):
    text = docx2txt.process(file)
    text = text[1:]
    test_lst = []
    for question in text.split('#'):
        test_lst.append(question)

    images_in_test = []
    no_images_in_test = []
    for i in test_lst:
        if '@image' in i.split('//')[0]:
            images_in_test.append(i)
        else:
            no_images_in_test.append(i)
    a = images_in_test + no_images_in_test
    return a


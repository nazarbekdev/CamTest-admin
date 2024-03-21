import tkinter as tk
from tkinter import filedialog


def yuklash():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Fayl o'qildi:")
            print(content)


def til_tanlash(til):
    print("Tanlangan til:", til)


root = tk.Tk()
root.title("Test Yuklash")
root.attributes("-fullscreen", True)

button_test_yuklash = tk.Label(root, text='Test Yuklash:', font=("Arial", 16))
button_test_yuklash.pack(padx=10)

button_fayl = tk.Button(root, text="Fayl tanlash", command=yuklash, relief=tk.RAISED)
button_fayl.pack(padx=10)


label_til = tk.Label(root, text="Tilni tanlang:")
label_til.pack(pady=10)

button_uz = tk.Button(root, text="Uzbek", command=lambda: til_tanlash("uz"), width=6, height=1)
button_uz.pack()

button_ru = tk.Button(root, text="Russian", command=lambda: til_tanlash("ru"), width=6, height=1)
button_ru.pack()

button_ar = tk.Button(root, text="Arabic", command=lambda: til_tanlash("ar"), width=6, height=1)
button_ar.pack()

root.mainloop()


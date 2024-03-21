import tkinter as tk


def check_code_and_open_second_page():
    entered_code = code_entry.get()
    if entered_code == '4444':  # Replace "your_admin_code_here" with the actual admin code
        print("Access granted")  # Replace this with the action you want to take if the code is correct
        open_second_page()  # Call the function to open the second page
        root.destroy()  # Close the first page
    else:
        print("Access denied")  # Replace this with the action you want to take if the code is incorrect


def open_second_page():
    # Create the main window for the second page
    second_page = tk.Tk()
    second_page.attributes("-fullscreen", True)
    second_page.title("Second Page")

    # Foydalanuvchilar haqida ma'lumot tugmasini qo'shish
    user_info_button = tk.Button(second_page, text="Foydalanuvchilar haqida ma'lumot", command=show_user_info, width=30, height=5, bg='gray', activebackground='white')
    user_info_button.pack(pady=10)
    user_info_button.place(relx=0.2, rely=0.3)

    # TEST KIRITISH tugmasini qo'shish
    test_button = tk.Button(second_page, text="TEST KIRITISH", command=start_test, width=30, height=5, bg='gray', activebackground='white')
    test_button.pack(pady=10)
    test_button.place(relx=0.5, rely=0.1, anchor='center')

    # Dasturiy ta'minot tugmasini qo'shish
    software_button = tk.Button(second_page, text="Dasturiy ta'minot", command=open_software, width=30, height=5, bg='gray', activebackground='white')
    software_button.pack(pady=10)
    software_button.place(relx=0.7, rely=0.3)


def show_user_info():
    print("Foydalanuvchilar haqida ma'lumot")


def start_test():
    print("TEST KIRITISH")


def open_software():
    print("Dasturiy ta'minot")


# Create the main window for the first page
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Administrator Login")

# Create a label for instructions
label = tk.Label(root, text="Please enter the access code:")
label.pack(pady=10)
label.place(relx=0.5, rely=0.4, anchor="center")

# Create an entry for the access code
code_entry = tk.Entry(root, show="*")  # Use show="*" to hide the entered characters
code_entry.pack(pady=5)
code_entry.place(relx=0.5, rely=0.5, anchor="center")

# Create a button to check the code and open the second page
check_button = tk.Button(root, text="Check Code", command=check_code_and_open_second_page)
check_button.pack(pady=5)
check_button.place(relx=0.5, rely=0.6, anchor="center")

# Display the first window
root.mainloop()

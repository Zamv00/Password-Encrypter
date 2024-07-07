from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.messagebox import *
import time
import string

def has_special_characters(s):
    allowed_characters = string.ascii_letters + string.digits + " "
    for c in s:
        if c not in allowed_characters:
            return True
    return False

def new_window():
    global caller_id
    if caller_id == "encrypt":
        messagebox.showinfo("Successful", "Password encrypted successfully. Click OK to continue")
    elif caller_id == "decrypt":
        messagebox.showinfo("Successful", "Password decrypted successfully. Click OK to continue")
    elif caller_id == "error":
        messagebox.showerror("Error", "You must insert something first. Click OK to continue")
    elif caller_id == "specials":
        messagebox.showerror("Error", "Special characters are not allowed. Click OK to continue")
        textbox.delete("1.0", END)

def encrypt():
    global caller_id
    caller_id = "encrypt"
    new_password = ""
    u_char = None
    normal_password = (textbox.get("1.0", END)).strip()
    try:
        if len(normal_password) == 0:
            caller_id = "error"
            new_window()
            root.update()
        elif has_special_characters(normal_password):
            print("special characters")
            caller_id = "specials"
            new_window()
            root.update()
        else:
            for char in normal_password:
                if char.isalpha():
                    if char.islower():
                        u_char = char.upper()
                    elif char.isupper():
                        u_char = char
                    for i in alfabeto:
                        if u_char == i:
                            index = alfabeto.index(i)
                            if char.isupper():
                                char = alfabeto_1[index]
                            elif char.islower():
                                char = alfabeto_1[index].lower()
                            new_password += char
                            break
                elif char.isnumeric():
                    for n in numbers:
                        if char == str(n):
                            index = numbers.index(n)
                            char = numbers_1[index]
                            new_password += str(char)
                            break
            print(new_password)
            label.config(text="Password encrypted!")
            textbox.delete("1.0", END)
            textbox.insert("1.0", new_password)
            new_window()
            root.update()
            label.config(text="Insert a password")
    except Exception:
        print("An error has occured in encrypting the file")

def decrypt():
    global caller_id
    caller_id = "decrypt"
    normal_password = ""
    u_char = None
    new_password = (textbox.get("1.0", END)).strip()
    if len(new_password) == 0:
        caller_id = "error"
        new_window()
        root.update()
    elif has_special_characters(new_password):
        print("special characters")
        caller_id = "specials"
        new_window()
        root.update()
    else:
        for char in new_password:
            if char.isalpha():
                if char.islower():
                    u_char = char.upper()
                elif char.isupper():
                    u_char = char
                for i in alfabeto:
                    if u_char == i:
                        index = alfabeto_1.index(i)
                        if char.isupper():
                            char = alfabeto[index]
                        elif char.islower():
                            char = alfabeto[index].lower()
                        normal_password += char
                        break
            elif char.isnumeric():
                for n in numbers:
                    if char == str(n):
                        index = numbers_1.index(n)
                        char = numbers[index]
                        normal_password += str(char)
                        break
        print(normal_password)
        label.config(text="Password decrypted!")
        textbox.delete("1.0", END)
        textbox.insert("1.0", normal_password)
        new_window()
        root.update()
        label.config(text="Insert a password")


def save_file():
    file = filedialog.asksaveasfile(initialfile="Untitled",
                                    initialdir="C:\\Users\\sansf\\Documents",
                                    defaultextension=".txt",
                                    filetypes=[("Text Documents", "*.txt")])
    if file is None:
         return
    else:
        try:
            file.write(textbox.get(1.0,END))
        except Exception as e:
            print("An error has occured in saving the file!", e)
        finally:
            file.close()


def open_file():
    file_path = askopenfilename(defaultextension=".txt",
                           filetypes=[("Text Documents", "*.txt")])
    if not file_path:
        return
    else:
        try:
            textbox.delete("1.0", END)
            with open(file_path, "r") as file:
                textbox.insert(1.0, file.read())
        except Exception as e:
            print("An error has occured in reading the file", e)


def about():
    showinfo("About this program", "Written by Zamv\n 2024")


alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","R","O","P","Q","R","S","T","W","X","Y","Z"]
alfabeto_1 = ["B","C","D","E","F","G","H","I","J","K","L","M","N","R","O","P","Q","R","S","T","W","X","Y","Z","A"]

numbers = [0,1,2,3,4,5,6,7,8,9]
numbers_1 = [1,2,3,4,5,6,7,8,9,0]

root = Tk()
root.title("Password Encrypter")
root.geometry("300x150")
root.resizable(False, False)
# icon = PhotoImage(file="img.ico")

menubar = Menu()
root.config(menu=menubar)
# root.iconphoto(False, icon)

file_menu = Menu(menubar, tearoff=FALSE)
about_menu = Menu(menubar, tearoff=FALSE)

menubar.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="Save", command=save_file, font=("Consolas", 12))
file_menu.add_command(label="Open", command=open_file, font=("Consolas", 12))

menubar.add_cascade(menu=about_menu, label="About")
about_menu.add_command(label="About", command=about, font=("Consolas", 12))


label = Label(root, text="Insert a password", font=("Consolas", 15, "bold"), padx=5, pady=5)
label.pack()

textbox = Text(root, width=20, height=2,bd=5, font=("Constantia", 12),padx=5)
textbox.pack()

button_frame=Frame(root, pady=5)
button_frame.pack()

encrypt_button = Button(button_frame, text = "Encrypt",font=("Consolas",11,"bold"),padx=10,bg="black",fg="green",
       activebackground="black",activeforeground="green", command=encrypt)
encrypt_button.pack(side=LEFT,padx=(0,10))

decrypt_button = Button(button_frame, text = "Decrypt",font=("Consolas",11,"bold"),padx = 10,bg="black",fg="green",
       activebackground="black",activeforeground="green", command=decrypt)
decrypt_button.pack(side=LEFT)


root.mainloop()



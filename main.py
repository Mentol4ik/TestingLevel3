from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()
root.title("Бесследный унитожитель файлов")
root.geometry("2560x1600")

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)

text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)



def deleting():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        if os.path.exists(file_path):
            os.remove(file_path)
            print("Файл успешно удален")
        else:
            print("Файл не найден")
        if os.path.exists(file_path):
            os.rmdir(file_path)
            print("Папка успешно удалена")
        else:
            print("Папка не найдена")


def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


open_button = ttk.Button(text="Удалить", command=deleting)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)

save_button = ttk.Button(text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)

root.mainloop()
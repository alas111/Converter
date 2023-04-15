import os
import tkinter as tk
from tkinter import colorchooser
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import main as converter

color_var = (255, 255, 255)
file_path = ''


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file:
        global file_path
        file_path = os.path.abspath(file.name)
        ent_1.delete(0, END)
        ent_1.insert(0, file_path)


def run():
    global file_path
    if file_path == '':
        directory_path = ent_1.get()
        if directory_path == '':
            tk.messagebox.showwarning("Внимание!", "Пожалуйста, выберите файл.")
    else:
        directory_path = file_path

    nums_0, nums_1, nums_3, nums_4 = converter.main(directory_path, color_var)
    zero_circle_label.config(text=str(nums_1))
    zero_lines_label.config(text=str(nums_3))
    zero_distance_label.config(text=str(nums_4))
    zero_all_elements_label.config(text=str(nums_0))


def color():
    my_color = colorchooser.askcolor()[0]
    color_str = from_rgb(my_color)
    color_canvas.delete(tk.ALL)
    color_canvas.create_rectangle(0, 0, 80, 80, fill=color_str)
    global color_var
    color_var = my_color


def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def info():
    tk.messagebox.showinfo("About converter", "CONVERTER\nVersion: 1.0.0\nDeveloper: Letnikov D.O."
                                              "\nPowered by open-source software\nAll rights reserved")


# Main window properties
root = Tk()
root.geometry("405x180")
root.resizable(False, False)
root.title("Converter 1.0.0")
root.iconbitmap('E:/Python_Projects/PyCharm_Projects/Text_Work/Converter/images/icon.ico')

# Color preview box
color_canvas = tk.Canvas(root, height=80, width=80, bg='white')
color_canvas.place(x=220, y=69)
color_canvas.create_rectangle(0, 0, 80, 80, fill='white')

# Buttons
Button(root, text="Открыть", height=1, width=10, command=open_file).place(x=315, y=7)
Button(root, text="Цвет", height=1, width=10, command=color).place(x=220, y=38)
play = PhotoImage(file=r"E:/Python_Projects/PyCharm_Projects/Text_Work/Converter/images/play.png")
Button(root, text='Запуск', height=105, width=74, bg='white', image=play, command=run).place(x=315, y=38)

# Entries
ent_1 = Entry(root, width=48, justify='left')
ent_1.place(x=10, y=10)

# Total elements line
border_canvas = tk.Canvas(root, height=10, width=200)
border_canvas.place(x=10, y=100)
border_canvas.create_line(0, 5, 200, 5)

# Labels
circle_label = tk.Label(text="Колличество окружностей: ")
circle_label.place(x=10, y=40)
lines_label = tk.Label(text="Колличество линий: ")
lines_label.place(x=10, y=60)
distance_label = tk.Label(text="Колличество дистанций: ")
distance_label.place(x=10, y=80)
all_elements_label = tk.Label(text="Колличество всех элементов: ")
all_elements_label.place(x=10, y=110)

# First values of labels
zero_circle_label = tk.Label(text="0")
zero_circle_label.place(x=180, y=40)
zero_lines_label = tk.Label(text="0")
zero_lines_label.place(x=180, y=60)
zero_distance_label = tk.Label(text="0")
zero_distance_label.place(x=180, y=80)
zero_all_elements_label = tk.Label(text="0")
zero_all_elements_label.place(x=180, y=110)

# Menu bar
menu_bar = Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Выход", command=root.destroy)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="О програме", command=info)

menu_bar.add_cascade(label="Файл", menu=file_menu)
menu_bar.add_cascade(label="Помощь", menu=help_menu)

root.config(menu=menu_bar)

# Infinite loop
root.mainloop()

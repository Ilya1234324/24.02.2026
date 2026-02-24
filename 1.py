import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os 
import random 

def open_registration():
    registration = tk.Toplevel(root)
    registration.title('Регистрация')
    registration.geometry('700x400')
    registration.configure(bg='#c3c3c3')
    root.withdraw()

    frame_registration1 = tk.Frame(registration, bg="#51fc5d", width=700, height=90)
    frame_registration1.place(x=0, y=0)

    frame_registration2 = tk.Frame(registration, bg="#b8b8b8", width=225, height=20)
    frame_registration2.place(x=5, y=95)

    frame_registration3 = tk.Frame(registration, bg="#b8b8b8", width=225, height=20)
    frame_registration3.place(x=238, y=95)

    frame_registration4 = tk.Frame(registration, bg="#b8b8b8", width=225, height=20)
    frame_registration4.place(x=470, y=95)

    frame_registration5 = tk.Frame(registration, bg="#b8b8b8", width=225, height=270)
    frame_registration5.place(x=5, y=120)

    frame_registration6 = tk.Frame(registration, bg="#b8b8b8", width=225, height=270)
    frame_registration6.place(x=238, y=120)

    frame_registration7 = tk.Frame(registration, bg="#b8b8b8", width=225, height=270)
    frame_registration7.place(x=470, y=120)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure('Rounded.TButton',
                background='#333333',
                foreground='white',
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                relief='flat',
                font=('Arial', 12))
    style.map('Rounded.TButton',
          background=[('active', '#555555'), ('pressed', '#222222')],
          foreground=[('active', 'white')])

    label_registration1 = tk.Label(registration, text='НЕЙРОДОБР', bg='#51fc5d', fg='white', font=("Arial", 25))
    label_registration1.place(x=240,y=10)

    label_registration2 = tk.Label(registration, text='Программа для мониторинга состояния водителей', bg='#51fc5d', fg='white', font=("Arial", 10))
    label_registration2.place(x=195,y=55)

    label_registration3 = tk.Label(registration, text='Регистрация оператора', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration3.place(x=50,y=95)

    label_registration4 = tk.Label(registration, text='Индефикация', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration4.place(x=315,y=95)

    label_registration5 = tk.Label(registration, text='Информационный блок', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration5.place(x=525,y=95)

    label_registration6 = tk.Label(registration, text='Фамилия', bg='#b8b8b8', fg='black', font=("Arial", 12))
    label_registration6.place(x=30,y=145)

    label_registration7 = tk.Label(registration, text='Имя', bg='#b8b8b8', fg='black', font=("Arial", 12))
    label_registration7.place(x=60,y=195)

    label_registration8 = tk.Label(registration, text='Отчество', bg='#b8b8b8', fg='black', font=("Arial", 12))
    label_registration8.place(x=25,y=245)

    label_registration9 = tk.Label(registration, text='Возраст', bg='#b8b8b8', fg='black', font=("Arial", 12))
    label_registration9.place(x=32,y=295)

    label_registration10 = tk.Label(registration, text='Оператор не определен', bg='#b8b8b8', fg='black', font=("Arial", 12))
    label_registration10.place(x=480,y=145)

    label_registration11 = tk.Label(registration, text='id не присвоен', bg="#ff0000", fg='black', font=("Arial", 22))
    label_registration11.place(x=480,y=215)

    label_registration12 = tk.Label(registration, text='Запуск программы невозможен', bg='#b8b8b8', fg='black', font=("Arial", 10))
    label_registration12.place(x=480,y=305)

    entry_registration1 = tk.Entry(registration, width=15)
    entry_registration1.place(x=115, y=150)

    entry_registration2 = tk.Entry(registration, width=15)
    entry_registration2.place(x=115, y=200)

    entry_registration3 = tk.Entry(registration, width=15)
    entry_registration3.place(x=115, y=250)

    entry_registration4 = tk.Entry(registration, width=15)
    entry_registration4.place(x=115, y=300)

    def check_entry1():
        if entry_registration1.get().strip():  
            label_registration10.config(text="Оператор определен")

            random_id = random.randint(100000, 999999)     
            
            label_registration11.config(text=f"ID: {random_id}", bg="#00ff00")
            
            
            label_registration12.config(text="Оператор зарегистрирован")
        else:
            label_registration10.config(text="Оператор не определен")
            label_registration11.config(text="id не присвоен", bg="#ff0000")
            label_registration12.config(text="Запуск программы невозможен")

    button_registration1 = ttk.Button(registration, text='Записать', style='Rounded.TButton', command=check_entry1)
    button_registration1.place(x=115, y=350, width=100, height=30)

    button_registration2 = ttk.Button(registration, text='Далее', style='Rounded.TButton', command=open_okno)
    button_registration2.place(x=575, y=350, width=100, height=30)

    photo_path = "фото/young-businessman-classic-blue-suit-tie_305638-9.avif"

    if os.path.exists(photo_path):
        try:
            image = Image.open(photo_path)
            image = image.resize((200, 240), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(registration, image=photo, bg='#b8b8b8')
            image_label.place(x=250, y=130) 
            image_label.image = photo
            
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            placeholder = tk.Label(registration, text="🖼️\nФото\nнедоступно", 
                                 bg='#b8b8b8', fg='gray', font=("Arial", 16))
            placeholder.place(x=70, y=80)
    else:
        print(f"Файл не найден: {photo_path}")
        placeholder = tk.Label(registration, text="🖼️\nНет фото", 
                             bg='#b8b8b8', fg='gray', font=("Arial", 16))
        placeholder.place(x=70, y=80)


def open_okno():
    zarega = tk.Toplevel(root)
    zarega.title('Авторизация')
    zarega.geometry('700x400')
    zarega.configure(bg='#c3c3c3')
    open_registration.withdraw()







def open_authorizatio():
    authorization = tk.Toplevel(root)
    authorization.title('Авторизация')
    authorization.geometry('700x400')
    authorization.configure(bg='#c3c3c3')
    root.withdraw()




root = tk.Tk()
root.title('Выбор действия')
root.geometry('300x165')
root.configure(bg="#c3c3c3")

button_registration = tk.Button(root, text='Регистрация', width=10, height=2, bg='green', command=open_registration)
button_registration.place(x=40, y=100)

button_authorization = tk.Button(root, text='Авторизация', width=10, height=2, bg='green')
button_authorization.place(x=190, y=100)

label = tk.Label(root, text='Выберите действие:', bg='#c3c3c3')
label.place(x=90, y=30)

root.mainloop()
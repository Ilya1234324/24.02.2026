import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os 
import random 
import json
import hashlib

CREDENTIALS_FILE = "user_credentials.json"

def hash_password(password):
    """Хеширование пароля для безопасного хранения"""
    return hashlib.sha256(password.encode()).hexdigest()

def save_credentials(username, password):
    """Сохранение учетных данных в файл"""
    hashed_password = hash_password(password)
    credentials = {"username": username, "password": hashed_password}
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(credentials, f)
    print(f"Сохранены учетные данные для пользователя: {username}")  

def load_credentials():
    """Загрузка учетных данных из файла"""
    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = json.load(f)
            print(f"Загружены учетные данные: {credentials['username']}")  
            return credentials
    except FileNotFoundError:
        print("Файл с учетными данными не найден")
        return None

def open_main_window():
    """Открывает главное окно с функционалом"""
    global root
    print("Открываем главное окно")  
    root.deiconify()  

def open_registration_window():
    """Окно регистрации нового пользователя"""
    print("Открываем окно регистрации")
    
    reg_win = tk.Toplevel(root)
    reg_win.title('Регистрация пользователя')
    reg_win.geometry('350x300')
    reg_win.configure(bg="#c3c3c3")
    reg_win.resizable(False, False)

    label_title = tk.Label(reg_win, text='НЕЙРОДОБР', bg='#51fc5d', fg='white', 
                          font=("Arial", 16), width=20)
    label_title.pack(pady=10)
    
    label_subtitle = tk.Label(reg_win, text='Регистрация нового пользователя', 
                             bg="#c3c3c3", font=("Arial", 10))
    label_subtitle.pack(pady=5)

    frame_input = tk.Frame(reg_win, bg="#c3c3c3")
    frame_input.pack(pady=20)

    tk.Label(frame_input, text="Придумайте логин:", bg="#c3c3c3", 
            font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky='w')
    entry_username = tk.Entry(frame_input, width=25, font=("Arial", 10))
    entry_username.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame_input, text="Придумайте пароль:", bg="#c3c3c3", 
            font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky='w')
    entry_password = tk.Entry(frame_input, width=25, font=("Arial", 10), show="*")
    entry_password.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(frame_input, text="Подтвердите пароль:", bg="#c3c3c3", 
            font=("Arial", 10)).grid(row=2, column=0, pady=5, sticky='w')
    entry_confirm = tk.Entry(frame_input, width=25, font=("Arial", 10), show="*")
    entry_confirm.grid(row=2, column=1, pady=5, padx=5)
    
    def register_user():
        """Регистрация нового пользователя"""
        username = entry_username.get().strip()
        password = entry_password.get()
        confirm = entry_confirm.get()

        if not username:
            messagebox.showwarning("Ошибка", "Введите логин!")
            return
        
        if not password:
            messagebox.showwarning("Ошибка", "Введите пароль!")
            return
        
        if password != confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
            return
        
        if len(password) < 4:
            messagebox.showwarning("Ошибка", "Пароль должен быть не менее 4 символов!")
            return

        save_credentials(username, password)
        
        messagebox.showinfo("Успех", "Регистрация прошла успешно!\nТеперь вы можете войти в систему.")
        reg_win.destroy()
        open_main_window()

    btn_register = tk.Button(reg_win, text='Зарегистрироваться', bg='green', fg='white',
                            font=("Arial", 10), width=20, command=register_user)
    btn_register.pack(pady=10)

    reg_win.protocol("WM_DELETE_WINDOW", lambda: close_application(reg_win))

def open_login_window():
    """Окно входа в систему"""
    print("Открываем окно входа")
    
    login_win = tk.Toplevel(root)
    login_win.title('Вход в систему')
    login_win.geometry('350x270')
    login_win.configure(bg="#c3c3c3")
    login_win.resizable(False, False)

    label_title = tk.Label(login_win, text='НЕЙРОДОБР', bg='#51fc5d', fg='white', 
                          font=("Arial", 16), width=20)
    label_title.pack(pady=10)
    
    label_subtitle = tk.Label(login_win, text='Вход в систему', 
                             bg="#c3c3c3", font=("Arial", 10))
    label_subtitle.pack(pady=5)

    frame_input = tk.Frame(login_win, bg="#c3c3c3")
    frame_input.pack(pady=20)

    tk.Label(frame_input, text="Логин:", bg="#c3c3c3", 
            font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky='w')
    entry_username = tk.Entry(frame_input, width=20, font=("Arial", 10))
    entry_username.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame_input, text="Пароль:", bg="#c3c3c3", 
            font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky='w')
    entry_password = tk.Entry(frame_input, width=20, font=("Arial", 10), show="*")
    entry_password.grid(row=1, column=1, pady=5, padx=5)
    
    def check_credentials():
        """Проверка введенных учетных данных"""
        username = entry_username.get().strip()
        password = entry_password.get()
        
        if not username or not password:
            messagebox.showwarning("Ошибка", "Введите логин и пароль!")
            return

        saved_credentials = load_credentials()
        
        if saved_credentials:
            saved_username = saved_credentials["username"]
            saved_password_hash = saved_credentials["password"]

            if username == saved_username and hash_password(password) == saved_password_hash:
                messagebox.showinfo("Успех", f"Добро пожаловать, {username}!")
                login_win.destroy()
                open_main_window()
            else:
                messagebox.showerror("Ошибка", "Неверный логин или пароль!")
                entry_password.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Пользователь не найден!\nПерезапустите программу для регистрации.")

    btn_login = tk.Button(login_win, text='Войти', bg='green', fg='white',
                         font=("Arial", 10), width=15, command=check_credentials)
    btn_login.pack(pady=10)

    btn_register = tk.Button(login_win, text='Нет аккаунта? Зарегистрироваться', 
                            bg='gray', fg='white', font=("Arial", 9),
                            command=lambda: [login_win.destroy(), open_registration_window()])
    btn_register.pack(pady=5)

    entry_password.bind('<Return>', lambda event: check_credentials())

    login_win.protocol("WM_DELETE_WINDOW", lambda: close_application(login_win))

def close_application(window):
    """Закрытие окна и завершение программы"""
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        window.destroy()
        root.destroy()

def open_registration():
    registration = tk.Toplevel(root)
    registration.title('Регистрация оператора')
    registration.geometry('700x400')
    registration.configure(bg="#e3e1e1")
    registration.resizable(False, False)
    root.withdraw()
    
    registration.protocol("WM_DELETE_WINDOW", lambda: close_window(registration))

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

    operator_id = None
    operator_status = "не определен"

    def validate_age(age_text):
        """Проверка корректности возраста"""
        if not age_text:
            return True, None 
        try:
            age = int(age_text)
            if age < 18 or age > 60:
                return False, "Возраст должен быть от 18 до 60 лет"
            return True, None
        except ValueError:
            return False, "Введите корректное число"

    def check_entry1():
        nonlocal operator_id, operator_status

        if not entry_registration1.get().strip():
            messagebox.showwarning("Внимание", "Введите фамилию")
            return
            
        if not entry_registration2.get().strip():
            messagebox.showwarning("Внимание", "Введите имя")
            return

        age_text = entry_registration4.get().strip()
        is_valid_age, age_error = validate_age(age_text)
        
        if age_text and not is_valid_age:
            messagebox.showwarning("Возрастное ограничение", age_error)
            return

        label_registration10.config(text="Оператор определен")
        random_id = random.randint(100000, 999999)     
        operator_id = random_id
        operator_status = "зарегистрирован"
        
        label_registration11.config(text=f"ID: {random_id}", bg="#00ff00")
        label_registration12.config(text="Оператор зарегистрирован")
        
        messagebox.showinfo("Успех", f"Оператор успешно зарегистрирован!\nID: {random_id}")

    button_registration1 = ttk.Button(registration, text='Записать', style='Rounded.TButton', command=check_entry1)
    button_registration1.place(x=115, y=350, width=100, height=30)

    button_registration2 = ttk.Button(registration, text='Далее', style='Rounded.TButton', command=lambda: open_okno(registration, 
        entry_registration1.get(),
        entry_registration2.get(),
        entry_registration3.get(),
        entry_registration4.get(),
        operator_id,
        operator_status))
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


def open_okno(prev_window, surname, name, patronymic, age, operator_id, operator_status):
    zarega = tk.Toplevel(root)
    zarega.title('Авторизация')
    zarega.geometry('700x400')
    zarega.configure(bg='#c3c3c3')
    zarega.resizable(False, False)
    prev_window.destroy()
    
    zarega.protocol("WM_DELETE_WINDOW", lambda: close_window(zarega))

    frame_registration1 = tk.Frame(zarega, bg="#51fc5d", width=700, height=90)
    frame_registration1.place(x=0, y=0)

    frame_registration2 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=20)
    frame_registration2.place(x=5, y=95)

    frame_registration3 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=20)
    frame_registration3.place(x=238, y=95)

    frame_registration4 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=20)
    frame_registration4.place(x=470, y=95)

    frame_registration5 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=270)
    frame_registration5.place(x=5, y=120)

    frame_registration6 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=270)
    frame_registration6.place(x=238, y=120)

    frame_registration7 = tk.Frame(zarega, bg="#b8b8b8", width=225, height=270)
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

    label_registration1 = tk.Label(zarega, text='НЕЙРОДОБР', bg='#51fc5d', fg='white', font=("Arial", 25))
    label_registration1.place(x=240,y=10)

    label_registration2 = tk.Label(zarega, text='Программа для мониторинга состояния водителей', bg='#51fc5d', fg='white', font=("Arial", 10))
    label_registration2.place(x=195,y=55)

    label_registration3 = tk.Label(zarega, text='Информация операторов', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration3.place(x=50,y=95)

    label_registration4 = tk.Label(zarega, text='Индефикация', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration4.place(x=315,y=95)

    label_registration5 = tk.Label(zarega, text='Информационный блок', bg='#b8b8b8', fg='black', font=("Arial", 8))
    label_registration5.place(x=525,y=95)

    label_surname_text = tk.Label(zarega, bg='#b8b8b8', fg='black', font=("Arial", 11, "bold"))
    label_surname_text.place(x=115, y=125)
    label_surname_value = tk.Label(zarega, text=surname if surname else 'не указана', bg='#b8b8b8', fg='black', font=("Arial", 11))
    label_surname_value.place(x=115, y=125)

    label_name_text = tk.Label(zarega, bg='#b8b8b8', fg='black', font=("Arial", 11, "bold"))
    label_name_text.place(x=115, y=155)
    label_name_value = tk.Label(zarega, text=name if name else 'не указано', bg='#b8b8b8', fg='black', font=("Arial", 11))
    label_name_value.place(x=115, y=155)

    label_patronymic_text = tk.Label(zarega, bg='#b8b8b8', fg='black', font=("Arial", 11, "bold"))
    label_patronymic_text.place(x=115, y=185)
    label_patronymic_value = tk.Label(zarega, text=patronymic if patronymic else 'не указано', bg='#b8b8b8', fg='black', font=("Arial", 11))
    label_patronymic_value.place(x=115, y=185)

    label_age_text = tk.Label(zarega, bg='#b8b8b8', fg='black', font=("Arial", 11, "bold"))
    label_age_text.place(x=115, y=215)
    label_age_value = tk.Label(zarega, text=age if age else 'не указан', bg='#b8b8b8', fg='black', font=("Arial", 11))
    label_age_value.place(x=115, y=215)

    if operator_id:
        label_registration10 = tk.Label(zarega, text='Оператор определен', bg='#b8b8b8', fg='black', font=("Arial", 12))
        label_registration11 = tk.Label(zarega, text=f"ID: {operator_id}", bg="#00ff00", fg='black', font=("Arial", 22))
        label_registration12 = tk.Label(zarega, text='Оператор зарегистрирован', bg='#b8b8b8', fg='black', font=("Arial", 10))
    else:
        label_registration10 = tk.Label(zarega, text='Оператор не определен', bg='#b8b8b8', fg='black', font=("Arial", 12))
        label_registration11 = tk.Label(zarega, text='id не присвоен', bg="#ff0000", fg='black', font=("Arial", 22))
        label_registration12 = tk.Label(zarega, text='Запуск программы невозможен', bg='#b8b8b8', fg='black', font=("Arial", 10))
    
    label_registration10.place(x=480,y=145)
    label_registration11.place(x=480,y=215)
    label_registration12.place(x=480,y=305)

    photo_path = "фото/young-businessman-classic-blue-suit-tie_305638-9.avif"

    if os.path.exists(photo_path):
        try:
            image = Image.open(photo_path)
            image = image.resize((200, 240), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(zarega, image=photo, bg='#b8b8b8')
            image_label.place(x=250, y=130) 
            image_label.image = photo
            
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            placeholder = tk.Label(zarega, text="🖼️\nФото\nнедоступно", 
                                 bg='#b8b8b8', fg='gray', font=("Arial", 16))
            placeholder.place(x=250, y=130)
    else:
        print(f"Файл не найден: {photo_path}")
        placeholder = tk.Label(zarega, text="🖼️\nНет фото", 
                             bg='#b8b8b8', fg='gray', font=("Arial", 16))
        placeholder.place(x=250, y=130)

    if os.path.exists(photo_path):
        try:
            image = Image.open(photo_path)
            image = image.resize((100, 120), Image.Resampling.LANCZOS)
            photo_small = ImageTk.PhotoImage(image)

            image_label_small = tk.Label(zarega, image=photo_small, bg='#b8b8b8')
            image_label_small.place(x=10, y=125) 
            image_label_small.image = photo_small
            
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            placeholder = tk.Label(zarega, text="🖼️\nФото\nнедоступно", 
                                 bg='#b8b8b8', fg='gray', font=("Arial", 16))
            placeholder.place(x=10, y=125)
    else:
        print(f"Файл не найден: {photo_path}")
        placeholder = tk.Label(zarega, text="🖼️\nНет фото", 
                             bg='#b8b8b8', fg='gray', font=("Arial", 16))
        placeholder.place(x=10, y=125)


def close_window(window):
    """Закрытие окна и возврат к главному"""
    root.deiconify()
    window.destroy()

root = tk.Tk()
root.title('НЕЙРОДОБР - Главное окно')
root.geometry('300x165')
root.configure(bg="#c3c3c3")
root.resizable(False, False)

root.withdraw()

button_registration = tk.Button(root, text='Регистрация оператора', width=20, height=2, 
                               bg='green', fg='white', font=("Arial", 10), command=open_registration)
button_registration.pack(expand=True)

if os.path.exists(CREDENTIALS_FILE):
    print("Файл с учетными данными существует - открываем окно входа")
    open_login_window()
else:
    print("Файл с учетными данными НЕ существует - открываем окно регистрации")
    open_registration_window()

root.mainloop()
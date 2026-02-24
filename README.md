# как я сделал свое приложение на tkinter
Библиотеки я использовал вот эти:
```bash
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os 
import random 
```
import os я использовал для проверки файла фотографии на всякий случай,
а рандом я использовал для выдачи людям рандомного айди,
библиотека pillow для фото.
# Основная и самая важная часть кода:
```bash
def open_registration():
    registration = tk.Toplevel(root)
    registration.title('Регистрация')
    registration.geometry('700x400')
    registration.configure(bg='#c3c3c3')
    root.withdraw()
```
создание окна регистрации
```bash
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
```
создание бекенда для entry полей и кнопок (остальное пока что не доделано)
# Запуск программы 
он осуществляется через команду в терминале: python имя_файла.py тоесть в моем случае это python 1.py
# Фотографии моего проекта


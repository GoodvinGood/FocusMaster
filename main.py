import tkinter as tk
from tkinter import messagebox
import time

# Функция для обновления времени на экране
def update_timer():
    global timer_running
    if timer_running:
        current_time = int(timer_label['text'])
        if current_time > 0:
            timer_label['text'] = str(current_time - 1)
            root.after(1000, update_timer)
        else:
            messagebox.showinfo("Время вышло!", "Время для перерыва или перехода к следующей задаче.")
            timer_running = False

# Функция для запуска таймера
def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        update_timer()

# Функция для сброса таймера
def reset_timer():
    global timer_running
    timer_running = False
    timer_label['text'] = '1500'

# Функция для установки пользовательского времени
def set_custom_time():
    global timer_running
    timer_running = False
    custom_time = time_entry.get()
    if custom_time.isdigit():
        timer_label['text'] = custom_time
    else:
        messagebox.showerror("Ошибка", "Введите правильное числовое значение.")

# Создание основного окна
root = tk.Tk()
root.title("Таймер для концентрации внимания")

# Переменная для отслеживания состояния таймера
timer_running = False

# Элементы интерфейса
timer_label = tk.Label(root, text="1500", font="Arial 40 bold", bg="black", fg="white")
timer_label.pack(pady=20)

start_button = tk.Button(root, text="Старт", font="Arial 20", command=start_timer)
start_button.pack(pady=10)

reset_button = tk.Button(root, text="Сброс", font="Arial 20", command=reset_timer)
reset_button.pack(pady=10)

time_entry = tk.Entry(root, font="Arial 20", justify='center')
time_entry.pack(pady=10)

set_time_button = tk.Button(root, text="Установить время", font="Arial 20", command=set_custom_time)
set_time_button.pack(pady=10)

# Запуск основного цикла окна
root.mainloop()

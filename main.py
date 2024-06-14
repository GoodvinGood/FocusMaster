import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
print("Проверка")
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
root.geometry("500x400")
root.resizable(False, False)

# Установка фона
background_image = tk.PhotoImage(file="background.png")  # Замените "background.png" на путь к вашему файлу изображения
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Создание стиля
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("TLabel", font=("Arial", 40, "bold"), background="black", foreground="white")

# Переменная для отслеживания состояния таймера
timer_running = False

# Элементы интерфейса
timer_label = ttk.Label(root, text="1500", anchor="center", style="TLabel")
timer_label.pack(pady=20)

button_frame = ttk.Frame(root, style="TFrame")
button_frame.pack(pady=10)

start_button = ttk.Button(button_frame, text="Старт", command=start_timer, style="TButton")
start_button.grid(row=0, column=0, padx=5)

reset_button = ttk.Button(button_frame, text="Сброс", command=reset_timer, style="TButton")
reset_button.grid(row=0, column=1, padx=5)

time_entry = ttk.Entry(root, font=("Arial", 20), justify='center', width=10)
time_entry.pack(pady=10)

set_time_button = ttk.Button(root, text="Установить время", command=set_custom_time, style="TButton")
set_time_button.pack(pady=10)

# Запуск основного цикла окна
root.mainloop()

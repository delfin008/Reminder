from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime

def set_reminder():
    time_reminder = sd.askstring(title="Укажите время напоминания", prompt="Введите время (чч:мм)")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            print(now_time)
            r_time = now_time.replace(hour=hour, minute=minute)
            print(r_time)
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
        except ValueError:
            mb.showerror(title="Ошибка", message=f"Неправильно указано время")



window = Tk()
window.title("Напоминалка")


window.geometry(f"400x200+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-100}")
#установка окна в центре экрана монитора


l = Label(window, text="--Нажмите на кнопку и установите напоминание на любое время--")
l.pack(pady=10)
btn = Button(window,text="Установить напоминание", command=set_reminder)
btn.pack(pady=10)

window.mainloop()

from tkinter import *
from tkinter import simpledialog as sd
import time
import datetime

def set_reminder():
    time_reminder = sd.askstring(title="Укажите время напоминания", prompt="Введите время (чч:мм)")
    if time_reminder:
        hour, minute = time_reminder.split(":")
        hour = int(hour)
        minute = int(minute)
        now_time = datetime.datetime.now()


window = Tk()
window.title("Напоминалка")


window.geometry(f"400x200+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-100}")
#установка окна в центре экрана монитора


l = Label(window, text="--Нажмите на кнопку и установите напоминание на любое время--")
l.pack(pady=10)
btn = Button(window,text="Установить напоминание", command=set_reminder)
btn.pack(pady=10)

window.mainloop()

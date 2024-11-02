from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import time
import datetime
import pygame



def set_reminder():
    global r_time
    time_reminder = sd.askstring(title="Укажите время напоминания", prompt="Введите время (чч:мм)")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            r_time = now_time.replace(hour=hour, minute=minute, second=0)
            r_time = r_time.timestamp()
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
            check_time()
        except ValueError:
            mb.showerror(title="Ошибка", message=f"Неправильно указано время")

def check_time():
    global r_time
    if r_time:
        now = time.time()
        if now >= r_time:
            play_music()
            r_time = None
        window.after(1000, check_time)


def play_music():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer_music.load("Krasivay.mp3")
    pygame.mixer_music.play()

def stop_music():
    global music
    if music:
        pygame.mixer_music.stop()
        music = False


music = False
r_time =1.0


window = Tk()
window.title("Напоминалка")
window.geometry(f"400x200+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-100}")
#установка окна в центре экрана монитора


lab = Label(window, text="--Нажмите на кнопку и установите напоминание на любое время--")
lab.pack(pady=10)
btn = Button(window,text="Установить напоминание", command=set_reminder)
btn.pack(pady=10)
btn_stop_music = Button(window,text="Остановить музыку", command=stop_music)
btn_stop_music.pack()


window.mainloop()

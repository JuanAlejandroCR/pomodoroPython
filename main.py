from tkinter import*
import os
import math
import time
from threading import Thread
from plyer import notification
# -----------------------CONSTANTS----------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# -----------------------NOTIFICATION----------------------- #
def notifyMe(title, message):
    app_icon_path = os.path.join(os.path.dirname(__file__), "images", "icon.ico")

    notification.notify(
        title = title,
        message = message,
        app_icon = app_icon_path,
        timeout = 10
    )
# -----------------------TIMER RESET----------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

# -----------------------TIMER MECHANISM----------------------- #
def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        notifyMe("Break Time", "Take a long break! You deserve it.")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        notifyMe("Break Time", "Take a short break! You deserve it.")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        notifyMe("Work Time", "Get back to work! You can do it.")
        
# -----------------------COUNTDOWN MECHANISM----------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count // 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# -----------------------UI SETUP----------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(260, 257, image=tomato_img)
timer_text = canvas.create_text(260, 320, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=start_timer )
start_button.grid(column=0, row=1)

reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=reset_timer)
reset_button.grid(column=2, row=1)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 75, "bold"))
check_marks.grid(column=1, row=2)

window.mainloop()
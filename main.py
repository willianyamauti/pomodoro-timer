from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_label.config(text='')
    global reps
    reps = 0
    start_button.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    start_button.config(state=DISABLED)

    WORK_POMODORO = WORK_MIN * 60
    SHORT_BREAK_POMODORO = SHORT_BREAK_MIN * 60
    LONG_BREAK_POMODORO = LONG_BREAK_MIN * 60

    # Long rest on 8th rep
    if reps % 8 == 0:
        count_down(LONG_BREAK_POMODORO)
        timer_label.config(text='Break', fg=RED)

    # Work on 1st / 3rd / 5th / 7th
    elif reps % 2 != 0:
        count_down(WORK_POMODORO)
        timer_label.config(text='Work', fg=GREEN)

    # Rest on 2nd/ 4th / 6th rep
    else:
        count_down(SHORT_BREAK_POMODORO)
        timer_label.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer

    # gets min and seconds from the count(seconds)
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # format the number to a more human readable time
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    # go to the next rep
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(101, 135, text='00:00', fill='white', font=(FONT_NAME, 29, 'bold'))
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)
check_label = Label(text='', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 29, 'bold'))
check_label.grid(column=1, row=4)

window.mainloop()

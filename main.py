from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel()
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_lb.config(text="Timer")
    check_lb.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_lb.config(text="Break", fg=GREEN)
        countdown(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_lb.config(text="Break", fg=GREEN)
        countdown(SHORT_BREAK_MIN)
    else:
        timer_lb.config(text="Work!", fg=RED)
        countdown(WORK_MIN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif reps < 8:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_lb.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tmt_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tmt_img)
timer_text = canvas.create_text(100,135, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1,row=1)

timer_lb = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_lb.grid(column=1, row=0)

start_btn = Button(text="Start", font=(FONT_NAME,16, "bold"), command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 16, "bold"))
reset_btn.grid(column=2, row=2)

check_lb = Label(text="", font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
check_lb.grid(column=1, row=3)


window.mainloop()
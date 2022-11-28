import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 1
    # will stop the timer
    window.after_cancel(timer)
    check_mark.config(text='')
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer ():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps  % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)

    else :
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


    if reps % 2 == 0:
        work_session = check_mark.cget('text')
        check_mark.config(text=work_session+'✔')

    reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    if count_min < 10:
        count_min= f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # a way to change the text inside a canvas
    if count > 0:
         timer = window.after(1000, count_down, count-1) # if we want to cancel it we have to give it a name
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


#Tomato
# highlightthickness => to remove the white edges around the canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105,112, image=tomato_img)
# we assign it to variable to keep updating the time for it
timer_text=canvas.create_text(105, 130, text="00:00", font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)









#timer_text label
title_label = Label(text="Timer", font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)


# checkmark label

check_mark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12,'bold'))
check_mark.grid(column=1, row=4)




# start button
start = Button(master=window, text='Start', font=(FONT_NAME, 10, 'bold'), fg='green', command=start_timer)
start.grid(column=0, row=2)


# reset button
reset = Button(master=window, text='Reset', font=(FONT_NAME, 10, 'bold'), fg='red', command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()
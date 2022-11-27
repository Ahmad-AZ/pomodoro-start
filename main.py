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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
#window.minsize(height=500, width=500)

# highlightthickness => to remove the white edges around the canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105,112, image=tomato_img)
canvas.create_text(105, 130,text="00:00" , font=(FONT_NAME, 20, 'bold'), fill='white')
canvas.pack()












window.mainloop()
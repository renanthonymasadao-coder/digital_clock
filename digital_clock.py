import tkinter as ui
import time

window = ui.Tk()
window.title("Digital Clock")
window.geometry("400x400")

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

time_label = canvas.create_text(
    200, 200,
    fill="white",
    font=("Arial", 30, "bold")
)

def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    canvas.itemconfig(time_label, text=current_time)
    window.after(1000, update_clock)

update_clock()
window.mainloop()
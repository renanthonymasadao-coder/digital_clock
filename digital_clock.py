import tkinter as ui
import time

window = ui.Tk()
window.geometry("400x400")

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    

update_clock()

window.mainloop()

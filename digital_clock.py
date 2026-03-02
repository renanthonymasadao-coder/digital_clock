import tkinter as ui
import time
import math

window = ui.Tk()
window.title("Analog Clock")
window.geometry("400x400")
window.resizable(False, False)

canvas = ui.Canvas(window, width=400, height=400, background="black")
canvas.pack()

center_x = 200
center_y = 200
radius = 180

canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   outline="white", width=4)

for i in range(12):
    angle = math.radians(i * 30)

    x_outer = center_x + (radius - 10) * math.sin(angle)
    y_outer = center_y - (radius - 10) * math.cos(angle)

    x_inner = center_x + (radius - 30) * math.sin(angle)
    y_inner = center_y - (radius - 30) * math.cos(angle)

    canvas.create_line(x_inner, y_inner, x_outer, y_outer,
                       fill="white", width=3)

    number_x = center_x + (radius - 50) * math.sin(angle)
    number_y = center_y - (radius - 50) * math.cos(angle)

    canvas.create_text(number_x, number_y,
                       text=str(i if i != 0 else 12),
                       fill="white", font=("Arial", 14, "bold"))

seconds_hand_len = 140
minutes_hand_len = 110
hours_hand_len = 80

seconds_hand = canvas.create_line(center_x, center_y,
                                  center_x, center_y - seconds_hand_len,
                                  fill="red", width=1.5)

minutes_hand = canvas.create_line(center_x, center_y,
                                  center_x, center_y - minutes_hand_len,
                                  fill="white", width=3)

hours_hand = canvas.create_line(center_x, center_y,
                                center_x, center_y - hours_hand_len,
                                fill="white", width=5)

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    sec_angle = math.radians(seconds * 6)
    sec_x = center_x + seconds_hand_len * math.sin(sec_angle)
    sec_y = center_y - seconds_hand_len * math.cos(sec_angle)
    canvas.coords(seconds_hand, center_x, center_y, sec_x, sec_y)

    min_angle = math.radians(minutes * 6 + seconds * 0.1)
    min_x = center_x + minutes_hand_len * math.sin(min_angle)
    min_y = center_y - minutes_hand_len * math.cos(min_angle)
    canvas.coords(minutes_hand, center_x, center_y, min_x, min_y)

    hour_angle = math.radians(hours * 30 + minutes * 0.5)
    hour_x = center_x + hours_hand_len * math.sin(hour_angle)
    hour_y = center_y - hours_hand_len * math.cos(hour_angle)
    canvas.coords(hours_hand, center_x, center_y, hour_x, hour_y)

    window.after(1000, update_clock)

update_clock()
window.mainloop()
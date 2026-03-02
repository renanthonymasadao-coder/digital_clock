import tkinter as ui

window = ui.Tk()
window.title("Analog Clock")
window.geometry("400x400")
window.resizable(False, False)

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

center_x = 200
center_y = 200
radius = 180

canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   outline="white", width=4)

window.mainloop()
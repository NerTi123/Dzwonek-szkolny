
from tkinter import *

window = Tk()
window.title("Plan")
window.geometry("860x720")

# Przycisk
add_button = Button(window, text="Add")
update_button = Button(window, text="Update")
update_button.place(x=10, y=10)

frame = Frame(window)
frame.pack(pady=20)

# dni tygodnia
days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]

# petla do wyswietlenia dni tygodnia
for i, day in enumerate(days):
    label = Label(frame, text=day, borderwidth=2, relief="solid", width=15)
    label.grid(row=0, column=i)

canvas = Canvas(window, width=860, height=720)
canvas.pack()

# linie pionowe

for i in range(1, len(days)):
    x_position = 155
    canvas.create_line(x_position, 0, x_position, 720,fill="black")

for i in range(1, len(days)):
    x_position = 265 
    canvas.create_line(x_position, 0, x_position, 720,fill="black")

for i in range(1, len(days)):
    x_position = 375
    canvas.create_line(x_position, 0, x_position, 720,fill="black")

for i in range(1, len(days)):
    x_position = 485
    canvas.create_line(x_position, 0, x_position, 720,fill="black")

for i in range(1, len(days)):
    x_position = 595
    canvas.create_line(x_position, 0, x_position, 720,fill="black")

for i in range(1, len(days)):
    x_position = 705
    canvas.create_line(x_position, 0, x_position, 720,fill="black")


# linie poziome
row_height = 80  # wysokosc komorki
for i in range(1, 8):  # od kiedy linie sie zaczynaja (1 sama gora, 8 sam dół)
    y_position = i * row_height
    canvas.create_line(70, y_position, 705, y_position, fill="black")


# Dana godzina    (x(satałe),y)
canvas.create_text(80, 50, text="8:00 - 8:45", anchor="w")
canvas.create_text(80, 130, text="8:55 - 9:35", anchor="w")
canvas.create_text(80, 210, text="9:40 - 10:25", anchor="w")
canvas.create_text(80, 290, text="10:35 - 11:20", anchor="w")
canvas.create_text(80, 370, text="11:30 - 12:15", anchor="w")
canvas.create_text(80, 450, text="12:30 - 13:15", anchor="w")
canvas.create_text(80, 530, text="13:20 - 14:05", anchor="w")
canvas.create_text(80, 610, text="14:10 - 14:55", anchor="w")




window.mainloop()
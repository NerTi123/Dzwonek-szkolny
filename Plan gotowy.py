from tkinter import *

window = Tk()
window.title("Plan")
window.geometry("860x900")

# Nowe okno do dodowania lekcji
def open_popup():
    popup = Toplevel(window)
    popup.title("Leckja")
    popup.geometry("300x400")
    
    # input field
    Label(popup, text="Lekcja", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Subject input
    Label(popup, text="Przedmiot:").pack(pady=5)
    subject_entry = Entry(popup, width=30)
    subject_entry.pack()
    
    # Day selection
    Label(popup, text="Dzień:").pack(pady=5)
    day_var = StringVar(popup)
    day_var.set(days[0])
    day_menu = OptionMenu(popup, day_var, *days)
    day_menu.pack()
    
    # Time selection
    Label(popup, text="Czas:").pack(pady=5)
    times = ["8:00 - 8:45", "8:55 - 9:35", "9:40 - 10:25", "10:35 - 11:20",
             "11:30 - 12:15", "12:30 - 13:15", "13:20 - 14:05", "14:10 - 14:55", "15:00 - 15:45"]
    time_var = StringVar(popup)
    time_var.set(times[0])
    time_menu = OptionMenu(popup, time_var, *times)
    time_menu.pack()
    
    # Zapisz button
    def save_subject():
        subject = subject_entry.get()
        day_index = days.index(day_var.get())
        time_index = times.index(time_var.get())
        
        # Calculate position for the text
        x_position = 155 + (day_index * 110) + 55
        y_position = 50 + (time_index * 80)
        
        # Add text to canvas
        canvas.create_text(x_position, y_position, text=subject, anchor="center")
        popup.destroy()
    
    Button(popup, text="Zapisz", command=save_subject).pack(pady=20)

add_button = Button(window, text="Add", command=open_popup)
update_button = Button(window, text="Dodaj", command=open_popup)
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
for i in range(1, 10):  # od kiedy linie sie zaczynaja (1 sama gora, 10 sam dół)
    y_position = i * row_height
    canvas.create_line(70, y_position, 705, y_position, fill="black")


# Dana godzina    (x   ,y)
canvas.create_text(80, 50, text="8:00 - 8:45", anchor="w")
canvas.create_text(80, 130, text="8:55 - 9:35", anchor="w")
canvas.create_text(80, 210, text="9:40 - 10:25", anchor="w")
canvas.create_text(80, 290, text="10:35 - 11:20", anchor="w")
canvas.create_text(80, 370, text="11:30 - 12:15", anchor="w")
canvas.create_text(80, 450, text="12:30 - 13:15", anchor="w")
canvas.create_text(80, 530, text="13:20 - 14:05", anchor="w")
canvas.create_text(80, 610, text="14:10 - 14:55", anchor="w")
canvas.create_text(80, 690, text="15:00 - 15:45", anchor="w")


# usuwanie prawym
def delete_subject(event):
    # Get the clicked coordinates
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    
    # Find all text items at the clicked position
    items = canvas.find_overlapping(x-5, y-5, x+5, y+5)
    for item in items:
        if canvas.type(item) == "text" and item not in time_labels:
            canvas.delete(item)


time_labels = []

# Godziny lekcji z lewej storny
time_labels.append(canvas.create_text(80, 50, text="8:00 - 8:45", anchor="w"))
time_labels.append(canvas.create_text(80, 130, text="8:55 - 9:35", anchor="w"))
time_labels.append(canvas.create_text(80, 210, text="9:40 - 10:25", anchor="w"))
time_labels.append(canvas.create_text(80, 290, text="10:35 - 11:20", anchor="w"))
time_labels.append(canvas.create_text(80, 370, text="11:30 - 12:15", anchor="w"))
time_labels.append(canvas.create_text(80, 450, text="12:30 - 13:15", anchor="w"))
time_labels.append(canvas.create_text(80, 530, text="13:20 - 14:05", anchor="w"))
time_labels.append(canvas.create_text(80, 610, text="14:10 - 14:55", anchor="w"))
time_labels.append(canvas.create_text(80, 690, text="15:00 - 15:45", anchor="w"))

# Usuniecie lekcji przy kliknieciu prawym przyciskiem myszy
canvas.bind("<Button-3>", delete_subject)  



window.mainloop()

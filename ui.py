import tkinter as tk
from tkinter import messagebox
from main import add_car, view_all_cars  

def submit_car():
    car = entry_car.get()
    owner = entry_owner.get()
    year = int(entry_year.get())
    km = int(entry_km.get())

    add_car(car, owner, year, km)
    messagebox.showinfo("Success", "Car added!")

def show_all_cars():
    cars = view_all_cars()
    for row in cars:
        print(row)  # You can also show this in a new window or listbox

# GUI setup
window = tk.Tk()
window.title("Car Info System")

tk.Label(window, text="Car Number").grid(row=0)
tk.Label(window, text="Owner Name").grid(row=1)
tk.Label(window, text="Model Year").grid(row=2)
tk.Label(window, text="Service KM").grid(row=3)

entry_car = tk.Entry(window)
entry_owner = tk.Entry(window)
entry_year = tk.Entry(window)
entry_km = tk.Entry(window)

entry_car.grid(row=0, column=1)
entry_owner.grid(row=1, column=1)
entry_year.grid(row=2, column=1)
entry_km.grid(row=3, column=1)

tk.Button(window, text="Add Car", command=submit_car).grid(row=4, column=1)
tk.Button(window, text="View All Cars", command=show_all_cars).grid(row=5, column=1)

window.mainloop()

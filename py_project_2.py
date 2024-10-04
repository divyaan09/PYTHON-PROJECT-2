<<<------------------- FLIGHT RESERVATION SYSTEM ---------------------->>>

import tkinter as tk
from tkinter import messagebox

NUM_SEATS = 10
seats = [None] * NUM_SEATS

class Passenger:
    def __init__(self, name, age, seat_number):
        self.name = name
        self.age = age
        self.seat_number = seat_number

class Flight:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time

flights = [
    Flight("ABC123", "New York", "2024-04-20 09:00"),
    Flight("DEF456", "Los Angeles", "2024-04-20 10:30"),
    Flight("GHI789", "Chicago", "2024-04-20 12:00")
]

def book_seat():
    seat_number = seat_entry.get()
    if not seat_number.isdigit() or not (1 <= int(seat_number) <= NUM_SEATS):
        messagebox.showerror("Invalid Input", "Enter a valid seat number between 1 and 10.")
        return

    seat_number = int(seat_number)
    if seats[seat_number - 1] is not None:
        messagebox.showerror("Seat Taken", f"Seat {seat_number} is already booked.")
    else:
        name = name_entry.get()
        age = age_entry.get()
        if not name or not age:
            messagebox.showerror("Invalid Input", "Please enter both name and age.")
            return

        passenger = Passenger(name, age, seat_number)
        seats[seat_number - 1] = passenger
        messagebox.showinfo("Success", f"Seat {seat_number} booked successfully for {name}.")

def cancel_seat():
    seat_number = seat_entry.get()
    if not seat_number.isdigit() or not (1 <= int(seat_number) <= NUM_SEATS):
        messagebox.showerror("Invalid Input", "Enter a valid seat number between 1 and 10.")
        return

    seat_number = int(seat_number)
    if seats[seat_number - 1] is None:
        messagebox.showerror("Invalid Action", f"Seat {seat_number} is not booked.")
    else:
        seats[seat_number - 1] = None
        messagebox.showinfo("Success", f"Reservation for seat {seat_number} cancelled.")

def view_available_seats():
    available_seats = [str(i + 1) for i, seat in enumerate(seats) if seat is None]
    available_seats_str = ", ".join(available_seats) if available_seats else "No seats available."
    messagebox.showinfo("Available Seats", f"Available seats: {available_seats_str}")

def display_flights():
    flights_info = "\n".join([f"Flight Number: {f.flight_number}, Destination: {f.destination}, Departure Time: {f.departure_time}" for f in flights])
    messagebox.showinfo("Flights", flights_info)

root = tk.Tk()
root.title("Flight Reservation System")
root.geometry("400x400")
root.configure(bg="#ADD8E6")

title_label = tk.Label(root, text="Flight Reservation System", font=("Arial", 16), bg="#ADD8E6")
title_label.pack(pady=10)

name_label = tk.Label(root, text="Passenger Name:", font=("Arial", 12), bg="#ADD8E6")
name_label.pack(pady=5)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

age_label = tk.Label(root, text="Passenger Age:", font=("Arial", 12), bg="#ADD8E6")
age_label.pack(pady=5)
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.pack(pady=5)

seat_label = tk.Label(root, text="Seat Number (1-10):", font=("Arial", 12), bg="#ADD8E6")
seat_label.pack(pady=5)
seat_entry = tk.Entry(root, font=("Arial", 12))
seat_entry.pack(pady=5)

book_button = tk.Button(root, text="Book Seat", command=book_seat, font=("Arial", 12), bg="lightgreen")
book_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel Reservation", command=cancel_seat, font=("Arial", 12), bg="lightcoral")
cancel_button.pack(pady=10)

view_seats_button = tk.Button(root, text="View Available Seats", command=view_available_seats, font=("Arial", 12), bg="lightblue")
view_seats_button.pack(pady=10)

view_flights_button = tk.Button(root, text="View Flights", command=display_flights, font=("Arial", 12), bg="lightyellow")
view_flights_button.pack(pady=10)

root.mainloop()

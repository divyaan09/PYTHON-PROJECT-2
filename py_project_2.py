# <<<------------------- FLIGHT RESERVATION SYSTEM --------------------->>>

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

def display_menu():
    print("\nFlight Reservation System")
    print("1. Book a Seat")
    print("2. Cancel Reservation")
    print("3. View Available Seats")
    print("4. View Flights")
    print("5. Exit")

def get_passenger_info():
    name = input("Enter passenger name: ")
    age = input("Enter passenger age: ")
    return name, age

def book_seat():
    seat_number = int(input(f"Enter seat number (1-{NUM_SEATS}): "))
    if seat_number < 1 or seat_number > NUM_SEATS:
        print("Invalid seat number.")
        return

    if seats[seat_number - 1] is not None:
        print(f"Seat {seat_number} is already booked.")
    else:
        name, age = get_passenger_info()
        passenger = Passenger(name, age, seat_number)
        seats[seat_number - 1] = passenger
        print(f"Seat {seat_number} booked successfully for {passenger.name}.")

def cancel_reservation():
    seat_number = int(input("Enter seat number to cancel reservation: "))
    if seat_number < 1 or seat_number > NUM_SEATS:
        print("Invalid seat number.")
        return

    if seats[seat_number - 1] is None:
        print(f"Seat {seat_number} is not booked.")
    else:
        seats[seat_number - 1] = None
        print(f"Reservation for seat {seat_number} cancelled.")

def view_available_seats():
    print("Available seats:")
    for i, seat in enumerate(seats):
        if seat is None:
            print(f"Seat {i + 1}")

def display_flights():
    print("Available Flights:")
    for flight in flights:
        print(f"Flight Number: {flight.flight_number}, Destination: {flight.destination}, Departure Time: {flight.departure_time}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            book_seat()
        elif choice == '2':
            cancel_reservation()
        elif choice == '3':
            view_available_seats()
        elif choice == '4':
            display_flights()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

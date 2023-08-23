class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def flights_for_city(self, city):
        city_flights = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                city_flights.append(flight)
        return city_flights

    def flights_from_city(self, city):
        city_flights = []
        for flight in self.flights:
            if flight.source == city:
                city_flights.append(flight)
        return city_flights

    def flights_between_cities(self, city1, city2):
        city_flights = []
        for flight in self.flights:
            if (flight.source == city1 and flight.destination == city2) or \
               (flight.source == city2 and flight.destination == city1):
                city_flights.append(flight)
        return city_flights

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("Choose search parameter:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        choice = int(input())

        if choice == 1:
            city = input("Enter city code: ").upper()
            city_name = cities.get(city, "Unknown City")
            city_flights = flight_table.flights_for_city(city)
            print(f"Flights for {city_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 2:
            city = input("Enter city code: ").upper()
            city_name = cities.get(city, "Unknown City")
            city_flights = flight_table.flights_from_city(city)
            print(f"Flights from {city_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 3:
            city1 = input("Enter first city code: ").upper()
            city2 = input("Enter second city code: ").upper()
            city1_name = cities.get(city1, "Unknown City")
            city2_name = cities.get(city2, "Unknown City")
            city_flights = flight_table.flights_between_cities(city1, city2)
            print(f"Flights between {city1_name} and {city2_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        else:
            print("Invalid choice. Please choose a valid option.")

        another_search = input("Do you want to perform another search? (yes/no): ").lower()
        if another_search != "yes":
            break

if __name__ == "__main__":
    main()

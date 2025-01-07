'''
Murray Watt
mwatt29@uwo.ca
251341261
This code analyzes 
'''

def parse_flight_data(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Initialize the dictionary to store flight data
            all_flights = {}

            # Iterate through lines, skipping header
            for line in lines[1:]:
                # Split the line into individual pieces of flight information
                flight_info = line.strip().split(',')

                # Check if the line has enough elements
                if len(flight_info) < 10:
                    print(f"Skipping line: {line}")
                    continue

                # Convert flight number to lowercase
                flight_number = flight_info[0].lower()

                # Convert 'FlightDuration' to seconds
                duration_parts = list(map(int, flight_info[6].split(':')))
                flight_duration_seconds = duration_parts[0] * 3600 + duration_parts[1] * 60 + duration_parts[2]

                # Create a child dictionary for each flight
                flight_data = {
                    'DepartureAirport': flight_info[1].lower(),
                    'ArrivalAirport': flight_info[2].lower(),
                    'DepartureTime': flight_info[3],
                    'ArrivalTime': flight_info[4],
                    'Airline': flight_info[5].lower(),
                    'FlightDuration': flight_duration_seconds,
                    'AvgTicketPrice': int(flight_info[7]),
                    'Aircraft': flight_info[8].lower(),
                    'PassengerCount': int(flight_info[9])
                }

    

                # Add the child dictionary to the parent dictionary
                all_flights[flight_number] = flight_data

        return all_flights


    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{file_path}' not found.")
        return -1





def calculate_average_ticket_price(all_flights, airline):
    try:
        # Convert the airline name to lowercase for case-insensitive comparison
        airline = airline.lower()

        # Initialize variables for calculating average ticket price
        total_price = 0
        total_flights = 0

        # Iterate through all flights and sum up ticket prices for the specified airline
        for flight_number, flight_data in all_flights.items():
            if flight_data['Airline'].lower() == airline:
                total_price += flight_data['AvgTicketPrice']
                total_flights += 1

        # Calculate average ticket price or return 0 if no flights found
        if total_flights > 0:
            average_price = total_price / total_flights
            return round(average_price, 2)
        else:
            return 0

    except Exception as e:
        # Handle exceptions and return -1 in case of an error
        print(f"Error: {e}")
        return -1

def get_total_passengers_by_airline(all_flights):
    passengers_by_airline = {}

    try:
        # Iterate through all flights and sum up passengers for each airline
        for flight_data in all_flights.values():
            airline = flight_data['Airline'].lower()
            passengers = flight_data['PassengerCount']

            # Update the total passengers for the airline
            passengers_by_airline[airline] = passengers_by_airline.get(airline, 0) + passengers

        return passengers_by_airline

    except Exception as e:
        # Handle exceptions and return an empty dictionary in case of an error
        print(f"Error: {e}")
        return {}

def get_overnight_flights(all_flights):
    overnight_flights = []

    try:
        # Iterate through all flights and check if they are overnight flights
        for flight_number, flight_data in all_flights.items():
            departure_time = flight_data['DepartureTime']
            arrival_time = flight_data['ArrivalTime']

            # Extract day parts from departure and arrival times
            departure_day_part = departure_time.split(' ')[0]
            arrival_day_part = arrival_time.split(' ')[0]

            # Check if the flight is overnight
            if departure_day_part != arrival_day_part:
                overnight_flights.append(flight_number)

        return overnight_flights

    except Exception as e:
        # Handle exceptions and return an empty list in case of an error
        print(f"Error: {e}")
        return []


def get_top_n_aircraft(all_flights, n=3):
    try:
        # Initialize dictionary to store the count of flights for each aircraft model
        aircraft_count = {}

        # Count the flights for each aircraft model
        for flight_data in all_flights.values():
            aircraft_model = flight_data['Aircraft']
            aircraft_count[aircraft_model] = aircraft_count.get(aircraft_model, 0) + 1

        # Sort the aircraft_count dictionary items by count in descending order
        sorted_aircraft = sorted(aircraft_count.items(), key=lambda x: x[1], reverse=True)

        # Check if specified n is greater than the number of unique aircraft models
        if n > len(sorted_aircraft):
            raise ValueError("Invalid n value!")

        # Return the list of the top n aircraft models
        top_n_aircraft = [aircraft[0] for aircraft in sorted_aircraft[:n]]
        return top_n_aircraft

    except Exception as e:
        # Handle exceptions and return an empty list in case of an error
        print(f"Error: {e}")
        return []

def get_total_duration(all_flights, airports):
    try:
        # Initialize dictionary to store total durations for each airline
        airline_durations = {airline: 0 for airline in set(flight['Airline'] for flight in all_flights.values())}

        # Convert airport codes to lowercase
        airports = [airport.lower() for airport in airports]

        # Iterate through all flights
        for flight_data in all_flights.values():
            departure_airport = flight_data['DepartureAirport'].lower()
            arrival_airport = flight_data['ArrivalAirport'].lower()
            airline = flight_data['Airline']
            flight_duration_minutes = flight_data['FlightDuration']

            # Check if the flight involves airports in the provided list
            if departure_airport in airports and arrival_airport in airports:
                # Convert flight duration to whole hours
                flight_duration_hours = flight_duration_minutes // 60

                # Aggregate total duration for the corresponding airline
                airline_durations[airline] += flight_duration_hours

        return airline_durations

    except Exception as e:
        # Handle exceptions and return an empty dictionary in case of an error
        print(f"Error: {e}")
        return {}









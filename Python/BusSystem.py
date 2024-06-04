import threading
import random
import time
import string

# Stations list (A to Z)
stations = list(string.ascii_uppercase)
passengers = {}
# print(len(stations))
currentStationIndex = 0

class BusStation:

    def __init__(self):
        self.stations = stations

    def changing_station(self):
        global currentStationIndex        
        print('-' * 15)
        print(f'Current Station is: {self.stations[currentStationIndex]}')
        currentStationIndex = (currentStationIndex + 1) % len(self.stations)
        time.sleep(10)
    
    def destination_station(self):
        destination_station = random.randint(currentStationIndex+1,26)
        # print(type(destinat)
        print(f'The destination station is : {self.stations[destination_station]}')
        return self.stations[destination_station]


class TicketFair:
    def __init__(self, stations):
        
        self.stations = stations
        self.fare_per_station = 10

    def calculate_fair(self, departure, destination):
        try:
            departure_index = self.stations.index(departure)
            destination_index = self.stations.index(destination)
        except ValueError:
            raise ValueError('Invalid station name')

        self.departure_station = stations.index(self.departure)

        if departure_index == destination_index:
            return 0
        
        # calculate the number of stations in between departure and destination
        num_stations = abs(destination_index - departure_index)
        # calculate the fare for the trip
        fare = num_stations * self.fare_per_station
        return fare

    def match_fair(self, target_fare):
        num_stations = target_fare // self.fare_per_station
        possible_destinations = []
        for i in range(len(self.stations)):
            if i + num_stations < len(self.stations):
                possible_destinations.append(self.stations[i + num_stations])
            if i - num_stations >= 0:
                possible_destinations.append(self.stations[i - num_stations])
        return random.choice(possible_destinations)

class passengersData:

    def __init__(self):
        self.passengers = passengers

   
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters, k=length))
        return random_string
    
    
    def add_data(self,p_id,departure,destination,fare):
        p_id = self.generate_random_string(8)
        departure = self.departure_station
        passengers[p_id] = {'Departure Station' : departure, 'Destination Station : ' : destination, 'Ticket Fare : ' : fare}
        print(p_id)

    
def main():
    bus_station = BusStation()
    print('Welcome To Bus System')
    while True:
        t1 = threading.Thread(target=bus_station.changing_station)
        t2 = threading.Thread(target=bus_station.destination_station)
        t3 = threading.Thread(target=passengersData.add_data)
        print('1. Book a ticket')
        print('2. Exit')
        choice = '1'
        if choice == '1':
            t2.start()
            t3.start()
            t3.join()
            t2.join()
            
        t1.start()
        t1.join()
        time.sleep(1)


if __name__ == "__main__":
    main()

import threading
import random
import time
import string

# Stations list (A to Z)
stations = list(string.ascii_uppercase)
currentStationIndex = 0

class BusStation:
    def __init__(self):
        self.stations = stations

    def changing_station(self):
        global currentStationIndex        
        print('-' * 15)
        print(f'Current Station is: {self.stations[currentStationIndex]}')
        currentStationIndex = (currentStationIndex + 1) % len(self.stations)
        time.sleep(5)
    
    def destination_station(self):
        pass

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

def main():
    bus_station = BusStation()
    print('Welcome To Bus System')
    while True:
        t1 = threading.Thread(target=bus_station.changing_station)
        
        print('1. Book a ticket')
        print('2. Exit')
        choice = input('Enter your choice : ')
        if choice == '1':
            pass
        t1.start()
        t1.join()
        time.sleep(1)


if __name__ == "__main__":
    main()

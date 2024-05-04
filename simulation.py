import time
import os

class Simulation:
    def __init__(self, map, print_driver, char_matrix):
        self.map = map
        self.print_driver = print_driver
        self.char_matrix = char_matrix

    def update(self):
        """Update state of dynamic items on the map."""
        for road in self.map.roads:
            for item in road.road_items:
                item.update(1)  # Assuming we're updating every 1 second.

    def run(self):
        """Run the simulation, updating and printing the state every second."""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            self.update()
            self.map.print(self.print_driver, self.char_matrix)
            time.sleep(1)

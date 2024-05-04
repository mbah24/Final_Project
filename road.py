from enum import Enum

class Heading(Enum):
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"

class Road:
    def __init__(self, name, locx, locy, length, hdg):
        self.name = name
        self.locx = locx
        self.locy = locy
        self.length = length  # Ensure this attribute is named 'length'
        self.hdg = hdg
        self.road_items = []  # Initialize the road_items list here

    def display_info(self):
        return f"Name: {self.name}, Location: ({self.locx}, {self.locy}), Length: {self.length} km, Heading: {self.hdg}"

    def add_road_item(self, item):
        self.road_items.append(item)  # Now it can safely append items

    def print(self, print_driver, obj):
        # Assuming a simplified representation here; details could vary based on actual implementation
        print_driver.print_road(self, obj)
        for item in self.road_items:  # Ensure that each item can also be printed
            item.print(print_driver, obj)

class RoadItem:
    def __init__(self, mile_marker):
        self.mile_marker = mile_marker

    def print(self, print_driver, obj):
        print_driver.print_road_item(self, obj)

class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)
        print(f"Road named {road.name} added to the map.")

    def display(self, printer):
        if not self.roads:
            print("No roads to display.")
            return
        for road in self.roads:
            printer.print_road(road)
            for item in road.road_items:
                printer.print_traffic_light(item)

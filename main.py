from print_driver import ConsolePrint
from map import Map
from traffic_control import TrafficLight
from road import Road
import time
import os

def main():
    printer = ConsolePrint()
    map_instance = Map()
    main_road = Road("Downtown", 0.0, -0.09, 0.180, 'EAST')
    map_instance.add_road(main_road)

    traffic_lights = [
        TrafficLight(mile_marker=18, green_duration=12, yellow_duration=4, red_duration=7, position=(0, 12)),
        TrafficLight(mile_marker=45, green_duration=9, yellow_duration=4, red_duration=5, position=(6, 5))
    ]

    for light in traffic_lights:
        main_road.add_road_item(light)

    try:
        while True:
            for light in traffic_lights:
                light.update(1)  # Simulate time passing by 1 second
            map_instance.display(printer)
            time.sleep(1)  # Wait for 1 second before the next update
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for next print
    except KeyboardInterrupt:
        print("Simulation stopped.")

if __name__ == "__main__":
    main()


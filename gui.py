# gui.py (if necessary, adjust based on your existing implementation)
from road import *
from traffic_control import TrafficLight
class MetricGUI:
    def create_road(self, name, locx, locy, length, hdg):
        return Road(name, locx, locy, length, hdg)

    def create_traffic_light(self, mile_marker, green_duration, yellow_duration, red_duration, color):
        return TrafficLight(mile_marker, color)
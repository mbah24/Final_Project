from traffic_control import TrafficLight
class IPrintDriver:
    def print_road(self, road, obj):
        raise NotImplementedError("Subclasses should implement this!")

    def print_traffic_light(self, traffic_light, obj):
        raise NotImplementedError("Subclasses should implement this!")

class ConsolePrint:
    def print_road(self, road, obj=None):
        print(f"Road Name: {road.name}, Coordinates: ({road.locx}, {road.locy}), Length: {road.length} km, Heading: {road.hdg}")
        self.print_road_with_traffic_lights(road)

    def print_traffic_light(self, traffic_light, obj=None):
        pass  # We will handle traffic light printing in a unified road display function now

    def print_road_with_traffic_lights(self, road):
        # Initialize the road display with solid and dashed lines
        solid_line = '|' + ' ' * 58 + '|'
        dash_sequence = '|' + '-- ' * 19 + '|'

        # Create a display that includes the position of traffic lights
        road_display = [solid_line, dash_sequence, solid_line, dash_sequence, solid_line, dash_sequence, solid_line]

        for item in road.road_items:
            if isinstance(item, TrafficLight):
                color_code = {'GREEN': 'O', 'YELLOW': '-', 'RED': 'x'}.get(item.current_color(), ' ')
                pos = item.position
                if 0 <= pos[0] < len(road_display) and 0 <= pos[1] * 3 + 2 < len(road_display[pos[0]]):
                    line = list(road_display[pos[0]])
                    line[pos[1] * 3 + 2] = color_code  # Adjust index for traffic light position
                    road_display[pos[0]] = ''.join(line)

        for line in road_display:
            print(line)


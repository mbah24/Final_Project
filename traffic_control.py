from road import RoadItem
from enum import Enum

class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    YELLOW = 'Yellow'

class TrafficLight:
    def __init__(self, mile_marker, green_duration, yellow_duration, red_duration, position):
        self.mile_marker = mile_marker
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.position = position  # Add this line to store the position attribute
        self.state = 'red'  # Initial state, can start with any state
        self.timer = 0  # Initialize the timer


    def update(self, seconds=1):
        # Increment the timer with the number of seconds each cycle (usually 1 second)
        self.timer += seconds

        # Check the state and update based on timer and duration
        if self.state == 'green' and self.timer >= self.green_duration:
            self.state = 'yellow'
            self.timer = 0  # Reset timer when state changes
        elif self.state == 'yellow' and self.timer >= self.yellow_duration:
            self.state = 'red'
            self.timer = 0
        elif self.state == 'red' and self.timer >= self.red_duration:
            self.state = 'green'
            self.timer = 0

    def current_color(self):
        # Return the current color state
        return self.state.upper()
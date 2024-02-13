import os
from dotenv import load_dotenv
from sense_hat import SenseHat
from datetime import datetime

load_dotenv()

HAT_ROTATION = int(os.getenv('HAT_ROTATION', 0))

color = {
    'red': [255, 0, 0],
    'green': [0, 255, 0],
    'blue': [0, 0, 255],
    'yellow': [255, 255, 0],
    'orange': [255, 165, 0],
    'purple': [128, 0, 128],
    'white': [255, 255, 255],
    'black': [0, 0, 0]
}


class Hat:
    def __init__(self, price):
        self.price = price
        self.at_hour = self.current_hour()

        # Hat basics
        self.sense = SenseHat()
        self.sense.rotation = HAT_ROTATION
        self.sense.show_message("INIT", text_colour=color['white'])
        self.sense.stick.direction_any = self.joystick_action

    def joystick_action(self, event):
        if event.action == 'pressed':
            print('Joystick pressed', event.direction)
            if event.direction == 'middle':
                self.sense.show_message('Debug')
            if event.direction == 'up':
                self.sense.show_message(
                    "Max: " + str(self.price.max), text_colour=color['white'])
            elif event.direction == 'down':
                self.sense.show_message(
                    "Min: " + str(self.price.min), text_colour=color['white'])
            elif event.direction == 'left':
                self.at_hour = self.at_hour - 1
                print('Left', str(self.at_hour))
                prefix = "KLO " + str(self.at_hour) + ":: "
                self.sense.show_message(
                    prefix + str(self.price.hour[self.at_hour]), text_colour=color['white'])
            elif event.direction == 'right':
                self.at_hour = self.at_hour + 1
                print('Right', str(self.at_hour))
                prefix = "KLO " + str(self.at_hour) + ":: "
                self.sense.show_message(
                    prefix + str(self.price.hour[self.at_hour]), text_colour=color['white'])
        elif event.action == 'released':
            print('Joystick released', event.direction)

    # Get current hour as INT
    def current_hour(self):
        now = datetime.now()
        return int(now.strftime("%H"))

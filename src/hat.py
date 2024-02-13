import os
from dotenv import load_dotenv
from sense_hat import SenseHat
from datetime import datetime
import time

load_dotenv()

HAT_ROTATION = int(os.getenv('HAT_ROTATION', 0))
HAT_LOW_LIGHT = True if os.getenv('HAT_LOW_LIGHT') == 'True' else False
HAT_PREFIX_SCROLL_SPEED = float(os.getenv('HAT_PREFIX_SCROLL_SPEED', 0.05))
HAT_PRICE_SCROLL_SPEED = float(os.getenv('HAT_PRICE_SCROLL_SPEED', 0.9))

PRICE_NICE = float(os.getenv('PRICE_NICE', 5.0))
PRICE_OK = float(os.getenv('PRICE_OK', 7.0))

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
        self.sense.low_light = HAT_LOW_LIGHT
        self.sense.stick.direction_any = self.joystick_action

        self.display_init()

    def joystick_action(self, event):
        self.sense.clear()

        if event.action == 'pressed':
            print('Joystick pressed', event.direction)
            if event.direction == 'middle':
                print('Middle button')
                # self.at_hour = self.current_hour()
                # self.display_prefix("Avg")
                # self.display_price(self.price.avg)

                # self.display_current_hour()
                # self.display_price(self.price.hour[self.at_hour])
            if event.direction == 'up':
                self.display_prefix("Max")
                self.display_price(self.price.max)
            elif event.direction == 'down':
                self.display_prefix("Min")
                self.display_price(self.price.min)
            elif event.direction == 'left':
                self.at_hour = self.at_hour - 1
                self.display_current_hour()
                self.display_price(self.price.hour[self.at_hour])
            elif event.direction == 'right':
                self.at_hour = self.at_hour + 1
                self.display_current_hour()
                self.display_price(self.price.hour[self.at_hour])
        elif event.action == 'released':
            print('Joystick released', event.direction)

    # Get current hour as INT
    def current_hour(self):
        now = datetime.now()
        hour = now.strftime("%H")
        print('Current hour:', str(hour))
        return int(hour)

    def display_current_hour(self):
        prefix = "Klo " + str(self.at_hour) + ":: "
        self.sense.show_message(prefix, scroll_speed=0.05)

    def display_prefix(self, text):
        prefix = str(text) + ":: "
        self.sense.show_message(
            prefix, text_colour=color['white'], scroll_speed=HAT_PREFIX_SCROLL_SPEED)

    def display_init(self):
        self.sense.show_message(
            'INIT', text_colour=color['white'], scroll_speed=HAT_PREFIX_SCROLL_SPEED)

    def display_price(self, value):
        print('Current price:', str(value))
        valStr = str(round(value, 2))
        self.sense.show_message(
            valStr, text_colour=self.price_color(value), scroll_speed=HAT_PRICE_SCROLL_SPEED)

    def price_color(self, price):
        if price < PRICE_NICE:
            return color['green']
        elif price < PRICE_OK:
            return color['yellow']
        else:
            return color['red']

    def display_scheduled_message(self):
        self.display_current_hour()
        self.display_price(self.price.hour[self.at_hour])

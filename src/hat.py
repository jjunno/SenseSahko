import os
from dotenv import load_dotenv
from sense_hat import SenseHat

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
    def __init__(self):
        self.sense = SenseHat()
        self.sense.rotation = HAT_ROTATION
        self.sense.show_message("INIT", text_colour=color['white'])

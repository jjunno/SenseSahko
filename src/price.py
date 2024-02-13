import os
from dotenv import load_dotenv

load_dotenv()


class Price:
    def __init__(self, json):
        self.date = json['date']
        self.min = json['min']
        self.max = json['max']
        self.avg = json['avg']
        self.hours = json['hour']

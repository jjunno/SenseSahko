import os
from dotenv import load_dotenv

load_dotenv()


class Price:
    def __init__(self, json):
        self.date = json['date']
        self.min = json['min']
        self.max = json['max']
        self.avg = json['avg']
        self.hour = json['hour']
        self.vat = float(os.getenv('VAT', 0.24))
        self.add_vats()

    def add_vats(self):
        self.min = self.min * (1 + self.vat)
        self.max = self.max * (1 + self.vat)
        self.avg = self.avg * (1 + self.vat)
        for i, h in enumerate(self.hour):
            self.hour[i] = self.hour[i] * (1 + self.vat)

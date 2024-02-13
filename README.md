# SenseSahko
Display current Finnish electricity spot price using SenseHat joystick or by scheduling the message.

Quickly developed and tested on Raspberry Pi 5 8Gb. I was sick, had a sick leave and needed something fast and stupid to do.

# Quick start

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

(You might run in to some issues SenseHat (or related) libraries when running it in venv. https://github.com/astro-pi/python-sense-hat/issues/58#issuecomment-374414765)

# env

API_URL=https://tehopirtti.net/finnish_electricity_spot_price.json
USE_HAT=True
HAT_ROTATION=180
HAT_LOW_LIGHT=True
HAT_PREFIX_SCROLL_SPEED=0.05
HAT_PRICE_SCROLL_SPEED=0.1

PRICE_NICE=5.0
PRICE_OK=10.0
VAT=0.24

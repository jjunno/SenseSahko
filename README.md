# SenseSahko

Raspberry Pi (5) SenseHat pörssisähkökikkare

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# env

API_URL=https://tehopirtti.net/finnish_electricity_spot_price.json
USE_HAT=True
HAT_ROTATION=180
HAT_LOW_LIGHT=True
HAT_PREFIX_SCROLL_SPEED=0.05
HAT_PRICE_SCROLL_SPEED=0.1

PRICE_NICE=5.0
PRICE_OK=10.0

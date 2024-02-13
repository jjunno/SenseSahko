import os
import api
import price
import hat
from dotenv import load_dotenv

load_dotenv()


def main():

    a = api.Api()
    a.fetch()
    p = price.Price(a.json)

    s = hat.Hat(p)
    s.display_scheduled_message()


if __name__ == "__main__":
    main()

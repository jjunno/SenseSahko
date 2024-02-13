import os
import api
import price
import hat
from dotenv import load_dotenv

load_dotenv()

USE_HAT = True if os.getenv('USE_HAT') == 'True' else False


def main():
    if USE_HAT:
        print('Use hat')
    else:
        print('No hat')

    a = api.Api()
    a.fetch()
    p = price.Price(a.json)

    print('Min:', p.min)
    print('Max:', p.max)
    print('Avg:', p.avg)
    # for h in p.hour:
    #     print(h)

    if USE_HAT:
        s = hat.Hat(p)
    input('Press enter to exit')


if __name__ == "__main__":
    main()

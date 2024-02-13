import os
import api
import price
from dotenv import load_dotenv

load_dotenv()

def main():
  a = api.Api()
  a.fetch()
  p = price.Price(a.json)

  print('Min:', p.min)
  print('Max:', p.max)
  print('Avg:', p.avg)
  for h in p.hours:
    print(h)
  

if __name__ == "__main__":
    main()

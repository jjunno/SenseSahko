import os
import api
from dotenv import load_dotenv

load_dotenv()


def main():
  a = api.Api()
  a.fetch()
  

if __name__ == "__main__":
    main()

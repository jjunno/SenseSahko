import os
from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError

load_dotenv()

class Api:
  def __init__(self):
    self.url = os.getenv('API_URL')
    self.json = {}

  def fetch(self):
    print('Fetching data from API')
    try:
      response = requests.get(self.url)
      if (response.status_code == 200):
        self.json = response.json()
    except HTTPError as http_err:
        print(http_err)
    except Exception as err:
        print(err)
    else:
        print('Fetch OK')

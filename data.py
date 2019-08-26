""" Define different function for data api  """

import requests
import random

def num_fact_api():
    num = random.randint(0, 500)
    endpoint = random.choice(['trivia', 'math'])
    url = 'http://numbersapi.com/'+ str(num) + '/'+ endpoint
    page = requests.get(url)
    return page.text

if __name__ == '__main__':
    num_fact_api()

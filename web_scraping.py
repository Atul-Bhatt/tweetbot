
# the requests module will make requests from the websites
# BeautifulSoup module will parse the html from the browsers
# the os module will create folders in our directory
import requests
from bs4 import BeautifulSoup as bs
import os


# url with pictures of models
url = 'https://www.shoutmeloud.com/popular-internet-companies-and-founders-behind-them.html'

# download page for parsing and parse using bs
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create a directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass

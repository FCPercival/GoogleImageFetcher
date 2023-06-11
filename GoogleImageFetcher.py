from bs4 import BeautifulSoup
import urllib.request
import os
import re


class GoogleImageFetcher:
    def __init__(self, query, image_type="Action", directory=None):
        self.query = query
        self.image_type = image_type
        self.directory = directory

    def get_soup(self, url, header):
        return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), 'html.parser')

    def download_images(self):
        query = self.query.split()
        query = '+'.join(query)
        url = "https://www.google.com/search?tbm=isch&q=" + query

        print(url)
        header = {'User-Agent': 'Mozilla/5.0'}
        soup = self.get_soup(url, header)

        images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]

        if self.directory is None:
            home_dir = os.path.expanduser("~")
            images_dir = os.path.join(home_dir, "Images")
            DIR = images_dir
        else:
            DIR = self.directory

        cntr = len([i for i in os.listdir(DIR) if self.image_type in i]) + 1
        print(cntr)

        for img in images:
            raw_img = urllib.request.urlopen(img).read()
            with open(DIR + "/" + self.image_type + "_" + str(cntr) + ".jpg", 'wb') as f:
                f.write(raw_img)
            cntr += 1

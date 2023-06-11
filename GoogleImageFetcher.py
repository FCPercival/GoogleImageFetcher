#  MIT License
#
#  Copyright (c) 2023 Federico Vittorio Chiodo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

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

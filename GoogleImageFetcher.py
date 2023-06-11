from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import sys
import getopt

class ImageDownloader:
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
            DIR = "/home/federico/Immagini"
        else:
            DIR = self.directory

        cntr = len([i for i in os.listdir(DIR) if self.image_type in i]) + 1
        print(cntr)

        for img in images:
            raw_img = urllib.request.urlopen(img).read()
            with open(DIR + "/" + self.image_type + "_" + str(cntr) + ".jpg", 'wb') as f:
                f.write(raw_img)
            cntr += 1

def print_usage():
    print("Usage: python3 script.py -s <query> [-t <image_type>] [-dir <directory>] [-h]")
    print("Arguments:")
    print("  -s <query>            : Search query for images (required)")
    print("  -t <image_type>       : Image type (optional, default: Action)")
    print("  -dir <directory>      : Directory path for saving images (optional, default: /home/federico/Immagini)")
    print("  -h                    : Show help")

def main(argv):
    query = None
    image_type = "Action"
    directory = None

    try:
        opts, args = getopt.getopt(argv, "s:t:dir:h")
    except getopt.GetoptError:
        print("Error: Invalid arguments.")
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-s":
            query = arg
        elif opt == "-t":
            image_type = arg
        elif opt == "-dir":
            directory = arg
        elif opt == "-h":
            print_usage()
            sys.exit()

    if query is None:
        print("Error: Missing query.")
        print_usage()
        sys.exit(2)

    downloader = ImageDownloader(query, image_type, directory)
    downloader.download_images()

if __name__ == "__main__":
    main(sys.argv[1:])

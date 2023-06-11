import getopt
import sys
import os
from GoogleImageFetcher import GoogleImageFetcher


class CommandHandler:
    def __init__(self):
        self.query = None
        self.image_type = "Action"
        self.directory = None

    def print_usage(self):
        try:
            home_dir = os.path.expanduser("~")
            images_dir = os.path.join(home_dir, "Images")
            DIR = images_dir
        except FileNotFoundError:
            DIR = "ERROR FETCHING DIRECTORY"

        print("Usage: python3 main.py -s <query> [-t <image_type>] [-dir <directory>] [-h]")
        print("Arguments:")
        print("  -s <query>            : Search query for images (required)")
        print("  -t <image_type>       : Image type (optional, default: Action)")
        print("  -dir <directory>      : Directory path for saving images (optional, default: " + DIR + ")")
        print("  -h                    : Show help")

    def parse_arguments(self, argv):
        try:
            opts, args = getopt.getopt(argv, "s:t:dir:h")
        except getopt.GetoptError:
            self.print_usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-s":
                self.query = arg
            elif opt == "-t":
                self.image_type = arg
            elif opt == "-dir":
                self.directory = arg
            elif opt == "-h":
                self.print_usage()
                sys.exit()

        if self.query is None:
            print("Error: Missing query.")
            self.print_usage()
            sys.exit(2)

    def handle_commands(self, argv):
        self.parse_arguments(argv)
        fetcher = GoogleImageFetcher(self.query, self.image_type, self.directory)
        fetcher.download_images()

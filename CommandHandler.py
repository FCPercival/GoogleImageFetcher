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

        print("Usage: python3 main.py -s <query> [-t <image_type>] [-d <directory>] [-h]")
        print("Arguments:")
        print("  -s <query>            : Search query for images (required)")
        print("  -t <image_type>       : Image type (optional, default: Action)")
        print("  -d <directory>        : Directory path for saving images (optional, default: " + DIR + ")")
        print("  -h                    : Show help")

    def parse_arguments(self, argv):
        try:
            opts, args = getopt.getopt(argv, "s:t:d:h")
        except getopt.GetoptError:
            self.print_usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-s":
                self.query = arg
            elif opt == "-t":
                self.image_type = arg
            elif opt == "-d":
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

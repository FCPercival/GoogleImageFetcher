# GoogleImageFetcher
 
This is a simple fetcher for images using Google Images. (Fetches 20 images with one call)

The program constructs a URL based on the query and sends a request to Google, it then parses the HTML response using BeautifulSoup to extract the image URLs and saves the raw images to the specified directory or at the default directory.

Each image is saved with a unique filename based on the image type and a counter. (If the program has been run before and there are already images of the specified type in the destination directory, it continues the counter from the last saved image)

## USAGE
```
Usage: python3 main.py -s <query> [-t <image_type>] [-d <directory>] [-h]
Arguments:
  -s <query>            : Search query for images (required)
  -t <image_type>       : Image type (optional, default: Action)
  -d <directory>        : Directory path for saving images (optional, default: /home/<current_user>/Images)
  -h                    : Show help
```

To install all the required libraries use the command: <code>pip install -r requirements.txt</code>

### Examples

<code>python3 main.py -s "Cat" -t "Animal" -d "/home/user/images"</code>

# License
This project is under the MIT license, see the LICENSE file for more informations.

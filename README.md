# GoogleImageFetcher
 
This is a simple fetcher for images using Google Images (Fetches 20 images with one call)

## USAGE
```
Usage: python3 main.py -s <query> [-t <image_type>] [-d <directory>] [-h]
Arguments:
  -s <query>            : Search query for images (required)
  -t <image_type>       : Image type (optional, default: Action)
  -d <directory>        : Directory path for saving images (optional, default: /home/<current_user>/Images)
  -h                    : Show help
```

### Examples

<code>python3 main.py -s "Cat" -t "Animal" -d "/home/user/images"</code>

# License
This project is under the MIT license, see the LICENSE file for more informations

import shutil
import requests


imageURL = 'https://wallpapers.com/images/hd/avatar-the-last-airbender-pictures-n64tz1hvcd7gjqh1.jpg'

image_response = requests.get(imageURL, stream=True)

output_filename = 'downloaded_image.jpg'
with open(output_filename, 'wb') as out_file:
    shutil.copyfileobj(image_response.raw, out_file)
del image_response    # this frees up the memory (optional)
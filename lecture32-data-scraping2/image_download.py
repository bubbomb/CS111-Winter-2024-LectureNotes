import shutil
import requests


# imageURL = 'https://wallpapers.com/images/hd/avatar-the-last-airbender-pictures-n64tz1hvcd7gjqh1.jpg'


imageURL = 'https://i.pinimg.com/originals/8d/31/cc/8d31cca1c749792b9aaa7fd64499d888.jpg'
image_response = requests.get(imageURL, stream=True)

output_filename = 'avatar.jpg'
with open(output_filename, 'wb') as out_file:
    shutil.copyfileobj(image_response.raw, out_file)
del image_response    # this frees up the memory (optional)
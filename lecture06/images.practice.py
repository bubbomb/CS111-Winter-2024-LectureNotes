from byuimage import Image

def darken(image):
    for pixel in image:
        pixel.red = pixel.red * 0.5
        pixel.green = pixel.green * 0.5
        pixel.blue = pixel.blue * 0.5
    return image


def mute_top(image):
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_new = new_image.get_pixel(x, y)
            factor = 1.0
            if (pixel.red + pixel.blue + pixel.green)/3 > 220 and y < image.height//2:
                factor = 0.5
            pixel_new.red = pixel.red * factor
            pixel_new.green = pixel.green * factor
            pixel_new.blue = pixel.blue * factor
    return new_image

def bottom_black_border(image):
    new_image = Image.blank(image.width, image.height+50)  # Create the larger image.
    for y in range(image.height):                          # Copy the original image
        for x in range(image.width):                       #  into the top of the new
            pixel = image.get_pixel(x, y)                  #  one.
            pixel_new = new_image.get_pixel(x, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    for y in range(image.height,image.height+50):          # Make the pixels in the
        for x in range(image.width):                       #  bottom black. RGB for
            pixel_new = new_image.get_pixel(x, y)          #  black is (0,0,0).
            pixel_new.red = 0
            pixel_new.green = 0
            pixel_new.blue = 0

    return new_image

myImage = Image("gloomhaven.webp")
# myImage = darken(myImage)
# myImage = mute_top(myImage)
myImage = bottom_black_border(myImage)
myImage.show()
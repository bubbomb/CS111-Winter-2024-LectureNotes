from byuimage import Image
import sys

def darken(image, starting_y=0, starting_x=0):
    """ Pass in an image, modify it """
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel.red = pixel.red * 0.2
            pixel.green = pixel.green * 0.2
            pixel.blue = pixel.blue * 0.2
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

def detect_green(pixel):
    factor = 1.3
    threshold = 100
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

def change_to_red(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            if detect_green(pixel):
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0

    return image

def green_screen(foreground,background):
    final = Image.blank(background.width,background.height)
    for y in range(background.height):
        for x in range(background.width):
            fp = final.get_pixel(x,y)
            bp = background.get_pixel(x,y)
            fp.red = bp.red
            fp.green = bp.green
            fp.blue = bp.blue

    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp):
                np = final.get_pixel(x,y)
                np.red = fp.red
                np.green = fp.green
                np.blue =fp.blue
    return final

def detect_green(pixel, factor=1.3, threshold=100):
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

print(sys.argv)
foreground_image_path = sys.argv[1]
background_image_path = sys.argv[2]
charizard = Image(foreground_image_path)
mordor = Image(background_image_path)
myImage = green_screen(charizard, mordor)
myImage.show()
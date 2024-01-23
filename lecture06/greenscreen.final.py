from byuimage import Image


def detect_green(pixel):
    factor = 1.3
    threshold = 100
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

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


foreground = Image('images/keanu_reeves.jpeg')
background = Image('images/gloomhaven.webp')

final_image = green_screen(foreground, background)
final_image.show()

from PIL import Image

def what_is_the_secret(secret_image, s=4):
    data = Image.open(secret_image)
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x, y))
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s
            data.putpixel((x, y), (red, green, blue))
    return data


if __name__ == '__main__':
    what_is_the_secret('moran-wishes-the-best.png').save("goodLuck.png")

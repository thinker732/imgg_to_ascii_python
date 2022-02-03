import PIL.Image


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_img(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_heigth = int(new_width*ratio)
    resized_imgage = image.resize((new_width, new_heigth))
    return (resized_imgage)


# convert pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=100):
    # img from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not a valid img")

    # convert to ascii
    new_image_data = pixel_to_ascii(grayify(resize_img(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save image to txt
    with open("ascii_to_image.txt", "w") as f:
        f.write(ascii_image)


main()

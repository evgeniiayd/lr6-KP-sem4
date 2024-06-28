def check_image(filename):
    if filename:
        from PIL import Image

        with Image.open(filename) as img:
            img.load()
            print(img.size[0], img.size[1])

            return img.size[0], img.size[1]
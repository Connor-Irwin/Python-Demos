from PIL import Image

while True:
    inImage = input("Input image: ")

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.open(inImage)

    # converts to RGBA (red, green, blue, alpha)
    img = img.convert(mode="RGBA")

    # create the pixel map
    pixels = img.load()

    # start removing pixels
    for x in range(img.size[0]):    # for every row
        for y in range(img.size[1]):    # For every column
            #if black, make transparent
            if pixels[x,y] == (0, 0, 0, 255):
                pixels[x,y] = (0, 0, 0, 0)

    outImage = input("Output image (blank = replace input image): ")

    if outImage == "":
        outImage = inImage

    try:
        img.save(outImage, optimize=True)
    except:
        img = img.convert(mode="RGB")
        img.save(outImage, optimize=True, quality=100)

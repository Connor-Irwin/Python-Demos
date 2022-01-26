from PIL import Image

while True:
    inImage = input("Input image: ")

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.open(inImage)

    # converts to RGBA (red, green, blue, alpha)
    img = img.convert(mode="RGBA")

    # create the pixel map
    pixels = img.load()

    # most common pixel and its frequency
    mostCommon = (0, 0, 0, 0)
    mostCommonFrequency = 0

    # get most common pixel (besides transparent)
    for x1 in range(img.size[0]):
        for y1 in range(img.size[1]):
            if mostCommonFrequency > x1 * y1 / 2:
                break
            currentPixelFrequency = 0
            for x2 in range(img.size[0]):
                if pixels[x1,y1] == (0, 0, 0, 0):
                    break
                for y2 in range(img.size[1]):
                    if pixels[x1,y1] == pixels[x2,y2]:
                        currentPixelFrequency += 1
            if currentPixelFrequency > mostCommonFrequency:
                mostCommonFrequency = currentPixelFrequency
                mostCommon = pixels[x1,y1]

    # start removing pixels
    for x in range(img.size[0]):    # for every row
        for y in range(img.size[1]):    # For every column
            #if black, make transparent
            if pixels[x,y] == mostCommon:
                pixels[x,y] = (0, 0, 0, 0)

    outImage = input("Output image (blank = replace input image): ")

    if outImage == "":
        outImage = inImage

    try:
        img.save(outImage, optimize=True)
    except:
        img = img.convert(mode="RGB")
        img.save(outImage, optimize=True, quality=100)

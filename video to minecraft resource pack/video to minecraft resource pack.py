########################
#                      #
# Made by Connor Irwin #
#                      #
########################

from os import system, makedirs
from PIL import Image
from PIL.ImageDraw import Draw
from glob import glob
from shutil import rmtree
from math import log2, ceil

# Makes a picture into a perfect square without cropping it. Also make the image be the correct aspect ration (16x16 or 32x32 or 64x64).
def expand2square(pil_img):
    width, height = pil_img.size

    result = pil_img

    background_color = (0, 0, 0)
    
    if width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, ceil((width - height) / 2)))

    if width < height:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, (ceil((height - width) / 2), 0))

    width, height = result.size

    if 2 ** ceil(log2(width)) >= 128:
        # Scales the image to 128x128
        return result.resize((128, 128))
    else:
        # Scales the image correctly
        return result.resize((2 ** ceil(log2(width)), 2 ** ceil(log2(width))))

print("This application requires \"FFmpeg\" to be installed to work correctly.\n")

# Take in some inputs
resourcePackName = input("Please enter a name for the resource pack: ")
packDescription = input("\nPlease enter a resource pack description: ")
discDescription = input("\nPlease enter an audio disc description: ")
fps = int(input("\nPlease enter FPS of sprite sheet (Must be 20 or less and a multiple of 20. Can be a fraction or decimal.): "))
inputFile = input("\nPlease enter the path of a video file: ")

# Make the "images" directory
try:
    makedirs("images")
except:
    print("\nCould not create directory, \"images\". Make sure this directory does not exist already.")
    input("\nPress enter to close this window")
    quit()

# Make the *resourcePackName* directory and subdirectories
try:
    makedirs(resourcePackName + "/assets/minecraft/textures/painting")
    makedirs(resourcePackName + "/assets/minecraft/sounds/records")
    makedirs(resourcePackName + "/assets/minecraft/lang")
except:
    print("\nCould not create directory, \"" + resourcePackName + "\" or one of its subdirectories. Make sure this directory does not exist already.")
    input("\nPress enter to close this window")
    rmtree("images")
    quit()

print("\nExtracting images...\n")
# Takes in "input.mp4" and outputs *fps* frames per second as a png image
system("ffmpeg -i " + inputFile + " -vf fps=" + str(fps) + " images/%d.png")
print("Done.\n")

# Make the count down images (these start with negative numbers with the first being the smallest number)
sizeOfImages = expand2square(Image.open("images/1.png")).size
for i in range(-1 * fps * 10, 0):
    img = Image.new(size=sizeOfImages, mode="RGB")
    textImg = Draw(img)
    textImg.text((sizeOfImages[0] // 2, sizeOfImages[1] // 2), str(i * -1 // fps))
    img.save("images/" + str(i) + ".png")

# Creates list of all images in the "images" directory
images = glob("images/*.png")
images = sorted(images, key=lambda i: int(i.split('.')[0].split("\\")[1]))
spriteSheetSize = (sizeOfImages[0], sizeOfImages[1] * len(images))
spriteSheet = Image.new(size=spriteSheetSize, mode="RGB")

print("Creating sprite sheet...")

for i, item in enumerate(images):   
    image = expand2square(Image.open(item))
    spriteSheet.paste(image, (0, i * sizeOfImages[1]))
    image.close()

print("Done.\n")

print("Creating resource pack...")

# Make the resource pack
# Make the "pack.mcmeta" file
file = open(resourcePackName + "/pack.mcmeta", "w")
file.write("{\"pack\":{\"pack_format\":6,\"description\":\"" + packDescription + "\"}}")
file.close()

# Make the "pack.png" image
expand2square(Image.open(images[len(images) // 2])).save(resourcePackName + "/pack.png", optimize=True)

# Make the "en_us.json" file
file = open(resourcePackName + "/assets/minecraft/lang/en_us.json", "w")
file.write("{\"item.minecraft.music_disc_13.desc\":\"" + discDescription + "\"}")
file.close()

# Make the "13.ogg" file
system("ffmpeg -i " + inputFile + " -q:a 0 -map a \"" + resourcePackName + "/assets/minecraft/sounds/records/13.ogg\"")

# Make the "pointer.png.mcmeta" file
file = open(resourcePackName + "/assets/minecraft/textures/painting/pointer.png.mcmeta", "w")
file.write("{\"animation\":{\"frametime\":" + str(20 / fps) + ",\"frames\":" + str([i for i in range(len(images))]) + "}}")
file.close()

print("Done.\n")

print("Saving sprite sheet (this might take a while)...")
spriteSheet.save(resourcePackName + "/assets/minecraft/textures/painting/pointer.png", optimize=True)

rmtree("images")

print("Done.\n")
input("Press enter to close window.")

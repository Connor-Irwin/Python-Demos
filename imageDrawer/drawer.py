from PIL import Image
from mouse import move, click, press, release, is_pressed as mouse_is_pressed
from time import sleep
from keyboard import is_pressed as keyboard_is_pressed

# Sleepss
sleep(5)

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.open('youngReyna.jpg')

# converts to monochrome
img = img.convert(mode='1')

# create the pixel map
pixels = img.load()

xOffSet = 25
yOffSet = 160

# Distance between dots
dotDistance = 1

# Draw an imaginary border as a test

move((0 * dotDistance + xOffSet), (0 * dotDistance + yOffSet))
sleep(.5)
move((img.size[0] * dotDistance + xOffSet), (0 * dotDistance + yOffSet))
sleep(.5)
move((img.size[0] * dotDistance + xOffSet), (img.size[1] * dotDistance + yOffSet))
sleep(.5)
move((0 * dotDistance + xOffSet), (img.size[1] * dotDistance + yOffSet))
sleep(.5)
move((0 * dotDistance + xOffSet), (0 * dotDistance + yOffSet))
sleep(.5)

# Sleep some more
sleep(5)

# Start drawing
for x in range(img.size[0]):    # for every col:
    for y in range(img.size[1]):    # For every row
        if keyboard_is_pressed('q'):
            release()
            break
        elif pixels[x,y] == 0:
            if mouse_is_pressed() == False and y < img.size[1]-1 and pixels[x, y+1] == 0:
                move(x * dotDistance + xOffSet, y * dotDistance + yOffSet)
                press()
            else:
                move(x * dotDistance + xOffSet, y * dotDistance + yOffSet)
                release()
                click()
            #sleep(.0001)

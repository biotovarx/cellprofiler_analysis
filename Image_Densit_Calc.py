

# This script will calculate the RGB pixel values within an image


# Imports the necessary packages
from PIL import Image
from shutil import copyfile
import os
import sys

# Check the correct number of arguments

if len(sys.argv) != 3:
    print("*** ERROR:  NO FILE SPECIFIED IN ARGUMENT ***")
    print("Enter the directory with the tiled images")
    print("Example: python3 Image_Densit_Calc.py image_tiles out")
    sys.exit(0)

# Initializes the values
dense_tiles = {}
filename_list = []

# Loops through all of the image tiles in the given directory
for filename in os.listdir(sys.argv[1]):

    # for filename in os.listdir("./image_tiles"):
    # Clears the number of non-white pixels
    non_white = 0

    # Opens the tile image
    im = Image.open(sys.argv[1]+"/"+filename)  # Can be many different formats.
    # im = Image.open("./image_tiles/" + filename)

    # Checks that the image is 1000 pixels x 1000 pixels, otherwise moves to the next file
    if im.size != (1000, 1000):
        continue

    # Loads the image into a 1000 x 1000 pixel array
    pix = im.load()

    # Loops through all of the pixels on the x-axis
    for i in range(1, im.size[0]):
        # Loops through all of the pixels on the y-axis
        for j in range(1, im.size[1]):
            # Assigns RGB pixels from pixel array at x,y coordinates
            red_pix = pix[i, j][0]
            green_pix = pix[i, j][1]
            blue_pix = pix[i, j][2]
            # checks if pixel is above color threshold for white
            if red_pix and green_pix and blue_pix > 200:
                continue
            else:
                # Pixel is not above threshold, counted as not white pixel
                non_white += 1

    # Calculate the Image density and assign it in dictionary associated with filename
    image_density = (non_white / (im.size[0]*im.size[1])) * 100
    dense_tiles[round(image_density, 3)] = filename

# Takes a sorted list of the densities for each tile and reverses it
density = reversed(sorted(dense_tiles))

# Takes density from the reverse list, uses it as key to retrieve filename value from diction and make value list
for item in density:
    filename_list.append(dense_tiles[item])

# Creates a directory to copy the ten densest tile images
old_directory_name = sys.argv[1].replace('/', '')
new_directory_name = sys.argv[2]
if not os.path.exists(new_directory_name):
    os.makedirs(new_directory_name)

# Copies the ten densest images to the newly created directory
for tile_file in filename_list[0:10]:
    copyfile(sys.argv[1] + "/" + tile_file, new_directory_name + "/" + tile_file)


# with open("RGB_output.txt", "w") as f:

    # for imag in total_list[0:10]:
#        f.write(imag + "\n\n")

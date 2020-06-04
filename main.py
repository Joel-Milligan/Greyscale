from skimage import io, data, color
import numpy as np
import os

def main():
    directory = os.fsencode("./Coloured Images")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename != ".keep":
            old_img = io.imread(f"./Coloured Images/{filename}")
            new_img = color.rgb2gray(old_img)
            io.imsave(f"./Greyscale Images/{filename.split('.')[0]}_grey.png", new_img)

    # {filename.split('.')[1]}

if __name__ == "__main__":
    main()

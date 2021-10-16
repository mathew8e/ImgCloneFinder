from PIL import Image
from os import listdir
import numpy as np


def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)

    return loadedImages


def convImgToNpArrays(array):
    #function for creating a np array
    numpyimg = []
    for i in range(len(array)):
        numpyimg.append(np.asarray(imgs[i]))
    return numpyimg

# checking each photo with eacho
def cloneFind(npimgs):
    cloneImgArray = []
    for imgIndex1 in range(len(npimgs)):
        for imgIndex2 in range(len(npimgs)):
            if npimgs[imgIndex1].all() == npimgs[imgIndex2].all() and imgIndex1 != imgIndex2:

                cloneImgArray.append(imgs[imgIndex1].filename)
                cloneImgArray.append(imgs[imgIndex2].filename)

    #this return statement is funny lol XD
    return list(set(cloneImgArray))

#path specified will change later
path = ".//images/"

# images in an regular array
imgs = loadImages(path)

# change images to an np array
npimgs = convImgToNpArrays(imgs)

print(cloneFind(npimgs))

            
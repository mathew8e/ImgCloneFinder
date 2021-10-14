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


path = ".//images/"

# your images in an array
imgs = loadImages(path)




        

'''for imgIndex1 in range(len(imgs)):
    for imgIndex2 in range(len(imgs)):
        if imgs[imgIndex1].getdata == imgs[imgIndex2].getdata:
            print(2)
        if imgs[imgIndex1].getdata == imgs[imgIndex2].getdata and imgIndex1 != imgIndex2:
            print(1)'''
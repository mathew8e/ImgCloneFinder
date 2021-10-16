from PIL import Image
from os import listdir
import numpy as np


#make a progress bar

def loadImages(path):
    # return array of images

    print("Started img loading")
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)
    print("Finished img loading")
    return loadedImages


def convImgToNpArrays(array):
    #function for creating a np array
    print("Started np converting")
    numpyimg = []
    for i in range(len(array)):
        numpyimg.append(np.asarray(imgs[i]))
    print("Np convert end")
    return numpyimg

# checking each photo with eacho
def cloneFind(npimgs):
    #make this an np array so you can have a array in array
    cloneImgArray = []
    for imgIndex1 in range(len(npimgs)):
        print("checking",imgIndex1," from ", len(npimgs))
        for imgIndex2 in range(len(npimgs)):
            if np.array_equal(npimgs[imgIndex1], npimgs[imgIndex2]) and imgIndex1 != imgIndex2:
                print("Found ",imgs[imgIndex1].filename.replace(path, '')," with ",imgs[imgIndex2].filename.replace(path,''))
                cloneImgArray.append(imgs[imgIndex1].filename.replace(path, ''))
                cloneImgArray.append(imgs[imgIndex2].filename.replace(path, ''))

    #return cloneImgArray

    #this return statement is funny lol XD return unique values
    return list(set(cloneImgArray))

#path specified will change later
path = "C://Users//mathe//Downloads//Images for the website October 9-20211011T180149Z-001//Images for the website October 9//Khlil Chaaban/"

# images in an regular array
imgs = loadImages(path)

# change images to an np array
npimgs = convImgToNpArrays(imgs)

cloneListArray = cloneFind(npimgs)

print(f"\n        Found these images as copy \n  {cloneListArray}")

            
from PIL import Image
from os import listdir, remove
import numpy as np


#make a progress bar

def loadImages(path):
    # return array of images

    print("Started img loading")
    imagesList = listdir(path)
    loadedImages = []
    for image in range(len(imagesList)):
        try:
            img = Image.open(path + imagesList[image])
        except PermissionError:
            print(" FILE: " + imagesList[image].replace(path,'')+" can't be opened it is proboaly a folder so it cant open it")
            quit()
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

def cloneFind(npimgs):
    # checking each photo with eachother

    dictOfIndexes = {}
    pairArray = {}

    #two indexes will go through all files
    for imgIndex1 in range(len(npimgs)):
        print("checking",imgIndex1," from ", len(npimgs))
        for imgIndex2 in range(len(npimgs)):

            #                 if imgs are the same                      if the img is not itself            if img clone isnt 2 1  1 2
            if np.array_equal(npimgs[imgIndex1], npimgs[imgIndex2]) and imgIndex1 != imgIndex2 and not(imgIndex1 in dictOfIndexes.values()) and not(imgIndex2 in dictOfIndexes.values()) and not(imgIndex2 in dictOfIndexes.keys()) and not(imgIndex1 in dictOfIndexes.values()):

                img1 = imgs[imgIndex1].filename #.replace(path, '')
                img2 = imgs[imgIndex2].filename #.replace(path, '') #this replaces the path

                # just some debugging
                print("Found ",img1," with ",img2)
                
                
                if img1 in pairArray.keys() :
                    print(pairArray[img1])
                    pairArray[img1].append(img2)
                elif not any([True for k,v in pairArray.items() if img1 in v]):
                    pairArray[img1] = [img2]

                #remembering matched indexes to not repeat itself
                dictOfIndexes[imgIndex1] = imgIndex2


    return pairArray

    #this return statement is funny lol XD return unique values
    #return list(set(cloneImgArrayOfArrays))

def deleteCloneImages(dictOfCloneImages):
    #this function will delete all unoriginal photos


    for k,v in dictOfCloneImages.items():
        for delImg in v:
            remove(delImg)
            print(f"removing {delImg} \n")




'''INSERT PATH HERE TO IMG FOLDER'''

#-----------------------------------------------------------------------------------------------------------------------------------------

winpath = r"C:\Users\mathe\Downloads\Images for the website October 9-20211011T180149Z-001\Images for the website October 9\Khlil Chaaban" # <----

#-----------------------------------------------------------------------------------------------------------------------------------------


path = winpath.replace("\\","//")+"/"

# images in an regular array
imgs = loadImages(path)

# change images to an np array
npimgs = convImgToNpArrays(imgs)

cloneListArray = cloneFind(npimgs)


#print(f"\n        Found these images as copy \n  {cloneListArray}")

            
deleteCloneImages(cloneListArray)
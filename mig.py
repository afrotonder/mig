"""
Metadata Image Generator (MIG): A simple python script with that inserts IPFS images into NFT JSONs
Author: Aftotonder
"""

import json
import os
import shutil
import glob
from datetime import date
import math
import random
import collections

# Creates a 32 charater string with random numbers/letters for the DNA
def genDNA(length):
  result = ""
  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  charactersLength = 62 #characters.length
  for i in range(32):
    result += characters[math.floor(random.randint(0, 61))]
  
  return result

# directory with metadata json files without image
directory = 'nftJsonDir'

# counter for metadata creation
count = 0

# final metadata array
metadata = []

# existing images directory
imageDir = './newImagesJSON/'

# temp array for sorted images
imagesList = []

# setup image array in proper order
# create array of images so its easier to sort. This is necessary, else python will sort the name array in the following order: 1, 10, 100, 1000, 110, etc 
for i in range(0, 782):

    # file name
    imgFile = imageDir+str(i+1)+'.json' 

    # open file
    images = open(imgFile)

    # load json from file
    imgJSON = json.load(images)

    # extract number id of image from image name. this is necessary to properly sort
    tempImg = {'id': int(imgJSON['image'].split('6im/')[1].split('.')[0]), 'image': imgJSON['image']}

    imagesList.append(tempImg)

    images.close()


# sort images in proper numeric order
sortedImages = sorted(imagesList, key = lambda i: i['id']) 


# counter for image names
nameCount = 1

for filename in os.listdir(directory):

    # get original JSON directory
    f = os.path.join(directory, filename)

    # checking if it is a file, run if so, else stop
    if os.path.isfile(f):

        # set asset name
        assetName = 'DOOM # ' + str(nameCount)

        temp = {
            "name": assetName,
            "dna": genDNA(32),
            "edition": 1,
            "date": 'Generated on ' + str(date.today()),
            "description": "1000 randomly generated artworks, comprised of real paint and digital objects. Created with p5.js.",
            "image": sortedImages[count]['image'],
            "attributes": [
                {
                "trait_type": "background",
                "value": "#ffe1b8"
                },
                {
                "trait_type": "color palette",
                "value": [
                    "#ffa28f",
                    "#ffcd9e",
                    "#ffe1b8",
                    "#bbff9e"
                ]
                },
                {
                "trait_type": "size",
                "value": "3000px by 3000px"
                },
                {
                "trait_type": "1/1?",
                "value": "No"
                }
            ]
            }
        #update counter
        count += 1

        # insert metadata
        metadata.append(temp)

# temp metadata filename counter
fileNameCount = 1

# for each metadata JSON, create a separate JSON file in the newFactoriaJSON directory
for data in metadata: 
    
    # get JSON for each metadata
    json_object = json.dumps(data, indent = 4)

    # set filename with its proper dir
    fileName = "./newFactoriaJSON/" + str(fileNameCount)+".json"
    
    # Writing JSON file
    with open(fileName, "w") as outfile:
        outfile.write(json_object)
        fileNameCount += 1
 
print('DONE! ⚡')
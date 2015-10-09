__author__ = 'jimmy'

from skimage import data, io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray

image = io.imread('test2.jpg')
image = rgb2gray(image)

NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

ThresholdValue = threshold_otsu(image)
print(ThresholdValue)

# simpe thresholding
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image[x,y] > ThresholdValue):
            #black / foreground
            image[x,y] = 0
        else:
            #white / background
            image[x,y] = 1


#io.imshow(image)
#io.show()

RegionInterval = 50

CurrentRegion = RegionInterval

newSection = False

ConflictList = []

def RegionValue(x):
    if (x != 0) and (x != 1):
        return x
    else:
        return 1000

def CheckNeighborPixels(x,y):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000
            upperRight = 1000
            upperLeft  = 1000
            idk1 = 1000
            idk2 = 1000

            if ((x-1) > 0):
                leftValue = RegionValue(image[x-1,y])
            if((x+1) < NumberOfColumns):
                rightValue = RegionValue(image[x+1,y])
            if ((y-1) > 0):
                belowValue = RegionValue(image[x,y-1])
            if ((y+1) < NumberOfColumns):
                aboveValue = RegionValue(image[x,y+1])

            if ((x-1)>0) and ((y-1) > 0):
                upperLeft = RegionValue(image[x-1,y-1])
            if ((x+1)<NumberOfColumns) and ((y-1) > 0):
                upperRight = RegionValue(image[x+1,y-1])
            if ((x+1)<NumberOfColumns) and ((y+1) < NumberOfColumns):
                idk1 = RegionValue(image[x+1,y+1])
            if ((x-1)>0) and ((y+1) < NumberOfColumns):
                idk1 = RegionValue(image[x-1,y+1])

            LowestNeighbor = min(leftValue,rightValue,belowValue,aboveValue,upperLeft,upperRight,idk1,idk2)


            return LowestNeighbor

#first pass
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image[x,y] == 0):

            LowestNeighbor = CheckNeighborPixels(x,y)

            if (LowestNeighbor < CurrentRegion):
                image[x,y] = LowestNeighbor
            else:
                image[x,y] = CurrentRegion
                newSection = True

        elif newSection:
            CurrentRegion += RegionInterval
            newSection = False

io.imshow(image)
io.show()
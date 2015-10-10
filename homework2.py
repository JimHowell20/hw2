__author__ = 'jimmy'

fileName = 'hw2-3A.jpg'

from skimage import data, io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def RegionValue(x):
    if (x != 0) and (x != 1):
        return int(x)
    else:
        return int(1000)

def CheckNeighborPixels(x,y):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000
            upperRight = 1000
            upperLeft  = 1000
            idk1 = 1000
            idk2 = 1000

            if ((x-1) > -1):
                leftValue = RegionValue(image[x-1,y])
            if((x+1) < NumberOfRows):
                rightValue = RegionValue(image[x+1,y])
            if ((y-1) > -1):
                belowValue = RegionValue(image[x,y-1])
            if ((y+1) < NumberOfColumns):
                aboveValue = RegionValue(image[x,y+1])

            if ((x-1) > -1) and ((y-1) > -1):
                upperLeft = RegionValue(image[x-1,y-1])
            if ((x+1) < NumberOfRows) and ((y-1) > -1):
                upperRight = RegionValue(image[x+1,y-1])
            if ((x+1) < NumberOfRows) and ((y+1) < NumberOfColumns):
                idk1 = RegionValue(image[x+1,y+1])
            if ((x-1)> -1) and ((y+1) < NumberOfColumns):
                idk1 = RegionValue(image[x-1,y+1])

            LowestNeighbor = min(leftValue,rightValue,belowValue,aboveValue,upperLeft,upperRight,idk1,idk2)

            NeighborList = [leftValue, rightValue, belowValue, aboveValue, upperRight, upperLeft, idk1, idk2]
            if (LowestNeighbor < CurrentRegion):
                image[x,y] = LowestNeighbor
                for value in NeighborList:
                    if (value != LowestNeighbor) and (value != 1000):
                        temp = testDict.get(value)
                        if (temp == None) or (LowestNeighbor < temp):
                            testDict[value] = LowestNeighbor

            return LowestNeighbor

def NeighborPixelIsEqualToValue(x,y,array,value):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000
            upperRight = 1000
            upperLeft  = 1000
            idk1 = 1000
            idk2 = 1000

            if ((x-1) > -1):
                leftValue = array[x-1,y]
            if((x+1) < NumberOfRows):
                rightValue = array[x+1,y]
            if ((y-1) > -1):
                belowValue = array[x,y-1]
            if ((y+1) < NumberOfColumns):
                aboveValue = array[x,y+1]

            if ((x-1) > -1) and ((y-1) > -1):
                upperLeft = array[x-1,y-1]
            if ((x+1) < NumberOfRows) and ((y-1) > -1):
                upperRight = array[x+1,y-1]
            if ((x+1) < NumberOfRows) and ((y+1) < NumberOfColumns):
                idk1 = array[x+1,y+1]
            if ((x-1)> -1) and ((y+1) < NumberOfColumns):
                idk1 = array[x-1,y+1]

            NeighborList = [leftValue, rightValue, belowValue, aboveValue, upperRight, upperLeft, idk1, idk2]

            for val in NeighborList:
                if val == value:
                    return True

            return False



#START of PROGRAM
image = io.imread(fileName)
image = rgb2gray(image)

NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

ThresholdValue = threshold_otsu(image)

numberOfBlackPixels = 0
numberOfWhitePixels = 0

# simpe thresholding
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image[x,y] > ThresholdValue):
            #black
            image[x,y] = 0
            numberOfBlackPixels += 1
        else:
            #white
            image[x,y] = 1
            numberOfWhitePixels += 1

#Assumption - Background has more pixels than foreground

# foreground pixels are black
ForegroundPixelValue = 0
if ( numberOfBlackPixels > numberOfWhitePixels):
    # foreground pixels are white
    ForegroundPixelValue = 1

BackgroundPixelValue = 1 - ForegroundPixelValue

image2 = image.copy()
# Do
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image[x,y] == BackgroundPixelValue):

            shouldDilate = NeighborPixelIsEqualToValue(x,y,image, ForegroundPixelValue)

            if (shouldDilate):
                image2[x,y] = ForegroundPixelValue


# io.imshow(image2)
# io.show()


image3 = image2.copy()

# Do Erosion
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image2[x,y] == ForegroundPixelValue):

            shouldDilate = NeighborPixelIsEqualToValue(x,y, image2, BackgroundPixelValue)

            if (shouldDilate):
                image3[x,y] = BackgroundPixelValue

# io.imshow(image3)
# io.show()

#initialize region tag / interval
RegionInterval = 1
CurrentRegion = 2
newSection = False

testDict = {}

#first pass
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        if (image[x,y] == ForegroundPixelValue):

            LowestNeighbor = CheckNeighborPixels(x,y)

            if (LowestNeighbor >= CurrentRegion):
                image[x,y] = CurrentRegion
                newSection = True

        elif newSection:
            CurrentRegion += RegionInterval
            newSection = False

lowestValueForRegion = {}

# Second Pass over Image
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):
        regionNumber = image[x,y]
        value = testDict.get(regionNumber)

        temp = value
        while (temp != None):
            temp = testDict.get(temp)
            if (temp != None):
                value = temp

        if (value != None):
            image[x,y] = value


SetOfRegions = set()

AreaOfRegion = {}
RowCountOfRegion = {}
ColumnCountOfRegion = {}

# Third Pass over Image to Count Number of Regions
for x in range(NumberOfRows):
    for y in range(NumberOfColumns):

        regionNumber = image[x,y]

        if (regionNumber != 0 and regionNumber != 1):

            SetOfRegions.add(int(regionNumber))
            AreaInitCheck = AreaOfRegion.get(regionNumber)
            RowInitCheck = RowCountOfRegion.get(regionNumber)
            ColumnInitCheck = ColumnCountOfRegion.get(regionNumber)

            if (AreaInitCheck == None):
                AreaOfRegion[regionNumber] = 1
            else:
                AreaOfRegion[regionNumber] += 1

            if (RowInitCheck == None):
                RowCountOfRegion[regionNumber] = x
            else:
                RowCountOfRegion[regionNumber] += x

            if (ColumnInitCheck == None):
                ColumnCountOfRegion[regionNumber] = y
            else:
                ColumnCountOfRegion[regionNumber] += y


print("Number Of Regions:", len(SetOfRegions))

index = 1
for x in SetOfRegions:
    Area = AreaOfRegion[x]
    RowCount = RowCountOfRegion[x]
    ColumnCount = ColumnCountOfRegion[x]

    rAVG = RowCount/float(Area)
    cAVG = ColumnCount/float(Area)

    ps1 = "Region " + str(index) + " Info : "
    ps2 = " Area " + str(Area)
    ps3 = " r Average " + str(rAVG)
    ps4 = " c Average " + str(cAVG)

    print(ps1)
    print(ps2)
    print(ps3)
    print(ps4)
    print("")
    index += 1


io.imshow(image, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = 8, origin='upper')
io.show()
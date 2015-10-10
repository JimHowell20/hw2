__author__ = 'jimmx'

fileName = 'hw2-2A.jpg'

from skimage import data, io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def RegionValue(y):
    if (y != 0) and (y != 1):
        return int(y)
    else:
        return int(1000)

def CheckNeighborPixels(y,x,array, storeValues):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000
            upperLeft  = 1000
            upperRight = 1000
            bottomLeft = 1000
            bottomRight = 1000

            if (x-1) > -1:
                leftValue = RegionValue(array[y,x-1])
            if (x+1) < NumberOfColumns:
                rightValue = RegionValue(array[y,x+1])
            if (y+1) < NumberOfRows:
                belowValue = RegionValue(array[y+1,x])
            if (y-1) > -1:
                aboveValue = RegionValue(array[y-1,x])

            if ((y-1) > -1) and ((x-1) > -1):
                upperLeft = RegionValue(array[y-1,x-1])
            if ((y-1)> -1) and ((x+1) < NumberOfColumns):
                upperRight = RegionValue(array[y-1,x+1])
            if ((y+1) < NumberOfRows) and ((x-1) > -1):
                bottomLeft = RegionValue(array[y+1,x-1])
            if ((y+1) < NumberOfRows) and ((x+1) < NumberOfColumns):
                bottomRight = RegionValue(array[y+1,x+1])


            LowestNeighbor = min(leftValue,rightValue,belowValue,aboveValue,upperLeft,upperRight,bottomLeft,bottomRight)

            NeighborList = [leftValue,rightValue,belowValue,aboveValue,upperLeft,upperRight,bottomLeft,bottomRight]

            if (LowestNeighbor < CurrentRegion) and storeValues == True:
                array[y,x] = LowestNeighbor
                for value in NeighborList:
                    if (value != LowestNeighbor) and (value != 1000):
                        temp = testDict.get(value)
                        if (temp == None) or (LowestNeighbor < temp):
                            testDict[value] = LowestNeighbor

            return LowestNeighbor

def CheckPerimeter(y,x,array):

    PerimeterCount = 0
    finalY = y
    finalX = x
    LoopCount = 0

    tempX = 0
    tempY = 0
    dx = 0
    dy = 0

    while True:

        dx = x - tempX
        dy = y - tempY

        tempX = x
        tempY = y

        temp = array[y,x]
        array[y,x] = 100

        io.imshow(array, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = 100, origin='upper')
        io.show()
        array[y,x] = temp
        leftValue  = 1000
        rightValue = 1000
        belowValue = 1000
        aboveValue = 1000

        upperLeft  = 1000
        upperRight = 1000
        bottomLeft = 1000
        bottomRight = 1000

        if finalY == y and finalX == x:
            LoopCount += 1

        if LoopCount >= 2 or (dx == 0 and dy == 0):
            break

        if (x-1) > -1 and dx <= 0:
            leftValue = RegionValue(array[y,x-1])
            if leftValue == PerimeterRegionID:
                PerimeterCount += 1
                x = x-1
                continue
        if (x+1) < NumberOfColumns and dx >= 0:
            rightValue = RegionValue(array[y,x+1])
            if rightValue == PerimeterRegionID:
                PerimeterCount += 1
                x = x+1
                continue
        if (y+1) < NumberOfRows and dy >= 0:
            belowValue = RegionValue(array[y+1,x])
            if belowValue == PerimeterRegionID:
                PerimeterCount += 1
                y = y+1
                continue

        if (y-1) > -1 and dy <= 0:
            aboveValue = RegionValue(array[y-1,x])
            if aboveValue == PerimeterRegionID:
                PerimeterCount += 1
                y = y-1
                continue


        if ((y-1) > -1) and ((x-1) > -1) and dx < 0 or dy < 0:
            upperLeft = RegionValue(array[y-1,x-1])
            if upperLeft == PerimeterRegionID:
                PerimeterCount += 2**0.5
                x = x-1
                y = y-1
                continue
        if ((y-1)> -1) and ((x+1) < NumberOfColumns)  and dx > 0 or dy < 0:
            upperRight = RegionValue(array[y-1,x+1])
            if upperRight == PerimeterRegionID:
                PerimeterCount += 2**0.5
                x = x+1
                y = y-1
                continue
        if ((y+1) < NumberOfRows) and ((x-1) > -1) and dx < 0 or dy > 0:
            bottomLeft = RegionValue(array[y+1,x-1])
            if bottomLeft == PerimeterRegionID:
                PerimeterCount += 2**0.5
                x = x-1
                y = y+1
                continue
        if ((y+1) < NumberOfRows) and ((x+1) < NumberOfColumns) and dx > 0 or dy > 0:
            bottomRight = RegionValue(array[y+1,x+1])
            if bottomRight == PerimeterRegionID:
                PerimeterCount += 2**0.5
                x = x+1
                y = y+1
                continue
        dx = 0
        dy = 0
    return PerimeterCount

def NeighborPixelIsEqualToValue(y,x,array,value):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000
            upperLeft  = 1000
            upperRight = 1000
            bottomLeft = 1000
            bottomRight = 1000

            if (x-1) > -1:
                leftValue = array[y,x-1]
            if (x+1) < NumberOfColumns:
                rightValue = array[y,x+1]
            if (y+1) < NumberOfRows:
                belowValue = array[y+1,x]
            if (y-1) > -1:
                aboveValue = array[y-1,x]

            if ((y-1) > -1) and ((x-1) > -1):
                upperLeft = array[y-1,x-1]
            if ((y-1)> -1) and ((x+1) < NumberOfColumns):
                upperRight = array[y-1,x+1]
            if ((y+1) < NumberOfRows) and ((x-1) > -1):
                bottomLeft = array[y+1,x-1]
            if ((y+1) < NumberOfRows) and ((x+1) < NumberOfColumns):
                bottomRight = array[y+1,x+1]

            NeighborList = [leftValue,rightValue,belowValue,aboveValue,upperLeft,upperRight,bottomLeft,bottomRight]

            count = 0
            for val in NeighborList:
                if val == value:
                    count += 1

            if count > 7:
                return True
            else:
                return False

def Check4NeighborPixels(y,x,array):

            leftValue  = 1000
            rightValue = 1000
            belowValue = 1000
            aboveValue = 1000

            if (x-1) > -1:
                leftValue = array[y,x-1]
            if (x+1) < NumberOfColumns:
                rightValue = array[y,x+1]
            if (y+1) < NumberOfRows:
                belowValue = array[y+1,x]
            if (y-1) > -1:
                aboveValue = array[y-1,x]

            LowestValue = min(leftValue,rightValue,belowValue,aboveValue)

            return LowestValue


#START of PROGRAM
image = io.imread(fileName)
image = rgb2gray(image)

NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

ThresholdValue = threshold_otsu(image)

numberOfBlackPixels = 0
numberOfWhitePixels = 0

# simpe thresholding
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):
        if image[y,x] > ThresholdValue:
            #black
            image[y,x] = 0
            numberOfBlackPixels += 1
        else:
            #white
            image[y,x] = 1
            numberOfWhitePixels += 1

#Assumption - Background has more Pixels than foreground

# foreground Pixels are black
ForegroundPixelValue = 0
if numberOfBlackPixels > numberOfWhitePixels:
    # foreground Pixels are white
    ForegroundPixelValue = 1

BackgroundPixelValue = 1 - ForegroundPixelValue

image2 = image.copy()

#  Erosion - foreground checks Neighboring background pixels, and turns into background if necessary
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):
        if image[y,x] == ForegroundPixelValue:

            shouldDilate = NeighborPixelIsEqualToValue(y,x, image, BackgroundPixelValue)

            if shouldDilate:
                image2[y,x] = BackgroundPixelValue

# io.imshow(image2)
# io.show()
#

image3 = image2.copy()
# Dilation - background checks Neighboring foreground pixels, and turns into foreground if necessary
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):
        if image2[y,x] == BackgroundPixelValue:

            shouldDilate = NeighborPixelIsEqualToValue(y,x,image2, ForegroundPixelValue)

            if shouldDilate:
                image3[y,x] = ForegroundPixelValue


# io.imshow(image3)
# io.show()

image = image3

#initialize region tag / interval
RegionInterval = 1
CurrentRegion = 2
newSection = False

testDict = {}

#first pass
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):
        if image[y,x] == ForegroundPixelValue:

            LowestNeighbor = CheckNeighborPixels(y,x,image, True)

            if LowestNeighbor >= CurrentRegion:
                image[y,x] = CurrentRegion
                newSection = True

        elif newSection:
            CurrentRegion += RegionInterval
            newSection = False

lowestValueForRegion = {}

# Second Pass over Image
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):
        regionNumber = image[y,x]
        value = testDict.get(regionNumber)

        temp = value
        while temp != None:
            temp = testDict.get(temp)
            if temp != None:
                value = temp

        if value != None:
            image[y,x] = value


SetOfRegions = set()

PerimeterRegionID = 50
AreaOfRegion = {}
RowCountOfRegion = {}
ColumnCountOfRegion = {}

PerimeterImage = image.copy()

# Third Pass over Image to Count Number of Regions
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionNumber = image[y,x]

        if regionNumber != 0 and regionNumber != 1:

            lowestNeighbor = Check4NeighborPixels(y,x,image)

            if lowestNeighbor == BackgroundPixelValue:
                PerimeterImage[y,x] = PerimeterRegionID
            else:
                PerimeterImage[y,x] = regionNumber

            SetOfRegions.add(int(regionNumber))
            AreaInitCheck = AreaOfRegion.get(regionNumber)
            RowInitCheck = RowCountOfRegion.get(regionNumber)
            ColumnInitCheck = ColumnCountOfRegion.get(regionNumber)

            if AreaInitCheck == None:
                AreaOfRegion[regionNumber] = 1
            else:
                AreaOfRegion[regionNumber] += 1

            if RowInitCheck == None:
                RowCountOfRegion[regionNumber] = y
            else:
                RowCountOfRegion[regionNumber] += y

            if ColumnInitCheck == None:
                ColumnCountOfRegion[regionNumber] = x
            else:
                ColumnCountOfRegion[regionNumber] += x

rrOfRegion = {}
rcOfRegion = {}
ccOfRegion = {}

# Fourth Pass for more stats
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionNumber = image[y,x]
        row = y
        column = x

        if regionNumber != 0 and regionNumber != 1:

            Area = AreaOfRegion[regionNumber]
            RowCount = RowCountOfRegion[regionNumber]
            ColumnCount = ColumnCountOfRegion[regionNumber]

            rAVG = RowCount/float(Area)
            cAVG = ColumnCount/float(Area)

            rrInitCheck = rrOfRegion.get(regionNumber)

            if rrInitCheck == None:
                rrOfRegion[regionNumber] = (row - rAVG)**2
            else:
                rrOfRegion[regionNumber] += (row - rAVG)**2

            rcInitCheck = rcOfRegion.get(regionNumber)

            if rcInitCheck == None:
                rcOfRegion[regionNumber] = (row - rAVG)*(column - cAVG)
            else:
                rcOfRegion[regionNumber] += (row - rAVG)*(column - cAVG)

            ccInitCheck = ccOfRegion.get(regionNumber)

            if ccInitCheck == None:
                ccOfRegion[regionNumber] = (column - cAVG)**2
            else:
                ccOfRegion[regionNumber] += (column - cAVG)**2


# Fifth Pass - Walk Along Perimeter

PerimeterOfRegion = {}

for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionPerimeterNumber = PerimeterImage[y,x]

        if regionPerimeterNumber == PerimeterRegionID:

            #Check original image to see what region it is
            InnerRegionValue = CheckNeighborPixels(y,x, image, False)

            pInitCheck = PerimeterOfRegion.get(InnerRegionValue)

            if pInitCheck == None and InnerRegionValue != PerimeterRegionID:

                Circumference = CheckPerimeter(y,x,PerimeterImage)

                PerimeterOfRegion[InnerRegionValue] = Circumference

                ps = "Circumference for region " + str(InnerRegionValue) + " " + str(Circumference)
                print(ps)


print("Number Of Regions:", len(SetOfRegions))

index = 1
for region in SetOfRegions:
    Area = AreaOfRegion[region]
    RowCount = RowCountOfRegion[region]
    ColumnCount = ColumnCountOfRegion[region]
    Mrr = rrOfRegion[region]/float(Area)
    Mrc = rcOfRegion[region]/float(Area)
    Mcc = ccOfRegion[region]/float(Area)

    rAVG = RowCount/float(Area)
    cAVG = ColumnCount/float(Area)

    ps1 = "Region " + str(index) + " Info : "
    ps2 = " Area " + str(Area)
    ps3 = " r Average " + str(rAVG)
    ps4 = " c Average " + str(cAVG)
    ps5 = " Mrr " + str(Mrr)
    ps6 = " Mrc " + str(Mrc)
    ps7 = " Mcc " + str(Mcc)

    print(ps1)
    print(ps2)
    print(ps3)
    print(ps4)
    print(ps5)
    print(ps6)
    print(ps7)
    print("")
    index += 1


# io.imshow(image, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = 8, origin='upper')
# io.show()

io.imshow(PerimeterImage, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = PerimeterRegionID, origin='upper')
io.show()
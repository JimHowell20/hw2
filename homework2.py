#Jim Howell
#A37491496
#CSE 803
#HW #2

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

def UpdateDictKeyValue(dictionary,key,value):
    valueCheck = dictionary.get(key)

    if valueCheck == None:
        dictionary[key] = value
    else:
        dictionary[key] += value


def RoundFloat(x):
    return  round(x,1)

def DistanceBetweenTwoPoints(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

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

def CheckPerimeter(y,x,array, regionValue):

    PerimeterCount = 0

    LoopCount = 0

    tempX = x
    tempY = y
    finalY = 2000
    finalX = 2000
    LastIncrement = 0
    dx = 0
    dy = 0

    while True:

        dx = x - tempX
        dy = y - tempY

        tempX = x
        tempY = y

        if LoopCount != 0:
            #Circle
            if (tempX == finalX) and (tempY == finalY):
                PerimeterCount -= LastIncrement #Counted Twice
                break
            #Line
            if (dx == 0) and (dy == 0):
                break

        if (LoopCount == 1):
            finalY = y
            finalX = x

        LoopCount += 1

        # if(regionValue == 4):
        #     temp = array[y,x]
        #     array[y,x] = 100
        #
        #     print("Perimeter Count", PerimeterCount)
        #
        #     io.imshow(array, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = 100, origin='upper')
        #     io.show()
        #     array[y,x] = temp


        leftValue  = 1000
        rightValue = 1000
        belowValue = 1000
        aboveValue = 1000

        upperLeft  = 1000
        upperRight = 1000
        bottomLeft = 1000
        bottomRight = 1000

        if ((y-1) > -1) and ((x-1) > -1) and dx <= 0 or dy <= 0:
            upperLeft = RegionValue(array[y-1,x-1])
            if upperLeft == PerimeterRegionID:
                PerimeterCount += 2**0.5
                LastIncrement = 2**0.5
                x = x-1
                y = y-1
                continue
        if ((y-1)> -1) and ((x+1) < NumberOfColumns)  and dx >= 0 or dy <= 0:
            upperRight = RegionValue(array[y-1,x+1])
            if upperRight == PerimeterRegionID:
                PerimeterCount += 2**0.5
                LastIncrement = 2**0.5
                x = x+1
                y = y-1
                continue
        if ((y+1) < NumberOfRows) and ((x-1) > -1) and dx <= 0 or dy >= 0:
            bottomLeft = RegionValue(array[y+1,x-1])
            if bottomLeft == PerimeterRegionID:
                PerimeterCount += 2**0.5
                LastIncrement = 2**0.5
                x = x-1
                y = y+1
                continue
        if ((y+1) < NumberOfRows) and ((x+1) < NumberOfColumns) and dx >= 0 or dy >= 0:
            bottomRight = RegionValue(array[y+1,x+1])
            if bottomRight == PerimeterRegionID:
                PerimeterCount += 2**0.5
                LastIncrement = 2**0.5
                x = x+1
                y = y+1
                continue

        if (x-1) > -1 and dx <= 0:
            leftValue = RegionValue(array[y,x-1])
            if leftValue == PerimeterRegionID:
                PerimeterCount += 1
                LastIncrement = 1
                x = x-1
                continue
        if (x+1) < NumberOfColumns and dx >= 0:
            rightValue = RegionValue(array[y,x+1])
            if rightValue == PerimeterRegionID:
                PerimeterCount += 1
                LastIncrement = 1
                x = x+1
                continue
        if (y+1) < NumberOfRows and dy >= 0:
            belowValue = RegionValue(array[y+1,x])
            if belowValue == PerimeterRegionID:
                PerimeterCount += 1
                LastIncrement = 1
                y = y+1
                continue

        if (y-1) > -1 and dy <= 0:
            aboveValue = RegionValue(array[y-1,x])
            if aboveValue == PerimeterRegionID:
                PerimeterCount += 1
                LastIncrement = 1
                y = y-1
                continue



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

            UpdateDictKeyValue(AreaOfRegion,regionNumber,1)
            UpdateDictKeyValue(RowCountOfRegion,regionNumber,y)
            UpdateDictKeyValue(ColumnCountOfRegion,regionNumber,x)


rrOfRegion = {}
rcOfRegion = {}
ccOfRegion = {}
mrdOfRegion = {}
PerimeterPixelCountOfRegion = {}

# Fourth Pass for more stats
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionNumber = image[y,x]
        regionPixelNumber = PerimeterImage[y,x]
        row = y
        column = x

        if regionNumber != 0 and regionNumber != 1:

            Area = AreaOfRegion[regionNumber]
            RowCount = RowCountOfRegion[regionNumber]
            ColumnCount = ColumnCountOfRegion[regionNumber]

            rAVG = RowCount/float(Area)
            cAVG = ColumnCount/float(Area)

            if regionPixelNumber == PerimeterRegionID:

                distance = DistanceBetweenTwoPoints(y,x,rAVG,cAVG)

                UpdateDictKeyValue(mrdOfRegion,regionNumber,distance)
                UpdateDictKeyValue(PerimeterPixelCountOfRegion,regionNumber,1)


            UpdateDictKeyValue(rrOfRegion,regionNumber,(row - rAVG)**2)
            UpdateDictKeyValue(rcOfRegion,regionNumber,(row - rAVG)*(column - cAVG))
            UpdateDictKeyValue(ccOfRegion,regionNumber,(column - cAVG)**2)


# Fifth Pass - Walk Along Perimeter

PerimeterOfRegion = {}

index = 0
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionPerimeterNumber = PerimeterImage[y,x]

        if regionPerimeterNumber == PerimeterRegionID:

            #Check original image to see what region it is
            InnerRegionValue = CheckNeighborPixels(y,x, image, False)

            pInitCheck = PerimeterOfRegion.get(InnerRegionValue)

            if pInitCheck == None and InnerRegionValue != PerimeterRegionID:

                index += 1

                Circumference = CheckPerimeter(y,x,PerimeterImage,index)

                PerimeterOfRegion[InnerRegionValue] = Circumference

STDofRDRegionValue = {}

# STD of radial distance
for y in range(NumberOfRows):
    for x in range(NumberOfColumns):

        regionNumber = image[y,x]
        regionPixelNumber = PerimeterImage[y,x]
        row = y
        column = x

        if regionNumber != 0 and regionNumber != 1:

            Area = AreaOfRegion[regionNumber]
            RowCount = RowCountOfRegion[regionNumber]
            ColumnCount = ColumnCountOfRegion[regionNumber]

            rAVG = RowCount/float(Area)
            cAVG = ColumnCount/float(Area)

            if regionPixelNumber == PerimeterRegionID:

                PerimeterPixelCount = PerimeterPixelCountOfRegion[regionNumber]

                MRD = mrdOfRegion[regionNumber]/float(PerimeterPixelCount)

                distance = DistanceBetweenTwoPoints(y,x,rAVG,cAVG)

                UpdateDictKeyValue(STDofRDRegionValue,regionNumber,(distance-MRD)**2)


print("Number Of Regions:", len(SetOfRegions))


index = 1
for region in SetOfRegions:
    Area = AreaOfRegion[region]
    RowCount = RowCountOfRegion[region]
    ColumnCount = ColumnCountOfRegion[region]
    PerimeterCount = PerimeterOfRegion[region]
    PerimeterPixelCount = PerimeterPixelCountOfRegion[region]
    PartialSTDofRad = STDofRDRegionValue[region]

    Mrr = rrOfRegion[region]/float(Area)
    Mrc = rcOfRegion[region]/float(Area)
    Mcc = ccOfRegion[region]/float(Area)
    MRD = mrdOfRegion[region]/float(PerimeterPixelCount)
    STDofRad = (PartialSTDofRad/float(PerimeterPixelCount))**0.5

    IMax = ((Mrr+Mcc)/2.0) + (((Mrr-Mcc)/2.0)**2+Mrc**2)**0.5
    IMin = ((Mrr+Mcc)/2.0) - (((Mrr-Mcc)/2.0)**2+Mrc**2)**0.5

    Circularity = MRD/STDofRad

    rAVG = RowCount/float(Area)
    cAVG = ColumnCount/float(Area)

    ps1 = "Region " + str(index) + " Info : "
    ps2 = " Area " + str(RoundFloat(Area))
    ps3 = " r Average " + str(RoundFloat(rAVG))
    ps4 = " c Average " + str(RoundFloat(cAVG))
    ps5 = " Mrr " + str(RoundFloat(Mrr))
    ps6 = " Mrc " + str(RoundFloat(Mrc))
    ps7 = " Mcc " + str(RoundFloat(Mcc))
    ps8 = " Perimeter " + str(RoundFloat(PerimeterCount))
    ps9 = " MRD " + str(RoundFloat(MRD))
    ps10 = " STD of Radial Dist " + str(RoundFloat(STDofRad))
    ps11 = " Circularity " + str(RoundFloat(Circularity))
    ps12 = " Max Moment of Inertia " + str(RoundFloat(IMax))
    ps13 = " Min Moment of Inertia " + str(RoundFloat(IMin))

    print(ps1)
    print(ps2)
    print(ps3)
    print(ps4)
    print(ps5)
    print(ps6)
    print(ps7)
    print(ps8)
    print(ps9)
    print(ps10)
    print(ps11)
    print(ps12)
    print(ps13)
    print("")
    index += 1


# io.imshow(image, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = 8, origin='upper')
# io.show()

io.imshow(PerimeterImage, cmap=plt.cm.cubehelix, interpolation='none', vmin = 0, vmax = PerimeterRegionID, origin='upper')
io.show()
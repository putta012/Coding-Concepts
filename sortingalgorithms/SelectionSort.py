def selectionSort(elementsList:list,asc=True):
    length=len(elementsList)
    if asc==True:
        for i in range(length):
            smallestAt=i
            for j in range(i+1,length):
                if elementsList[j]<elementsList[smallestAt]:
                    smallestAt=j
            (elementsList[i],elementsList[smallestAt])=(elementsList[smallestAt],elementsList[i])
    else:
        for i in range(length):
            largestAt=i
            for j in range(i+1,length):
                if elementsList[j]>elementsList[largestAt]:
                    largestAt=j
            (elementsList[i],elementsList[largestAt])=(elementsList[largestAt],elementsList[i])
    return elementsList

if __name__ == '__main__':
    elements=[34,36,1,4,67,674,79,342,3456,786,25,23,76,42]
    print(elements)
    sorted=selectionSort(elements,False)
    print(elements)
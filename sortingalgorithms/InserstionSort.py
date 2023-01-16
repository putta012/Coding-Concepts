def insertionSort(elementsList:list,asc=True):
    length=len(elementsList)
    if asc==True:
        for i in range(length):
            holeAt=i
            for j in range(i-1,-1,-1):
                if elementsList[j]>elementsList[holeAt]:
                    (elementsList[j],elementsList[holeAt])=(elementsList[holeAt],elementsList[j])
                    holeAt=j
                else:
                    break
    else:
        for i in range(length):
            holeAt=i
            for j in range(i-1,-1,-1):
                if elementsList[j]<elementsList[holeAt]:
                    (elementsList[j],elementsList[holeAt])=(elementsList[holeAt],elementsList[j])
                    holeAt=j
                else:
                    break
    return elementsList

if __name__ == '__main__':
    elements=[34,36,1,4,67,674,79,342,3456,786,25,23,76,42]
    print(elements)
    sorted=insertionSort(elements,False)
    print(elements)
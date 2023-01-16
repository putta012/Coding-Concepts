def bubbleSort(elementsList:list,asc=True):
    length=len(elementsList)
    if asc==True:
        for i in range(length-1):
            for j in range(length-i-1):
                if elementsList[j]>elementsList[j+1]:
                    (elementsList[j],elementsList[j+1])=(elementsList[j+1],elementsList[j])
    else:
        for i in range(length-1):
            for j in range(length-i-1):
                if elementsList[j]<elementsList[j+1]:
                    (elementsList[j],elementsList[j+1])=(elementsList[j+1],elementsList[j])
    return elementsList

if __name__ == '__main__':
    elements=[34,36,1,4,67,674,79,342,3456,786,25,4,76,42]
    print(elements)
    sorted=bubbleSort(elements,False)
    print(elements)
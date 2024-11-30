
def sortElement(EleL, EleR,arr):

    #SortedArray=[]
    MaxIndexL=len(EleL)
    MaxIndexR = len(EleR)
    I=J=K=0

    while I < MaxIndexL and J < MaxIndexR:
          if EleL[I]>EleR[J]:
              arr[K]=EleR[J]
              J+=1
          else:
              arr[K] = EleL[I]
              I += 1

          K+=1

    while I < MaxIndexL:
        arr[K] = EleL[I]
        I+=1
        K+=1

    while J <MaxIndexR:
        arr[K]=EleR[J]
        J+=1
        K+=1


    return arr




def Merge_Sort(Element):

    if len(Element)<=1:
        return Element

    midpoint=len(Element)//2
    left=Element[:midpoint]
    right=Element[midpoint:]

    left_return=Merge_Sort(left)
    right_return=Merge_Sort(right)

    return sortElement(left_return,right_return,Element)




if __name__ == '__main__':

    # ElementA=[1,3,4,10]
    # ElementB=[2,6,8]
    # Temp=[1,2,3,4,5,6,6]
    # Element=[1,7,2,8,3,5]
    # X=Merge_Sort(Element)
    # X=sortElement(ElementA,ElementB,Temp)
    # print(X)

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],

    ]

    for arr in test_cases:
        Merge_Sort(arr)

    for element in test_cases:
        print(element)


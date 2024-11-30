

def LinearSearch(NumList,TargetNum):

    for index,item in enumerate(NumList):
        
        if item ==TargetNum:
            return index
            break
    
    else:
        return -1

    


def BinarySearch(NumList,TargetNum):

    LeftIndex=0
    RightIndex=len(NumList)-1
    MidValue=0


    while (LeftIndex<=RightIndex):

        MidValue = (LeftIndex + RightIndex) // 2

        if(NumList[MidValue]==TargetNum):
            return  MidValue

        if (NumList[MidValue]<TargetNum):
            LeftIndex=MidValue+1

        elif (NumList[MidValue]>TargetNum):
            RightIndex=MidValue-1

    return -1



def recursion(NumList,TargetNum,LeftIndex,RightIndex):

        if RightIndex <  LeftIndex:
            return -1

        MidValue = (LeftIndex + RightIndex) // 2

        if (NumList[MidValue] == TargetNum):
            return MidValue

        if (NumList[MidValue] < TargetNum):
            LeftIndex = MidValue + 1

        elif (NumList[MidValue] > TargetNum):
            RightIndex = MidValue - 1

        return recursion(NumList,TargetNum,LeftIndex,RightIndex)







if __name__=='__main__':

    ListA=[10,14,15,17,23,25,55,58,76,78,79,100]

    #A=LinearSearch(ListA,13)
    #A = BinarySearch(ListA,55)
    A=recursion(ListA,78,0,len(ListA)-1)
    print(A)
    
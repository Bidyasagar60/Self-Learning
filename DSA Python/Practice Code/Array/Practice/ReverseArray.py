def ReverseArrayInbuilt(Elements):

    print (Elements[::-1])

def ReverseArray(Elements):

    I=0
    J=len(Elements)-1

    while (I<len(Elements) and I<=J):

        if I<=J:
            Temp=Elements[I]
            Elements[I]=Elements[J]
            Elements[J]=Temp

        I+=1
        J-=1

    print(Elements)


def ReverseArrayRec(Elements,A,B):

        if A>=B:
            return

        Elements[A],Elements[B]=Elements[B],Elements[A]

        ReverseArrayRec(Elements,A+1,B-1)





if __name__=='__main__':

    Elements=[1,4,6,8,2,6]

    TestCases=[
        [1, 4, 6, 8, 2, 6],
        [1],
        [1,2],
        [1,2,3,5,6],
        []
    ]

    #ReverseArrayRec(Elements,0,len(Elements)-1)

    for ele in TestCases:

         #ReverseArrayInbuilt(ele)
         #ReverseArray(ele)
         ReverseArrayRec(ele,0,len(ele)-1)
         print(ele)
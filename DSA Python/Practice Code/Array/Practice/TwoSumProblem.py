def checkSumBasic(Element, Target):


    for i in range (len(Element)):
        for j in range(i+1,len(Element)):
                if Element[i]+Element[j]==Target:
                    return True
                    break

    else:
        return False

def checkSumSorted(Element,Target):

    left=0
    right=len(Element)-1

    while left < right :

        Sum=Element[left]+Element[right]

        if Sum==Target:
            return True
        elif Sum>Target:
             right-=1
        else:
            left+=1

    return False


def sort_two_array(left, right, element):

    left_len=len(left)
    right_len=len(right)

    I=J=K=0

    while I<left_len and J < right_len :

        if left[I]>right[J]:
            element[K]=right[J]
            J+=1
        else:
            element[K]=left[I]
            I+=1

        K+=1

    while I<left_len:
        element[K]=left[I]
        I+=1
        K+=1

    while J<right_len:
        element[K]=right[J]
        J+=1
        K+=1

    return element




def merge_sort(element):

    if len(element)<=1:
        return element

    mid=len(element)//2
    left=element[:mid]
    right=element[mid:]

    sortedL=merge_sort(left)
    sortedR=merge_sort(right)

    return sort_two_array(left,right,element)




if __name__=='__main__':

    Element=[1,2,9,3,5,4,6]

    Target=8

    #print(checkSumBasic(Element,Target))

    merge_sort(Element)
    #print(Element)
    print(checkSumSorted(Element, Target))
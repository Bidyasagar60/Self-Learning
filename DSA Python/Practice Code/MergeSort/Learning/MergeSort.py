def merge_two_sorted_list(a,b):


    SortedList=[]
    len_a=len(a)
    len_b=len(b)

    i=j=0

    while i < len_a and j < len_b:

        if a[i] <= b[j]:
            SortedList.append(a[i])
            i+=1
        else:
            SortedList.append(b[j])
            j+=1

    while i < len_a:
        SortedList.append(a[i])
        i+=1

    while j < len_b:
        SortedList.append(b[j])
        j+=1

    return  SortedList


def merge_sort(arr):

    if len(arr) <=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right = arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return  merge_two_sorted_list(left,right)


if __name__ == '__main__':

    # ListA=[5,8,12,56]
    # ListB=[7,9,45,51]

    # ListA=[3,5]
    # ListB=[88]

    arr=[10,3,15,7,8,23,98,29]

    print(merge_sort(arr))

    #print(merge_two_sorted_list(ListA,ListB))
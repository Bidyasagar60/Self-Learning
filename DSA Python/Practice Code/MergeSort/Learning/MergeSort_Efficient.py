def merge_two_sorted_list(a,b,arr):
    len_a=len(a)
    len_b=len(b)

    i= j = k = 0

    while i < len_a and j < len_b:

        if a[i] <= b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1

        k+=1

    while i < len_a:
        arr[k]=a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1



def merge_sort(arr):

    if len(arr) <=1:
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return  merge_two_sorted_list(left,right,arr)


if __name__ == '__main__':

    # ListA=[5,8,12,56]
    # ListB=[7,9,45,51]

    # ListA=[3,5]
    # ListB=[88]

    arr=[10,3,15,7,8,23,98,29]

    test_cases=[
                [10,3,15,7,8,23,98,29],
                [],
                [3],
                [9,8, 7,2],
                [1,2,3,4,5],

    ]

    for arr in test_cases:
        merge_sort(arr)

    for element in test_cases:
        print(element)
        # print(arr)
    # merge_sort(arr)
    # print(arr)

    #print(merge_two_sorted_list(ListA,ListB))
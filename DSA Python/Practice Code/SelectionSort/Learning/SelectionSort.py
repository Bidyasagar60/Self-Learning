def selection_sort(arr):

     length=len(arr)-1
     for index in range(length):

         anchor=arr[index]

         j=index+1
         min_index=index
         while (j<=length):

             if arr[min_index]>arr[j]  :
                 min_index=j

             j+=1

         if index != min_index:
             min_num=arr[min_index]
             arr.pop(min_index)
             arr.insert(index,min_num)
             #arr[index]=min_num






if __name__ == '__main__':


    # elements=[21,38,29,17,4,25,11,32,9]
    # selection_sort(elements)
    # print(elements)
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
    ]

    for arr in test_cases:
        selection_sort(arr)

    for element in test_cases:
        print(element)
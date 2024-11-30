def shell_sort(arr):

    size=len(arr)
    gap = size//2

    while gap>0:
        for i in range(gap,size):

            anchor=arr[i]
            j=i

            while j>=gap and arr[j-gap]>anchor:
                arr[j]=arr[j-gap]
                j-=gap

            arr[j]=anchor

        gap=gap//2


if __name__ == '__main__':


    # elements=[21,38,29,17,4,25,11,32,9]
    # shell_sort(elements)
    # print(elements)
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],

    ]

    for arr in test_cases:
        shell_sort(arr)

    for element in test_cases:
        print(element)
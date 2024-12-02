



def reverseArray(arr, m):
    left=m+1
    right=len(arr)-1

    while (left < right):

        arr[left],arr[right]=arr[right],arr[left]

        left+=1
        right-=1
    
    return arr


if __name__ == '__main__':
    

    arr=[1,2,3,4,5,6]
    m=3
    result=reverseArray(arr,m)
    print(result)
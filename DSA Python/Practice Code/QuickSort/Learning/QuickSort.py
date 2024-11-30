def swap(a,b,arr):

    #arr[a],a[b]=arr[b],arr[a]

    if a!=b:

        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp




def partition(unsortedlist,start,end):

    pivotindex=start
    pivotElement=unsortedlist[pivotindex]

    startPointer=start
    endPointer=end

    while startPointer< endPointer:

        while startPointer <  len(unsortedlist) and (unsortedlist[startPointer] <= pivotElement):

            startPointer += 1

        while (unsortedlist[endPointer] > pivotElement):
            endPointer -= 1

        if startPointer < endPointer :
            swap(startPointer,endPointer,unsortedlist)

    swap(pivotindex,endPointer,unsortedlist)

    return  endPointer




def quicksort(unsortedlist,start,end):

    if start < end:
        pi=partition(unsortedlist,start,end)
        quicksort(unsortedlist,start,pi-1)
        quicksort(unsortedlist, pi+1, end)







if __name__=='__main__':

    elements=[11,9,29,7,2,15,28]

    quicksort(elements,0,len(elements)-1)

    print(elements)

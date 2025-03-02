class Practice:

    def Array_Rotation_inbuilt(self,arr):

        print(arr[::-1])

    def Array_Rotation(self,arr):

        l=0
        r=len(arr)-1

        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        
        print(arr)


class Zax:

    if __name__ == '__main__':

        arr=[1,2,3,4,5]
        obj=Practice()
        obj.Array_Rotation_inbuilt(arr)
        obj.Array_Rotation(arr)
class Practcie:

    def Find_Largest_inbuilt(self,arr):

        print(f'Largest Element in the array:{max(arr)}')

    def Find_Largest(self,arr):
        arr.sort()
        print(f'Largest Element in the array:{arr[len(arr)-1]}')



class Zax:

    if __name__ == '__main__':
        
        LS=[1,2,5,83,2,3,5]
        obj=Practcie()
        obj.Find_Largest_inbuilt(LS)
        obj.Find_Largest(LS)
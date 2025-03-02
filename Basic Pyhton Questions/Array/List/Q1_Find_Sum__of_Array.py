class Practice:

    def sum_array_inbult(self,arr):

        print(sum(arr))

    def sum_array(self,arr):

        total=0

        [total:=total+ x for x in arr]

        print(total)



class Zax:

    if __name__ == '__main__':
        
        Lax=[1,4,5,6,2]
        obj=Practice()
        obj.sum_array_inbult(Lax)
        obj.sum_array(Lax)
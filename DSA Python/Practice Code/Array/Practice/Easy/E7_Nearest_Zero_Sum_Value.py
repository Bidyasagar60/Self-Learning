class Practice:


    def nearest_zero(self,lst):
        lst.sort()
        left=0
        right=len(lst)-1
        result=(None,None)
        nearest_sum=float('inf')

        while(left<right):
            
            s=lst[left]+lst[right]

            if abs(s)<abs(nearest_sum):
                nearest_sum=s
                result=(lst[left],lst[right])
                
            if s < 0:
                left+=1
            else:
                right-=1

        print(result)



class Zax:


    if __name__ == '__main__':

        obj=Practice()
        ListA=[0,5,-11,8,-15,-6,4,10,2,-5]
        obj.nearest_zero(ListA)
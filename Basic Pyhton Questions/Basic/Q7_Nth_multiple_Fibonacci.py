class Practice:

    def Nth_multiple_fibo(self,n,k):

        counter=1
        index=1
        a1=0
        a2=1
        while counter <= n:
            temp=a1+a2
            a1=a2
            a2=temp
            index+=1
            if(temp%k == 0):
                counter+=1
        
        print(index,a2)




class Zax:

    if __name__ == '__main__':
         
         
        obj=Practice()
        obj.Nth_multiple_fibo(5,4)
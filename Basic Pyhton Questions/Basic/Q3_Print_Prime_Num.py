
from math import sqrt

class Practice:

    def prime_print(self,start,end):

        PrimeList=[]
        for num in range(start,end+1):           
            Flag=True
            #for i in range(2,int(num**0.5)+1):
            for i in range(2,int(sqrt(num))+1):

                if num%i ==0:
                    Flag=False
                    break

            if Flag:
                PrimeList.append(num)

        return PrimeList

    
class Zex:

    if __name__ == '__main__':
        obj=Practice()
        print(obj.prime_print(43,75))
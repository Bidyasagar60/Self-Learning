
from math import sqrt

class Practice:

    def prime_check(self,num):

        Flag=True

        #for i in range(2,int(num**0.5)+1):
        for i in range(2,int(sqrt(num))+1):

            if num%i ==0:
                Flag=False

        if Flag:
            print('Prime Number')
        else:
            print('Not a PrimeNumber')

    
class Zex:

    if __name__ == '__main__':
        obj=Practice()
        obj.prime_check(36)
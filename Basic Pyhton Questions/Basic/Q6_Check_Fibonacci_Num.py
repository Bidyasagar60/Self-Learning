from math import sqrt

class Practice:


    def is_perfect_square(self,n):

        if sqrt(n)* sqrt(n) == n:
            return True
        else:
            False


    def check_fibo(self,num):

        return self.is_perfect_square(5*num*num+4) or self.is_perfect_square(5*num*num+4)


class Zax:

    if __name__ == '__main__':

        obj=Practice()
        if obj.check_fibo(8):
            print('Is Fibo')
        else:
            print('Not a Fibo')


      
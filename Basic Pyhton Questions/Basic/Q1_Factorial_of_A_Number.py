class Practice:

    def factorial(num):

        fac_num=1
        while (num>0):
            fac_num=fac_num*num
            num-=1
        return fac_num


class Zex:

    if __name__ == '__main__':
        obj=Practice
        print(obj.factorial(10))


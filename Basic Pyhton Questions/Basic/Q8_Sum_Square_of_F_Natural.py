class Practice:


    def fss_nth_natural_sqr(self,num):

        target=0

        for i in range (1,num+1):
            target+=i*i
        
        print(target)



class Zax:


    if __name__ == '__main__':

        obj=Practice()
        obj.fss_nth_natural_sqr(5)
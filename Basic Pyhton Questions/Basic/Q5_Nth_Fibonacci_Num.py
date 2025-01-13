class Practice:


    def simple_nth_fibonacci(self,num):

        if num == 0:
            return 0
        if num == 1:
            return 1

        counter=2
        snd=1
        fst=0

        for counter in range(2,num+1):
            temp=fst+snd
            fst=snd
            snd=temp

            
        return snd
        
class Zax:

    if __name__ == '__main__':
        
        obj=Practice()
        print(obj.simple_nth_fibonacci(2))
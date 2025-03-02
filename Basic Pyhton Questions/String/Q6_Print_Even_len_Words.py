class Practice:

    def Even_Words(self,parg):

        for ele in parg.split():
            
            if len(ele)%2 == 0:
                print(ele)


        print([x for x in parg.split() if len(x)%2 == 0])
                
        




class Zax:

    if __name__ == '__main__':

        pa='This is a python language'

        obj=Practice()
        obj.Even_Words(pa)
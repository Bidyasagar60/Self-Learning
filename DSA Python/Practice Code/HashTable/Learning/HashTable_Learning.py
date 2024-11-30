class HashTable:

    def __init__(self):
        self.MAX=10
        self.arr=[None]*self.MAX


    def getHash(self,key):
        sum=0
        for element in key:
            sum+=ord(element)

        return sum%self.MAX

    def __setitem__(self,key,val):
        index=self.getHash(key)
        self.arr[index]=val

    def __getitem__(self,key):
        
        index=self.getHash(key)
        return self.arr[index]

    def __delitem__(self,key):
        index=self.getHash(key)
        self.arr[index]=None





if __name__=='__main__':
    H=HashTable()

    H['March 6']=340
    H['March 8']=445
    H['March 10']=225
    H['March 17']=800
    H['March 19']=45
    #print(H.arr)
    #del H['August-2024']
    print(H['March 17'])

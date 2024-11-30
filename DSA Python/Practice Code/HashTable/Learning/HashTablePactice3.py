class HashTable:

    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]


    def getHash(self,Key):
        Sum=0
        for element in Key:
            Sum+=ord(element)

        return Sum%self.MAX

    def __getitem__(self,Key):
        Index=self.getHash('Key')

        for element in self.arr[Index]:
            if element[0]==Key:
                print(element[1])

    def __setitem__(self,Key,Val):
        Index=self.getHash('Key')
        Found=False

        for id,element in enumerate(self.arr[Index]):
            if len(element)==2 and element[0]==Key:
                self.arr[Index][id]=(Key,Val)
                Found=True
            
        if not Found:
            self.arr[Index].append((Key,Value))




if __name__=='__main__':
    Word_Count=HashTable()
    with open('poem.txt',mode='r') as file:
        for line in file:
            tokens=line.split(' ')
            for token in tokens:
                token=token.replace('\n','')
                if token in Word_Count:
                    Word_Count[token]+=1
                else:
                    Word_Count[token]=1

print(Word_Count)

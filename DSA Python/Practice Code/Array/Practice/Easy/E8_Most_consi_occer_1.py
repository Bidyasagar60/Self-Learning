class Practice:

    def most_one_occur(self,lst):

        maxOccurance=0

        currentcounter=0
        for ele in lst:
            
            if ele==1:
                currentcounter+=1
            else:
                maxOccurance=max(maxOccurance,currentcounter)
                currentcounter=0
        
        return max(maxOccurance,currentcounter)








if __name__ == '__main__':
    obj=Practice()
    lst=[1,2,3,4,1,1,4,2,7,1,1,1,1]
    print(obj.most_one_occur(lst))

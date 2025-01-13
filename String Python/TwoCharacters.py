class TwoString:

    def givelength(self,C1,C2,text):
        
        maxcount=0

        lasttext=''

        for char in text:
            if char==C1 or char==C2:
                if char != lasttext:
                    maxcount+=1
                    if char==C1:
                        lasttext=C1
                    else:
                        lasttext=C2
                else:
                    return 0

        return maxcount




    def maximumTwoCharacter(self,str):
        
        unique=list(set(str))
        maxlength=0

        for i in range(0,len(unique)-1):
            for j in range(i+1,len(unique)):
                
                if unique[i]<unique[j]:
                    cmax=self.givelength(unique[i],unique[j],str)
                else:
                    cmax=self.givelength(unique[j],unique[i],str)

                if cmax>maxlength:
                    maxlength=cmax

        return maxlength









class Main:

    if __name__=='__main__':
        
        ST='beabeefeab'
        obj=TwoString()
        print(obj.maximumTwoCharacter(ST))

class Practice:

    def IsArmstrong(self,num):

        copy=num

        pwr=len(str(num))

        calculated_value=0
        while copy>0:

            r=copy%10
            calculated_value=calculated_value+(r**pwr)
            copy=copy//10
            

        print(calculated_value)
        if num==calculated_value:
            print('Armstrong Number')
        else:
            print('Not a Armstrong Number')



class Zex:

    if __name__ == '__main__':
        obj=Practice()
        obj.IsArmstrong(153)
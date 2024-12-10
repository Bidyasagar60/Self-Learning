
def plusOne(digits):
    print('Hellow')
    for i in range(len(digits) - 1, -1, -1):
        print(i)
        if digits[i] < 9:
           digits[i]=digits[i]+1
           return digits
          
        else:
            digits[i]=0
            
    return  [1]+digits


if __name__=='__main__':
    digits=[9,9,9]
    print(plusOne(digits))

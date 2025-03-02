

def reverse(Num):
    
    reverse_Num=0
    
    while Num > 0:
        Last=Num%10
        reverse_Num=(reverse_Num*10)+Last
        Num=Num//10

    print(reverse_Num)





if __name__ == '__main__':

    ListA=[10400,12345]

    for ele in ListA:
        reverse(ele)
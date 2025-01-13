class Practice:

    def palindrome_check_inbuilt(self,str):

        if str == str[::-1]:
            print(f'{str} is palindrome.')
        else:
            print(f'{str} is not palindrome.')

    def palindrome_check(self,s):

        copy=''
        m=len(s)-1
        while (m >= 0):
            copy=copy+s[m]
            m-=1
        if s == str(copy):
            print(f'{s} is palindrome.')
        else:
            print(f'{s} is not palindrome.')

        





class Zax:

    if __name__ == '__main__':
        obj=Practice()
        obj.palindrome_check_inbuilt('dood')

        obj.palindrome_check('dood')
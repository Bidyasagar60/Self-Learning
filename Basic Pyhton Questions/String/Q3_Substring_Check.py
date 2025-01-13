class Practice:

    def sub_string_check_inbuilt(self,w,s):
        
        if s.upper() in w.upper():
            return True
        else:
            False

    def sub_string_check(self,w,s):

        for sw in list(s.split()):
            if sw.lower() == s.lower():
                return True
        
        return False




class Zax:

    if __name__ == '__main__':

        obj=Practice()
        if obj.sub_string_check_inbuilt('My Name is Jack','Jack'):
            print('Present')
        else:
            print('Not present')

        if obj.sub_string_check('My Name is Jack','Jack'):
            print('Present')
        else:
            print('Not present')

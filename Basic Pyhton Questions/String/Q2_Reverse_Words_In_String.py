class Practice:

    def reverse_string_inbuilt(self,word):

        new_str=''
        for w in word.split():
            new_str=w+' '+new_str

        print(new_str)

        print(' '.join(word.split()[::-1]))




class Zax:

    if __name__ == '__main__':
        obj=Practice()
        obj.reverse_string_inbuilt('jack is knight')
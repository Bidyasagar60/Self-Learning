from collections import Counter

class Practice:

    def word_count_inbuilt(self,s):

        print(Counter(s.split()))


    def word_count(self,s):

        dict={}
        
        for w in s.split():

            if dict.get(w,0)> 0 :
                dict[w]+=1
            else:
                dict[w]=1

        print(dict)


class Zax:

    obj=Practice()
    s = "hello world hello everyone"
    obj.word_count_inbuilt(s)
    obj.word_count(s)



    
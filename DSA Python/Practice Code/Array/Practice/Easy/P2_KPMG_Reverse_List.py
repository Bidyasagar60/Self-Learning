
"""
### 2. Reverse a List
**Question:** Write a Python program to reverse a given list without using the `reverse()` method.

"""


if __name__ == '__main__':

    ListA=[2,5,60,8,5,45,458]

    #print(f" Reverse List : {ListA[::-1]}")

    left=0
    right=len(ListA)-1

    while left < right:
        ListA[left],ListA[right]=ListA[right],ListA[left]

        left+=1
        right-=1

    print(f" Reverse List : {ListA}")

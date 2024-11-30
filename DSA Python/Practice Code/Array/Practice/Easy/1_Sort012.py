"""

Problem statement
You have been given an integer array/list(ARR) of size 'N'. It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

Note :
Try to solve the problem in 'Single Scan'. ' Single Scan' refers to iterating over the array/list just once or to put it in other words,
you will be visiting each element in the array/list just once.

"""

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def sortMidEff(arr,n):
    count0=0
    count1=0
    count2=0
    arrx=[]
    for ele in arr:

        if ele == 0:
            count0+=1
        elif ele == 1:
            count1+=1
        else :
            count2+=1
    
    for i in range(count0):
        arrx.append(0)
    
    for i in range(count1):
        arrx.append(1)
    
    for i in range(count2):
        arrx.append(2)
    
    return arrx


def sortEfficient(arr, n) :

	
    low=0
    mid=0
    high=len(arr)-1

    while(mid<=high):

        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1


#taking inpit using fast I/O
def takeInput(i) :
	n = int(input(f'Enter Array No {i}  lentgh:').strip())

	if n == 0 :
		return list(), 0

	arr =   list(map(int, input(f'Enter {n} elements for Array {i}: ').strip().split()))
            #list(map(int, stdin.readline(f'Enter {n} elements for Array {i} ').strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
if __name__ == '__main__':

    t = int(input('How many arrays want to check as test cases ? : ').strip())
    for i in range(t) :
        arr, n= takeInput(i)
        #sortEfficient(arr, n)
        arr=sortMidEff(arr,n)
        print(arr)
        #printAnswer(arr, n)

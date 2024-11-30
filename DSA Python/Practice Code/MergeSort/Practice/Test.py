from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def sortedarray(left, right, arr):
    left_len = len(left)
    right_len = len(right)

    i = j = k = 0

    while i < left_len and j < right_len:

        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1

        k += 1

    while i < left_len:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < right_len:
        arr[k] = right[j]
        j += 1
        k += 1


def sort012(arr, n):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]


    right = arr[mid:]

    sort012(left, len(left))
    sort012(right, len(right))

    return sortedarray(left, right, arr)


# taking inpit using fast I/O
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


if __name__ == '__main__':

    arr=[9,6,8,3,2]
    n=5
    sort012(arr, n)
    printAnswer(arr, n)

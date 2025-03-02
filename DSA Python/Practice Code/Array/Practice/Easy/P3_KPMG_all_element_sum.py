""" **Question:** Write a Python program to calculate the sum of all elements in a list without using `sum()`.  """


if __name__ == '__main__':

    ListA=[88,45,42,12,6,40]
    

    TargetSum=0
    for e in  ListA:
        TargetSum+=e

    print(f"Sum of Array : {TargetSum}")
    
    
# Remove Duplicates from a List (Order should not be changed)


if __name__ == '__main__':

    listA=[1, 2, 2, 3, 4, 4, 5]

    dict={}

    for a in listA:

        if dict.get(a,0) < 1:
            dict[a]=1
        else:
            dict[a]+=1
    
    listA=list(dict.keys())
    print(listA)


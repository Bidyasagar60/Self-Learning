
def merge_list(lst,FinalList=None):

    if FinalList is None:
        FinalList=[]

    for i in lst:
         if isinstance(i,list):
            merge_list(i,FinalList)
         else:
            FinalList.append(i)

    return FinalList


if __name__ == '__main__':

    nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]

    onelist=merge_list(nested_list)

    print(onelist)


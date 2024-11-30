
def findDuplicateElement(Element):

    CounterDic={}

    DuplicateList=[]

    for element in Element:

        CounterDic[element]=CounterDic.get(element,0)+1

    for key,value in CounterDic.items():

        if value >1:
            DuplicateList.append(key)

    print(DuplicateList)

if __name__ == '__main__':


    Element=[1,2,45,6,4,6,2,44,2,6]
    # print(Element)
    # print(set(Element))

    findDuplicateElement(Element)
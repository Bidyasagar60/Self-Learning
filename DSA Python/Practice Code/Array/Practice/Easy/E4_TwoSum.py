def twoSum(arr, target, n):


    result=[]
    arr.sort()


    dict={}

    for value in arr:

        if dict.get(value,0) > 0:
            dict[value]=dict.get(value,0)+1
        
        else:
            dict[value]=1

    for i in arr:
        needed=target-i
        
        if  dict.get(needed,0) > 0:

            result.append([i,needed])
            if i==needed:
                dict[needed]=dict.get(needed,0)-1
            else:
                dict[needed]=dict.get(needed,0)-1
                dict[i]=dict.get(i,0)-1

    return result

def twoSumX(arr, target, n):

    dict={}
    result=[]

    for i in arr:

        s=target-i

        if dict.get(s,0) > 0:
            result.append([i,s])
            dict[s]=dict[s]-1
        
        else:
             if dict.get(i,0)>0:
                dict[i]=dict[i]+1
             else:
                dict[i]=1
    
    if len(result) == 0:
        result.append([-1,-1])

    return result


if __name__ =='__main__':

    arr=[1,-1,-1,2,2]
    target=1

    result=twoSumX(arr,target,len(arr))
    print(result)
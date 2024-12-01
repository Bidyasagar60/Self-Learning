
def sort_element(arr,low,high):

    if low>=high:
        return arr
    
    else:
         i=low
         j=high
         pivotindex = i
         pivotvalue=arr[pivotindex]

         print(f"pivot value: {pivotvalue}")

         while (i < j):
            
            while arr[i]<=pivotvalue and i<=high-1:
                i+=1
            
            while pivotvalue<arr[j] and j>=low+1 :
                j-=1
                
            if i<j:
                    arr[i],arr[j]=arr[j],arr[i]
        
         arr[pivotindex],arr[j]=arr[j],arr[pivotindex]

         sort_element(arr,low,j-1)
         sort_element(arr,j+1,high)


def pairSum(arr, s):
               
    result=[]

    left=0
    right=len(arr)-1

    while(left < right ):

        total=arr[left]+arr[right]
        if total==s:
            
            leftcount=1
            rightcount=1

            while(left+1 < right and arr[left]==arr[left+1]):                    
                leftcount+=1
                left+=1

            if arr[left]==arr[right]:
                leftcount+=1
            
            while(right-1 > left and arr[right]==arr[right-1]):
                rightcount+=1
                right-=1

            print(f'Left Count:{leftcount}')
            print(f'Right Count:{rightcount}')
            result.extend([sorted([arr[left],arr[right]])]*(leftcount*rightcount))

            
            left+=1
            right-=1
        
        elif total>s:
            right-=1
        else:
            left+=1
    
    result.sort()
    return result



def pairSumBruteForce(arr,target_num):

    result=[]
    
    for index in range(len(arr)):

        for inner_index in range(index+1,len(arr)) :

            sum=arr[index]+arr[inner_index]

            if target_num==sum:
                result.append([min(arr[index],arr[inner_index]),max(arr[index],arr[inner_index])])
                result.sort()


    return result



def pairSumOptimal(arr,target_num):

    result=[]
    ExtraElement=[]
    Dict={}

    
    for num in arr:
        num_to_check=target_num-num

        if num_to_check in Dict and Dict[num_to_check]>0:

            result.append([min(num,num_to_check),max(num,num_to_check)])
            
            
            if Dict[num_to_check]>1:
                    ExtraElement.append(tuple([min(num,num_to_check),max(num,num_to_check)]))
              
        Dict[num]=Dict.get(num,0)+1
    

    for x in ExtraElement:

        result.append(list(x))



    result.sort()
    return result


if __name__ == '__main__':

    Target=4
    #element=[7,5,2,4,8,10,3]
    element=[2,-6,2,5,2]
    #[2,-3,3,3,-2]
    #sort_element(element,0,len(element)-1)
    #element.sort()
    print(element)
    #result=pairSum(element,Target)
    result=pairSumOptimal(element,Target)
    #result=pairSumBruteForce(element,Target)
    print(result)

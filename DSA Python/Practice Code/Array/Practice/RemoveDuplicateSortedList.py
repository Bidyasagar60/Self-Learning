def RemoveDuplicate(nums):

    #Todo: Time Complexity = O(n)
    OriginalLength = len(nums)
    UniqueLength = 0
    


    index=0

    if OriginalLength==2 and nums[0]==nums[1]:
        nums[1]='_'

        UniqueLength=1

    while index< len(nums)-1  :
        if nums[index]==nums[index+1]:
            nums.pop(index+1)
        else:
            index+=1

    UniqueLength=len(nums)

    x=UniqueLength
    while  x<OriginalLength:
        nums.append('_')
        x+=1




def OptimalRemoveDuplicate1(nums):
    #Todo: Time Complexity = O(n)

    if not nums:
     return 0

    X=0
    for j in range(1,len(nums)):
        if nums[X]!=nums[j]:
            X += 1
            nums[X]=nums[j]


    return X+1



if __name__=='__main__':

    nums=[-3,1,1,1,-12]
        #[1,2,3,4,4,6,6,7,8,9,10,10]
    print(nums)
    #print(list(set(nums)))
    print(nums[:OptimalRemoveDuplicate1(nums)])
    #print(nums)
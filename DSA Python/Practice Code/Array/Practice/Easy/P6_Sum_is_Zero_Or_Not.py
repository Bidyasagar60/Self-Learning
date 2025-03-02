#WRITE  A PROGRAM TO CHECK IF SUM OF ANY TWO NUMBERS IS ZERO OR NOT ?

def check_sum_zero(nums):

    nums.sort()
    left=0
    right=len(nums)-1

    while (left<right):

        s=nums[left]+nums[right]
        if s==0:
            return True
        
        if s < 0:
            left+=1
        else:
            right-=1

    return False



def optimized_sum_zero(nums):

    seen=set()

    for i in nums:

        if -i in seen:
            return True
        else:
            seen.add(i)
    
    return False



if __name__ == '__main__':

    ListA=[1,3,-1,9,7,-11,-77,2]

    print(check_sum_zero(ListA))


    print(optimized_sum_zero(ListA))


    
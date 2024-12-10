


def searchInsert( nums, target) -> int:

    # Brute Force Tecchnique
    """
    if target <= nums[0]:
        return 0
    
    if nums[len(nums)-1]==target:
        return len(nums)-1

    if nums[len(nums)-1]<target:
        return len(nums)

    for index in range(len(nums)-1):
        
        if nums[index]==target:
            return index
        elif nums[index]<target and target < nums[index+1]:
            return index+1
    
    return len(nums)

    """

    # Optimal Approach O(Log n) time complexity

    low=0
    high=len(nums)-1

    if target <= nums[0]:
        return 0
    
    if nums[len(nums)-1]==target:
        return len(nums)-1

    if nums[len(nums)-1]<target:
        return len(nums)

    while low <= high:
        
        mid=(low+high)//2

        if nums[mid]==target:
            return mid

        elif nums[mid]>target and nums[mid-1] < target:
            return mid 
        
        elif nums[mid]<target and nums[mid+1] > target:
            return mid+1
        
        elif nums[mid]>target:
            high=mid-1
        
        else :
            low=mid+1
    
    return -1


if __name__ == '__main__':

    nums=[2,3,4,8,9,10,11]
    target=16

    print(searchInsert(nums,target))


        

    






    
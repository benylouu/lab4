def is_monotonic(nums):
    decreasing = True
    increasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False
    return increasing or decreasing 
                          

           
print(is_monotonic([1,2,2,3]))
print(is_monotonic([6,5,4,4]))
print(is_monotonic([1,3,2]))
print(is_monotonic([1,2,4,5]))
print(is_monotonic([1,1,1,1]))

        

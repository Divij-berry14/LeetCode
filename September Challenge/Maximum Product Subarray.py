def maxProduct(nums):
    maximum = max(nums)
    for i in range(len(nums)-1):
        temp = nums[i] * nums[i+1]
        if temp >= maximum:
            maximum = temp
    return maximum

nums = [-2,0,-1]
print(maxProduct(nums))
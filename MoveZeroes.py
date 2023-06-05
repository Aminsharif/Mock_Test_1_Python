def moveZeroes(nums):
    def move(nums, i):
        if i >= len(nums):
            return nums
        
        if nums[i] == 0:
            nums.append(nums.pop(i))  # Move the zero to the end of the array
        
        return move(nums, i + 1)
    
    return move(nums, 0)
  
  
nums = [0,1,0,3,12]
moveZeroes(nums)

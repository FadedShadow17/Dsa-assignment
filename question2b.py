def can_friends_sit_together(nums, indexDiff, valueDiff):
    for i in range(len(nums)):
        for j in range(i + 1, min(i + indexDiff + 1, len(nums))):
            if abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False


nums = [2, 3, 5, 4, 9]
indexDiff = 2
valueDiff = 1
result = can_friends_sit_together(nums, indexDiff, valueDiff)
print(result)  

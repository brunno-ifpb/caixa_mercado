from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for c in range(i + 1, len(nums)):
                if nums[i] + nums[c] == target:
                    return [i, c]

a = Solution()
nums = eval(input())
target = int(input())
print(a.twoSum(nums, target))
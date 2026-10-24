class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i,num in enumerate(nums):
            curr = target - num

            if curr in memo:
                return [memo[curr],i]
            else:
                memo[num] = i
            
        return []
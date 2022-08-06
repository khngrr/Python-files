nums = [3, 2, 4]
target = 6

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()

print(solution.twoSum(nums, target))

        
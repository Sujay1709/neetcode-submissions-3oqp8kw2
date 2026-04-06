class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i,num in enumerate(nums)]
        arr.sort()
        l, r = 0, len(nums) - 1
        nums.sort()
        while l<r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                i1, i2 = arr[l][1], arr[r][1]
                return sorted([i1, i2])
                return [l, r]
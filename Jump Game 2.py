class Solution: 
    def jump(self, nums: List[int]) -> int:
        res = nums
        res[-1] = 0
        for n in range(len(nums)-2,-1,-1):
            minimum = float('inf')
            for number in range(n+1, n+nums[n]+1):
                if number >= len(res):
                    break
                else:
                    if res[number]<minimum:
                        minimum = res[number]
            res[n] = minimum + 1
        return res[0]

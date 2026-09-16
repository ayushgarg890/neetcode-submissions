class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digs={}
        for idx,num in enumerate(nums):
            if target-num in digs:
                return [digs[target-num],idx]
            digs[num]=idx
        return []
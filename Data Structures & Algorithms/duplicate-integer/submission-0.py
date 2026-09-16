class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        digs = {}
        for num in nums:
            if num in digs:
                return True
            digs[num]=1
        return False
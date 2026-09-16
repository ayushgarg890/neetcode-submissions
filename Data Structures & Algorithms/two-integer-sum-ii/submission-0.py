class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num={}
        for idx,al in enumerate(numbers):
            if target-al in num:
                return [num[target-al]+1,idx+1]
            num[al]=idx
        return []
        
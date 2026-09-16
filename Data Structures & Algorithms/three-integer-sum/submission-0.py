class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sumx = val+nums[l]+nums[r]
                if sumx==0:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
                elif sumx>0:
                    r-=1
                else:
                    l+=1
        return res
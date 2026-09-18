class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minx=nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                minx = min(minx,nums[l])
                break
            
            m = (l+r)//2

            minx = min(minx,nums[m])

            if nums[m] >= nums[l]:
                l=m+1
            else:
                r=m-1

        return minx;
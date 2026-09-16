class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        
        leftMax = [0]*n
        rigthMax = [0]*n

        leftMax[0]=height[0]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        
        rigthMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rigthMax[i]=max(rigthMax[i+1],height[i])

        res=0

        for i in range(n):
            res += min(leftMax[i], rigthMax[i]) - height[i]
        
        return res

        


        
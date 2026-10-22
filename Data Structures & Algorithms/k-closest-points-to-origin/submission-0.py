class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHp=[]

        for x,y in points:
            dist = (x**2) + (y**2)
            minHp.append([dist,x,y])
        
        heapq.heapify(minHp)
        res=[]
        
        while k>0:
            dist,x,y = heapq.heappop(minHp)
            res.append([x,y])
            k-=1
        return res

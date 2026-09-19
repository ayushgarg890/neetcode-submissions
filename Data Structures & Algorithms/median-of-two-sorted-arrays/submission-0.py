class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1),len(nums2)
        i=j=0
        med1=med2=0

        for count in range((l1+l2)//2+1):
            med2=med1
            if i<l1 and j<l2:
                if nums1[i] > nums2[j]:
                    med1 = nums2[j]
                    j+=1
                else:
                    med1 = nums1[i]
                    i+=1
            elif i<l1:
                med1 = nums1[i]
                i+=1
            else:
                med1 = nums2[j]
                j+=1
        
        if (l1+l2)%2==1:
            return float(med1)
        return (med1+med2)/2.0
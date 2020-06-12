def findPythagoreanTriplets(nums):
    nums1=[x*x for x in nums]
    nums1.sort()
    n=len(nums1)
    for i in range(n-1,0,-1):
        l = 0
        r = i-1
        while l<r:
            if nums1[l]+nums1[r]==nums1[i]:
                return True
            if nums1[l]+nums1[r]<nums1[i]:
                l+=1
            else:
                r-=1
    return False
    
print findPythagoreanTriplets([3, 12, 5, 13])
# True
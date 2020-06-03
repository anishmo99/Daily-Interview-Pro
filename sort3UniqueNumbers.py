def sortNums(nums):
    c1,c2,c3=0,0,0
    for i in nums:
        if i==1:
            c1+=1
        elif i==2:
            c2+=1
        else:
            c3+=1
    l1=c1*[1]+c2*[2]+c3*[3]
    return l1

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

def two_sum(list, target):
    s=set()
    for i in list:
        if target-i in s:
            return True
        s.add(i)
    return False
    

print(two_sum([4,7,1,-3,2], 5))
print(two_sum([4,7,1,-3,2],10))
# Trues

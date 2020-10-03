def firstRecurringCharacter(string):
    hash_set = set()
    # flag = False
    for s in string:
        if s not in hash_set:
            hash_set.add(s)
        else:
            # flag = True
            return s
            # return
        
    return None


print(firstRecurringCharacter('qwertty'))
# t

print(firstRecurringCharacter('qwerty'))
# None
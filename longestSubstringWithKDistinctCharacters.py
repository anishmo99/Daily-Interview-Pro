def longestSubstringWithKDistinctCharacters(str, k):
    i,j,max_count=0,0,0
    ump = {}
    while j<len(str):
        if len(ump)<=k:
            if str[j] not in ump:
                ump[str[j]]=1
            elif str[j] in ump:
                ump[str[j]]+=1
            if(len(ump)==k):
                max_count=max(max_count,j-i+1)
            j+=1
        else:
            ump[str[i]]-=1
            if ump[str[i]]==0:
                del ump[str[i]]
            i+=1
    return -1 if max_count==0 else max_count
    



print(longestSubstringWithKDistinctCharacters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
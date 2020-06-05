def longestPalindromicSubstring(str):
    n=len(str)
    dp=[[0 for x in range(n)] for y in range(n)]
    maxlength,start=1,0
    
    for i in range(n):
        dp[i][i]=True
    
    i=0
    while i<n-1:
        if str[i]==str[i+1]:
            dp[i][i+1]=True
            start=i
            maxlength=2
        i+=1
        
    k=3
    while k<=n:
        i=0
        while i<=n-k:
            j=i+k-1
            if str[i]==str[j] and dp[i+1][j-1]==True:
                dp[i][j]=True
                if maxlength<k:
                    start=i
                    maxlength=k
            i+=1
        k+=1
    print(str[start:start+maxlength])
    
str=input()
longestPalindromicSubstring(str)
        

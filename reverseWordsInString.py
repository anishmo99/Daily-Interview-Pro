class Solution:
    def reverseWords(self, str):
        stack = []
        result = ""
        
        for ch in str:
            if ch!=' ':
                stack.append(ch)
            else:
                while len(stack)!=0 :
                    result += stack.pop()
                result += ' '

        while len(stack)!=0 :
            result += stack.pop()
        
        return result

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
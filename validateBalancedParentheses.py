def validateBalancedParentheses(str):
    stack=[]
    for i in str:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if len(stack)==0: return False
            if i==')':
                if stack[len(stack)-1]=='{' or stack[len(stack)-1]=='[':
                    return False
#                stack.pop()
            if i=='}':
                if stack[len(stack)-1]=='(' or stack[len(stack)-1]=='[':
                    return False
#                stack.pop()
            if i==']':
                if stack[len(stack)-1]=='{' or stack[len(stack)-1]==')':
                    return False
            stack.pop()
    return True if len(stack)==0 else False
str=input()
print(validateBalancedParentheses(str))

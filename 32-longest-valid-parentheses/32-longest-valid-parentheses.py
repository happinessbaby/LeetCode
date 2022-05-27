class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        max_len = 0
        # for i in range(len(s)):
        #     if stack[-1]=="(" and s[i]==")":
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
        # for i in range(len(s)):
        #     if s[i]=="(":
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack)==0:
        #             stack.append(i)
        #         else:
        #             max_len = max(max_len, i-stack[-1])
        # return max_len
        right = 0
        left = 0
        max_len = 0
        for i in range(len(s)):
            if s[i]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                max_len = max(max_len, 2*left)
            elif right>=left:
                left=right=0
        left=right=0
        for j in range(len(s)-1, -1, -1):
            if s[j]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                max_len = max(max_len, 2*left)
            elif left>=right:
                left=right=0
        return max_len
            
                
            
                
                
                
                
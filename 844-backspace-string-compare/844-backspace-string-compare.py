class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in range(len(s)):
            if s[i]!='#':
                stack1.append(s[i])
            if s[i]=='#' and stack1:
                stack1.pop()
        stack2 = []
        for i in range(len(t)):
            if t[i]!='#':
                stack2.append(t[i])
            if t[i]=='#' and stack2:
                stack2.pop()
        return True if stack1==stack2 else False
                
                
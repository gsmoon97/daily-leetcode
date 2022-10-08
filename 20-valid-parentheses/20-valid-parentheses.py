class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        # iterate from left to right
        # use DFS
        for x in s:
            if (x in op):
                stack.append(x)
            else:
                # check if any opening brackets are left to be closed
                if not stack:
                    return False                
                y = stack.pop()
                # check if the bracket types correspond
                if op.index(y) != cl.index(x):
                    return False
        # check if any opening brackets are left unclosed
        if not stack:
            return True
        else:
            return False
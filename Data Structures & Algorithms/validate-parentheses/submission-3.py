class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2!=0:
            return False
        close_to_open = {
            ']':'[', 
            '}': '{',
            ')':'('
        }

        stack = []
        for ch in s:
            if ch not in close_to_open:
                stack.append(ch)
            else:
                open_pair = close_to_open.get(ch)
                if stack == [] or stack.pop() != open_pair:
                    return False
        if stack: 
            return False 
        else:
             return True
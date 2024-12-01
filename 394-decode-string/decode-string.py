class Solution:
    def decodeString(self, s: str) -> str:
        # we will keep tracl of open and closed brackets
        # ok, if the counter is still >0 then we should keep looking for ], and cannot wrap up

        # we will implement a stack, 
        # everytime we see a number, we will not immediately write that many times into output
        # because the string might have nested brackets
        # that's why wonce we see anumber we will store that many copies of the bracket value back 
        # into stack

        # "3[a]2[bc]"
        # "3[a2[c]]"
        # "2[abc]3[cd]ef"

        stack = []

        # we want to iteratively add the characters of the string into stack
        # when we see a ], meaning. when we get the inner not nested brackets
        # we want to collapse them 
        # ex: 3[a2[c]]. => 3[acc] => accaccacc

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: 
                subs = ""
                while stack[-1] != "[":
                    subs = stack.pop() + subs
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * subs)
            
        return "".join(stack)



             

        

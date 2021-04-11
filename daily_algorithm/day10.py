# 1021. 删除最外层的括号
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, stack = "", []
        for c in S:
            if c == "(":
                if stack: res += c
                stack.append("(")
            if c == ")":
                stack.pop()
                if stack: res += c
        return res

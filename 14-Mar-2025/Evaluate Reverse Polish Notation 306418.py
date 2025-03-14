# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, s: List[str]) -> int:
        stk=[]
        for op in s:
            if op == '+':
                stk.append( stk.pop() + stk.pop())
            elif op == '-':
                a, b= stk.pop(), stk.pop()
                stk.append(b-a)
            elif op == '*':
                stk.append(stk.pop()*stk.pop())
            elif op == '/':
                a, b= stk.pop(), stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(op))
        return stk[0]

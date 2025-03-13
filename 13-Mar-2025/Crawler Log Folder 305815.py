# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk=[]
        for i in range(len(logs)):
            if logs[i]=='./':
                stk=stk
            elif logs[i]=='../':
                if stk:
                    stk.pop()
            else:
                stk.append(logs[i])
        return len(stk)
# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        has={1:"qwertyuiop", 2:"asdfghjkl", 3:"zxcvbnm"}
        for word in words:
            row1=0
            row2=0
            row3=0
            for i in word.lower():
                if i in has[1]:
                    row1+=1
                if i in has[2]:
                    row2+=1
                if i in has[3]:
                    row3+=1
            if row1== len(word) or row2== len(word)or row3== len(word):
                ans.append(word)
        return ans
                
        
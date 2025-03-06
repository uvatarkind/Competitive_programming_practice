# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count5 = count10= 0
        for i in range(len(bills)):
            if bills[i]==5:
                count5+=1
                
            elif bills[i]==10:
                if count5>=1:
                    count5-=1
                    count10+=1
                else:
                    return False
            else:

                if count5>=1 and count10>=1:
                    count5-=1
                    count10-=1
                elif count5>=3:
                    count5-=3
                else:
                    return False
        return True
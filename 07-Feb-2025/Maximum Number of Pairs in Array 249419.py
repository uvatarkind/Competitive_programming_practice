# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_pair=0
        count_left=0
        counter =  Counter(nums)
        print(counter)
        for key, val in counter.items():
            if val %2 !=0:
                 count_left += 1
            count_pair+= val // 2
        

        return [count_pair, count_left]



        
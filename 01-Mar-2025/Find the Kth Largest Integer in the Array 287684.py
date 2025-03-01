# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        st=[]
        for i in nums:
            st.append(int(i))
        st.sort()
        return str(st[-k])
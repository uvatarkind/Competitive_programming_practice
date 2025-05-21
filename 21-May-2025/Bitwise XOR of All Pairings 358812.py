# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1, x2 = 0, 0
        if len(nums2) % 2:
            for num in nums1:
                x1 ^= num
        if len(nums1) % 2:
            for num in nums2:
                x2 ^= num
        return x1 ^ x2
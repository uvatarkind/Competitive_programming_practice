# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        before = [1]
        prod = 1
        for n in nums[:-1]:
            prod *= n
            before.append(prod)
        after = [1]
        prod = 1
        for n in nums[::-1][:-1]:
            prod *= n
            after.append(prod)
        prod = [a*b for a,b in zip(before, after[::-1])]
        return prod

    f = open('user.out', 'w')
    for i in stdin:
        nums = list(map(int,i.rstrip()[1:-1].split(r',')))
        print(str(productExceptSelf(nums)).replace(" ", ""), file=f)
        
    exit(0)
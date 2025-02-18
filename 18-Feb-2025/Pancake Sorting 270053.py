# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1,-1,-1):
            max_index = 0
            for j in range(i+1):
                if arr[max_index] < arr[j]:
                    max_index = j
            if max_index!=i:
                res.append(max_index+1)
                arr = list(reversed(arr[:max_index+1])) + arr[max_index+1:]
                res.append(i+1)
                arr = list(reversed(arr[:i+1])) + arr[i+1:]
        return res



# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(p1 : int, flag: bool, arr: deque) -> bool:
            if not arr:
                return p1 >= 0 

            if flag:
                arr_left = deque(arr)
                left = arr_left.popleft()
                win_left = rec(p1 + left, not flag, arr_left)

                arr_right = deque(arr)
                right = arr_right.pop()
                win_right = rec(p1 + right, not flag, arr_right)

                return win_left or win_right
            else:
                arr_left = deque(arr)
                left = arr_left.popleft()
                lose_left = rec(p1 - left, not flag, arr_left)

                arr_right = deque(arr)
                right = arr_right.pop()
                lose_right = rec(p1 - right, not flag, arr_right)

                return lose_left and lose_right

        return rec(0, True, deque(nums))

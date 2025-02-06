# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        count_char= Counter(chars)
        for word in words:
            CanBeFormed=True
            count_word=Counter(word)
            for key in count_word:
                if key not in count_char:
                    CanBeFormed=False
                    break
                if count_word[key]>count_char[key]:
                    CanBeFormed=False
                    break
            if CanBeFormed ==True:
                ans+=len(word)
        return ans
        
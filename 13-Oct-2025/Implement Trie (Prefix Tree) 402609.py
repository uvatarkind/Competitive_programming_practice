# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.children={}
        self.word = False

    def insert(self, word: str) -> None:
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.word=True

    def search(self, word: str) -> bool:
        root= self
        for char in word:
            if char not in root.children:
                return False
            root= root.children[char]
        return root.word
    def startsWith(self, prefix: str) -> bool:
        root= self
        for char in prefix:
            if char not in root.children:
                return False
            root= root.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
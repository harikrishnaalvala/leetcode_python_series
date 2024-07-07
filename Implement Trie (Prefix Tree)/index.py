class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]
class Trie:

    def __init__(self):
        self.trie=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.trie
        for c in word:
            if curr.children[ord(c)-ord("a")]==None:
                curr.children[ord(c)-ord("a")]=TrieNode()
            curr=curr.children[ord(c)-ord("a")]
        curr.is_end=True

    def search(self, word: str) -> bool:
        curr=self.trie
        for c in word:
            if curr.children[ord(c)-ord("a")]==None:
                return False
            curr=curr.children[ord(c)-ord("a")]

        if curr.is_end:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.trie
        for c in prefix:
            if curr.children[ord(c)-ord("a")]==None:
                return False
            curr=curr.children[ord(c)-ord("a")]
        # curr.is_end=True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

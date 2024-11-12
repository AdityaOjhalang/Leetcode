class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:

        def dfs(ind,root):
            node = root

            for i in range(ind,len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                else:
                    if c in node.children:
                        node = node.children[c]
                    else:
                        return False
            return node.end
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
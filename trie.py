class Trie:
    def __init__(self):
        self.children = {}
        self.end = False;

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.end = True

    def get_suffixes(self, soFar):
        suffixes = []
        for (char, node) in self.children.items():
            if node.end is True:
                suffixes.append(soFar + char)
            else: suffixes.extend(node.get_suffixes(soFar + char))

        return suffixes

    def autocomplete(self, start):
        node = self
        for char in start:
            if char in node.children:
                node = node.children[char]
            else: return list()
        return list(node.get_suffixes(start))

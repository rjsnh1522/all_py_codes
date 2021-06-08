class Node:
    def __init__(self, word_end=False):
        self.word_end = word_end
        self.prefix_count = 0
        self.table = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for k in word:
            if k not in current.table:
                current.table[k] = Node()
            current = current.table[k]
            current.prefix_count += 1
        current.word_end = True

    def search(self, prefix):
        current = self.root
        for k in prefix:
            if k not in current.table:
                return False
            current = current.table[k]
        return current.word_end

    def count(self, prefix):
        current = self.root
        for k in prefix:
            if k not in current.table:
                return 0
            current = current.table[k]
        return current.prefix_count

    def _walk(self, root, prefix):
        out = []
        if root.word_end:
            out.append(prefix)
        for ch in root.table:
            if isinstance(prefix, tuple):
                temp = self._walk(root.table[ch], prefix + (ch,))
            elif isinstance(prefix, list):
                temp = self._walk(root.table[ch], prefix + [ch])
            else:
                temp = self._walk(root.table[ch], prefix + ch)
            out.extend(temp)
        return out

    def auto_complete(self, prefix):
        current = self.root
        for k in prefix:
            if k not in current.table:
                return []
            current = current.table[k]
        return self._walk(current, prefix)


words = ['apple', 'ape', 'den', 'dear', 'do', 'disco']

db = Trie()
for wo in words:
    db.insert(wo)

print(db.auto_complete('ap'))

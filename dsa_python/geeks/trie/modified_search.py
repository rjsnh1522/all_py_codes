from .trie_imp import Trie


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        trie_a = Trie()
        trie_b = Trie()
        for i in A:
            trie_a.insert(i)
        for i in B:
            trie_b.insert(i)

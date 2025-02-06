class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        letters = []
        for a, b in zip(word1, word2):
            letters.append(a)
            letters.append(b)

        diff = len(word1) - len(word2)
        if diff > 0:
            remaining = word1[-diff:]
        elif diff < 0:
            remaining = word2[diff:]
        else:
            remaining = []
        
        for c in remaining:
            letters.append(c)
        return ' '.join(letters)


print(Solution().mergeAlternately("abc", "pq"))
Solution().mergeAlternately("ab", "pqr")
Solution().mergeAlternately("abc", "pqr")

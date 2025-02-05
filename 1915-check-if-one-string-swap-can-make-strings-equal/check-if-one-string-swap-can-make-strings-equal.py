from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True


        if set(s1) != set(s2) or len(s1) != len(s2):
            return False

        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]


        return len(diff_indices) == 2 and s1[diff_indices[0]] == s2[diff_indices[1]] and s1[diff_indices[1]] == s2[diff_indices[0]]

        
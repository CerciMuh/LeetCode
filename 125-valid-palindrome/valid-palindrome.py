class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = "".join(i for i in s if i.isalnum())
        trimmed =trimmed.lower()
        l=0
        r=len(trimmed)-1
        while (r>l):
            if trimmed[l] == trimmed[r]:
                l+=1
                r-=1
            else:
                return False
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = "".join(x for x in s if x.isalnum())
        formattedString = formattedString.lower()
        left = 0 
        right = len(formattedString)-1
        while right>left:
            if formattedString[left]!= formattedString[right]:
                return False
            left+=1
            right -=1
        return True
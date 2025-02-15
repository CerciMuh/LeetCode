class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        

        window_count = {}
        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1
        

        if s1_count == window_count:
            return True
        

        for i in range(len(s1), len(s2)):

            window_count[s2[i]] = window_count.get(s2[i], 0) + 1
            

            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]  
            
            if s1_count == window_count:
                return True
        
        return False

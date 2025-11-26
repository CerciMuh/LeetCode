class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        maxWindowSize = len(p)
        countP = {}
        window = {}
        output = []
        for x in p:
            countP[x]=countP.get(x,0)+1
        while right < len(s):
            window[s[right]] = window.get(s[right],0)+1
            if right-left +1  == maxWindowSize:
                if window == countP:
                    output.append(left)
                window[s[left]] -=1
                if window[s[left]] == 0 :
                    del window[s[left]]
                left +=1
            right+=1
        return output



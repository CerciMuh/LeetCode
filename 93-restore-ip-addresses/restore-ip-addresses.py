class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if (len(s)>12 or len(s)<4):
            return []
        
        res = []

        def dfs(i, dots, path):
            if (dots == 4 and i == len(s)):
                res.append(path[:-1])
                return
            for j in range(i,min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i==j or s[i] != "0"):
                    dfs(j+1, dots + 1, path + s[i:j+1]+".")
        dfs(0,0,"")
        return res
                    
                    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for string in strs:
            counts = [0]*26
            for char in string:
                counts[ord(char)-ord("a")]+=1
            key = tuple(counts)

            if key not in grouped:
                grouped[key] = []
            grouped[key].append(string)

        return list(grouped.values())
                


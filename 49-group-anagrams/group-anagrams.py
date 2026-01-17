class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can go through the list in a for loop 
        #how can we see if the words have the same letters?
        #we can set a key value pair
        #key will be weight of the word and value will be list of words of that weight
        #so for loop; then a for loop for the letters of the word/ to calculate its weight. 
        # take the weight and use it as a key, value will be the words of this weight. group key values in list of lists return the list of lists

        hashmap = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]

        return list(hashmap.values())
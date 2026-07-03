class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        # key=sorted anagram
        # value=list containing group of anagrams

        anagrams = {}
        for word in strs:
            sorted_s = str(sorted(word))
            if sorted_s in list(anagrams.keys()):
                anagrams.get(sorted_s).append(word)
            else:
                anagrams[sorted_s] = [word]
        return list(anagrams.values())
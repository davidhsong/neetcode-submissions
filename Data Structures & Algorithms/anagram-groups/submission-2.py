class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        org = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in org.keys():
                org[sorted_s].append(s)
            else:
                org[sorted_s] = [s]
        return list(org.values())
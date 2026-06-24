class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            s_sorted = sorted(s)
            s_sorted = "".join(s_sorted)
            d[s_sorted].append(s)

        return list(d.values())

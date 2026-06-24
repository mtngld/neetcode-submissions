class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for x in nums:
            counter[x] += 1

        sorted_counter = sorted(counter.items(), key=lambda x : x[1], reverse=True)
        result = []
        for idx in range(k):
            result.append(sorted_counter[idx][0])
        return result
        
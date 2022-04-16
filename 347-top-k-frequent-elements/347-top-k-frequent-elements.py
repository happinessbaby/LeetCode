class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = defaultdict(int)
        for n in nums:
            memo[n]+=1
        return heapq.nlargest(k, memo.keys(), key=memo.get)
        
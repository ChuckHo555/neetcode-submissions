class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)

        for num in hashMap.keys():
            heapq.heappush(heap, (hashMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
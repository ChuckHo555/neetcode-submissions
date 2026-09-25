class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = []
        output =  []

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) +1

        for i in hashMap.keys():
            heapq.heappush(heap, (hashMap[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output

        
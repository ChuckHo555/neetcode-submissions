class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freqList = [[] for i in range(len(nums)+1)]

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) +1
        
        for i, j in hashMap.items():
            freqList[j].append(i)

        outList = []

        for n in range(len(freqList)-1, 0, -1):
            for m in freqList[n]:
                outList.append(m)

                if len(outList) == k:
                    return outList
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxConsec = 0

        left = 0
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left+=1
            hashSet.add(s[right])
            maxConsec = max(maxConsec, right-left+1)

        return maxConsec


        
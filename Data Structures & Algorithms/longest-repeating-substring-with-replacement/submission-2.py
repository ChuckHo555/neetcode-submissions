class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        mostDup = 0
        left = 0

        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            if (right-left +1) - max(hashMap.values()) > k:
                hashMap[s[left]]-=1
                left+= 1
            mostDup = max(mostDup, right-left+1)
        return mostDup

            
       
       

        
        
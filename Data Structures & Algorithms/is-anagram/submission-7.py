class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1, hashMap2 = {}, {}
        
        for i in range(len(s)):
            hashMap1[s[i]] = 1 + hashMap1.get(s[i], 0)
            hashMap2[t[i]] = 1 + hashMap2.get(t[i], 0)

        return hashMap1 == hashMap2

   

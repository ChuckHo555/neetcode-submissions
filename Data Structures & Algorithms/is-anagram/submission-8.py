class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for i in range(len(s)):
            hashMap1[s[i]] = 1 + hashMap1.get(s[i], 0)
        for i in range(len(t)):
            hashMap2[t[i]] = 1 + hashMap2.get(t[i], 0)

        return hashMap2 == hashMap1

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window, countT = {}, {}

        for count in range(len(t)):
            countT[t[count]] = countT.get(t[count], 0) +1

        res = [-1,-1]
        resLength = float('infinity')
        left = 0
        have, need = 0, len(countT)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have+=1
            while have == need:
                if resLength > (right-left+1):
                    resLength = right-left+1
                    res = [left,right]
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have-=1

                left+=1
        l, r = res
        return s[l:r+1] if resLength != float('infinity')else  ''
            
            
            
                














class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in strs:
            newString += str(len(i)) + '#' + i 
        return newString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            stringLength = int(s[i:j])
            i=j+1
            j = i +stringLength
            decodedStrings.append(s[i:j])
            i = j
        return decodedStrings



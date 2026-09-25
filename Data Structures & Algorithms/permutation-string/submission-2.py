class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Initialize hashmaps for character frequencies
        hashMapS1, hashMapS2 = {}, {}
        
        # Count frequencies of characters in s1
        for i in range(len(s1)):
            hashMapS1[s1[i]] = hashMapS1.get(s1[i], 0) + 1
            hashMapS2[s2[i]] = hashMapS2.get(s2[i], 0) + 1
        
        # Initial check for matching character counts
        if hashMapS1 == hashMapS2:
            return True
        
        # Sliding window
        left = 0
        for right in range(len(s1), len(s2)):
            # Add the new character (s2[right])
            hashMapS2[s2[right]] = hashMapS2.get(s2[right], 0) + 1
            
            # Remove the old character (s2[left])
            hashMapS2[s2[left]] -= 1
            if hashMapS2[s2[left]] == 0:
                del hashMapS2[s2[left]]
            
            # Check if the window matches
            if hashMapS1 == hashMapS2:
                return True
            
            left += 1
        
        return False

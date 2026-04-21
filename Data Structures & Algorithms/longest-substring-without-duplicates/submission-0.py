class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        i=0
        max_length=0

        for j in range(len(s)):
             while s[j] in window:
                window.remove(s[i])
                i+=1
             window.add(s[j])
             max_length= max(max_length, j-i+1)
        return max_length
        
        
        
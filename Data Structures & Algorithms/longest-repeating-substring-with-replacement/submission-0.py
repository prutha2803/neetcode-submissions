class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        freq={}
        max_freq=0
        max_length=0

        for j in range(len(s)):
            if s[j] in freq:
                freq[s[j]]+=1
            else:
                freq[s[j]]=1

            max_freq= max(max_freq, freq[s[j]])

            if ((j-i+1)- max_freq)>k:
                freq[s[i]]-=1
                i+=1

            max_length= max(max_length, (j-i+1))
        return max_length
        
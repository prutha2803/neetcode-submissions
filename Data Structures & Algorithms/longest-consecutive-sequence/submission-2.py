class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest=0

        for i in numset:
            if i-1 not in numset:
                current = i
                length=1

                while current + 1 in numset:
                    current+=1
                    length+=1
            
                longest= max(longest, length)
        
        return longest

        
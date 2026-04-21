class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read=1
        write=0
        if len(nums)==1:
            return 1
        else:
            for read in range(1, len(nums)):
                if nums[read]!= nums[write]:
                    write+=1
                    nums[write]= nums[read]

            return write+1

        
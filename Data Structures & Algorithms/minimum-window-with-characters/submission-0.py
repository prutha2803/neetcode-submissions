class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or s=="":
            return ""
        
        t_count={}
        for c in t:
            t_count[c]= t_count.get(c,0)+1

        need= len(t_count)
        have=0
        win_count={}
               
        result=""
        result_len= float("infinity")
        left=0

        for right in range(len(s)):
            c=s[right]
            win_count[c]=win_count.get(c,0)+1

            if c in t_count and win_count[c]==t_count[c]:
                have+=1
            
            while have==need:
                if(right-left+1)< result_len:
                    result_len= right-left +1
                    result= s[left:right+1]

                win_count[s[left]]-=1

                if s[left]in t_count and win_count[s[left]]< t_count[s[left]]:
                    have-=1
                
                left+=1
        return result
        
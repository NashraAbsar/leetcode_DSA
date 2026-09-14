class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}      #dict for roman to numeric
        total=0
        for i in range(len(s)):
            curr_val=roman_values[s[i]]                          # 0-n tk index ki numeric value store krta hai
            if i+1<len(s) and curr_val<roman_values[s[i+1]]:     #aage aur letter h? and curr wla next se chota h?
                total-=curr_val                                  
            else:
                total+=curr_val
        return total                                             #inp m string leke op me int
        
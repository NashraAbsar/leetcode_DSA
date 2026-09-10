class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        flag=True
        let=min(strs,key=len)
        for i in range(0,len(let)):
            for s in strs:
                if s[i]!=let[i]:
                    flag=False
                    break
            if flag:
                pre+=let[i]
        return pre
                    
                
        
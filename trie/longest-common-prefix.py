class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]

        for item in strs:
            for x in range(len(item)):
                if item[x]!=res[x]:
                    break
            if x==0:
                return ""
                
            if x<=len(item):
                res=item[0:x]


        return res
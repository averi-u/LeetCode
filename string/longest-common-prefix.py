class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]

        for item in strs:
            for x in range(len(item)):
                if item[x]!=res[x]:
                    break

            res=item[0:x]


        return res
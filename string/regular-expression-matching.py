class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def only_star(p):
            p = set(p)
            for c in list(p):
                if c != '*':
                    return False
            return True
        def dfs(i, j):
            nonlocal s, p
            if i == len(s) and only_star(p[j:]):
                return True
            if i == len(s) and not only_star(p[j:]):
                return False
            if j == len(p):
                return False
            if ord('a') <= ord(p[j]) <= ord('z'):
                if s[i] != p[j]:
                    return False
                return dfs(i+1, j+1)
            elif p[j] == '.':
                return dfs(i+1, j+1)
            else:
                return dfs(i+1, j) or dfs(i, j+1) or dfs(i+1, j+1)
        return dfs(0, 0)
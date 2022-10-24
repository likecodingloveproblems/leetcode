class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = dict()
        t_to_s = dict()
        for sc, tc in zip(s, t):
            if s_to_t.get(sc, False) or t_to_s.get(tc, False):
                if s_to_t.get(sc, False) and s_to_t[sc] != tc:
                    return False
                else:
                    s_to_t[sc] = tc
                if t_to_s.get(tc, False) and t_to_s[tc] != sc:
                    return False
                else:
                    t_to_s[tc] = sc
            else:
                s_to_t[sc] = tc
                t_to_s[tc] = sc
        return True


ss, tt = "egg", "add"
r = Solution().isIsomorphic(ss, tt)
print(r)

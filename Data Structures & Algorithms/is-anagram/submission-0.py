class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars={}
        for c in s:
            chars[c] = 1 + chars.get(c,0)
        
        for c in t:
            chars[c] = chars.get(c,0) - 1
        
        for c in chars:
            if chars.get(c) !=0:
                return False
        
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        while l!=0 and s!='':
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                l -= 1
        if s =="":
            return True
        else:
            return False
        
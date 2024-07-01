class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = []
        c = len(a)-1
        while c>=0:
            b.append(a[c])
            c-=1
        return ' '.join(b)

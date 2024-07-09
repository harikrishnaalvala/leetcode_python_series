class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        for i in digits:
            a+=str(i)
        b=int(a)
        b=b+1
        b=str(b)
        result=[]
        for i in b:
            result.append(int(i))
        return result

        

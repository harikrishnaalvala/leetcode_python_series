class Solution:
    def isHappy(self, n: int) -> bool:
        def new_digit(n,seen):
        
            n=str(n)
            a=0 # temprary variable for sum
            for i in n:# to get the sum of sqaures of digit 
                a+=(int(i))**2
            if a==1:
                return True   
            if a in seen:
                return False # infinte recursion 
            seen.add(a)
            
                
            flag=new_digit(a,seen)
            return flag# return the final result to main function 
        return new_digit(n,set())

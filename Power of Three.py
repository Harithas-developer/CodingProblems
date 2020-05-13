# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False   
        a = 1162261467 % n
        if a==0:
            return True
        else:
            return False
        
        ################################

        2nd Method
        
        if n<1:
            return False
        
        while n%3==0:
            n/=3
        return n==1
        

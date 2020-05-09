# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [False for i in range(n+1)]
        for i in range(2,n):
            if primes[i] == False:
                count+=1
                j = 2
                while j*i < n:
                    primes[j*i] = True
                    j+=1
        return count
        
        
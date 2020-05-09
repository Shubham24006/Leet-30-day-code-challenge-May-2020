# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true
# Example 2:
#
# Input: 14
# Output: false

# solution:
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        while i*i <= num:
            if i*i == num:
                return True
            i+=1
        return False
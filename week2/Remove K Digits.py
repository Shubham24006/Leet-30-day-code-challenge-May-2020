# Given a non-negative integer num represented as a string, remove k digits from the number so that the new
# number is the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

#Solution:

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_len = len(num)
        if num_len == k:
            return "0"
        else:
            i=0
            while i<num_len-1 and k>0:
                if int(num[i]) > int(num[i+1]):
                    num = num[0 : i] + num[i + 1 :]
                    i = -1
                    k -=1
                    num_len-=1
                i+=1
            if k>0:
                num = num.strip("0")[:-k]
                if num:
                    return num
                else:
                    return "0"
            else:
                return str(int(num))



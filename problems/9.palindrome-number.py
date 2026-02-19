#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (60.22%)
# Likes:    15644
# Dislikes: 2916
# Total Accepted:    7.7M
# Total Submissions: 12.9M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]
        
# @lc code=end


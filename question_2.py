# question_2.py
"""
**LONGEST PALINDROMIC SUBSTRING**

 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """

        str = ""
        for i in range(len(s)):
                l, r = i, i
                while l >= 0 and r < len(s) and s[1] == s[r]:  # Check for odd length palindromes
                        if   (r - l + 1) > len(str):
                                str = s[l:r+1]
                        l -= 1
                        r += 1

                l, r = i, i + 1
                while l >= 0  and r < len(s) and s[l] == s[r]:  # Check for even length palindromes
                        if (r - l + 1) > len(str):
                                str = s[l:r+1]
                                l -= 1
                                r += 1


        return str


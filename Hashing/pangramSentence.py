# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 
# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

from collections import defaultdict

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count = defaultdict(int)
        
        for char in sentence:
            count[char] += 1
            
        if len(count) == 26:
            return True
        return False

# Time complexity: O(n)
# Space complexity: O(1)
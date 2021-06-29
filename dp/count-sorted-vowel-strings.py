"""
1641. Count Sorted Vowel Strings
https://leetcode.com/contest/weekly-contest-213/problems/count-sorted-vowel-strings/
User Accepted:3058
User Tried:3352
Total Accepted:3149
Total Submissions:4172
Difficulty:Medium

Result:
Date: 2020-11-10
time consumption: over 310 minute

41 / 41 test cases passed.

Status: Accepted
Runtime: 8356 ms
Memory Usage: 14.2 MB

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 
"""

from typing import List


class Solution:
    def down_counter(self, init_case: List[int], count: int) -> int:
        cur = init_case
        stop_case = [1 for _ in range(len(init_case))]
        indices = [i for i in range(len(init_case))]
        max_index = len(cur) - 1

        while cur != stop_case:
            if cur[-1] < 0:
                break
            if cur[len(init_case) - 1] == 1:
                for index in indices:
                    if (index + 1) <= max_index:
                        if cur[index + 1] == 1:
                            cur[index] -= 1
                            for idx in range(index, max_index):
                                cur[idx + 1] = cur[idx]
                            break
                count += 1
                continue

            cur[len(init_case) - 1] -= 1
            count += 1

        return count

    def countVowelStrings(self, n: int) -> int:
        init_case = [5 for _ in range(n)]
        count_val = self.down_counter(init_case=init_case, count=1)

        return count_val


if __name__ == "__main__":
    solution = Solution()

    test_cases = [(4, 70), (5, 126)]

    for test_case in test_cases:
        n = test_case[0]
        expected_value = test_case[1]
        answer = solution.countVowelStrings(n=n)
        print(f"answer: {answer},\texpected: {expected_value}")

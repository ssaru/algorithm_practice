"""
1647. Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/contest/weekly-contest-214/problems/minimum-deletions-to-make-character-frequencies-unique/

User Accepted:2823
User Tried:3202
Total Accepted:2925
Total Submissions:6360
Difficulty:Medium

Result:
#1
Date: 2020-11-14
Duration: 76m

103 / 103 test cases passed.
Status: Accepted
Runtime: 136 ms, faster than 63.53% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
Memory Usage: 15.4 MB, less than 6.38% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""
from collections import Counter


class Solution:

    # 1
    def minDeletions(self, s: str) -> int:

        frequency_dict = Counter(list(s))  # O(n) -> list 안써도 된다. O(N)으로 두번 도는 것이다.
        frequency_val = list(frequency_dict.values())  # O(1) # worst char 26 # BigO 정의법 확인

        num_deletion = 0
        while True:
            # O(1)?? -> 위험을 내재하고있다. while문 지양. return이 무조건 들어가야하는데, return을 보장해야하는데, 보장이 어렵다.
            frequency_val = [i for i in frequency_val if i != 0]  # O(1)
            overlap_dict = dict(Counter(frequency_val))  # O(1)
            overlap_val = overlap_dict.values()  # O(1)

            # O(1) and O(n) and O(1)
            if (len(set(overlap_val)) == 1) and (sum(overlap_val) == len(overlap_val)):
                return num_deletion

            for key in overlap_dict:  # O(n)
                if overlap_dict[key] >= 2:
                    frequency_val[frequency_val.index(key)] -= 1
                    num_deletion += 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("aab", 0),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    ]

    for test_case in test_cases:
        s = test_case[0]
        expected_value = test_case[1]
        answer = solution.minDeletions(s=s)
        print(f"answer: {answer},\texpected: {expected_value}")

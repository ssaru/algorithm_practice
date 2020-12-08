"""
1673. Find the Most Competitive Subsequence
https://leetcode.com/contest/weekly-contest-217/problems/find-the-most-competitive-subsequence/

User Accepted:1464
User Tried:3185
Total Accepted:1519
Total Submissions:8143
Difficulty:Medium

Result

#1
Date: 2020-12-08

72 / 86 test cases passed.
Status: Time Limit Exceeded
Submitted: 5 minutes ago

Duration: 40m

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
"""

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        ans, start_ptr = [], 0
        partial_nums = nums
        for i in range(k, 0, -1):
            partial_nums = partial_nums[start_ptr:]
            candidates = partial_nums[: len(partial_nums) - (i - 1)]
            min_val = min(candidates)
            ans.append(min_val)

            min_val_ptr = partial_nums.index(min_val)
            start_ptr = min_val_ptr + 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 5, 2, 6], 2, [2, 6]),
        ([2, 4, 3, 3, 5, 4, 9, 6], 4, [2, 3, 3, 4]),
    ]

    for test_case in test_cases:
        nums, k, expected_value = test_case
        answer = solution.mostCompetitive(nums=nums, k=k)
        print(f"answer: {answer},\texpected: {expected_value}")

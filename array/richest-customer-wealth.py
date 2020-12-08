"""
1672. Richest Customer Wealth
https://leetcode.com/contest/weekly-contest-217/problems/richest-customer-wealth/

User Accepted:4370
User Tried:4436
Total Accepted:4425
Total Submissions:4630
Difficulty:Easy

Result

#1
Date: 2020-12-08
Duration: 3m

34 / 34 test cases passed.
Status: Accepted
Runtime: 52 ms, faster than 79.38% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.2 MB, less than 58.66% of Python3 online submissions for Richest Customer Wealth.

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(personal_account) for personal_account in accounts])


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
    ]

    for test_case in test_cases:
        accounts, expected_value = test_case
        answer = solution.maximumWealth(accounts=accounts)
        print(f"answer: {answer},\texpected: {expected_value}")

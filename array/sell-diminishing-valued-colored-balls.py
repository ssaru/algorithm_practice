"""
1648. Sell Diminishing-Valued Colored Balls
https://leetcode.com/contest/weekly-contest-214/problems/sell-diminishing-valued-colored-balls/

User Accepted:607
User Tried:1653
Total Accepted:627
Total Submissions:3605
Difficulty:Medium

Result

#1
Date: 2020-11-14
Time Limit Exceeded
Duration: 60m

#2
Start time: 24:00
Pause time: 1:38
Duration: 100m

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
 

Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""
from typing import List
import math


class Solution:
    """
    # 1
    def maxProfit(self, inventory: List[int], orders: int) -> int:                
        s, ordered = 0, sorted(inventory, reverse=True) # O(NlogN)
        diff = [i-j for i, j in zip(ordered, ordered[1:] + [0])] # O(N)                        
                
        while orders > 0 :              
            idx, max_val = ordered.index(max(ordered)), max(ordered)
            if ordered[0] <= max_val:
                ordered[0], ordered[idx]= max_val, ordered[0]            
            s += ordered[0]
            ordered[0]  -= 1
            
            orders -= 1            
        return int(s % (1e+9 + 7))
    """

    # [2, 8, 4,10, 6]
    #
    # idx
    #  1, 2, 3, 4, 5
    # [2, 2, 2, 3, 1]-> diff
    # [2, 4, 6,12, 5]
    # 10, 8, 6, 4, 1 -> ordered

    # [2, 8, 4,10, 6] -> sort

    # 10, 8, 6, 4, 2 <- result of sort
    #  8, 6, 4, 2, 0 <- t+1 array

    #  2, 2, 2, 2, 2 -> diff

    # if orders = 10
    # ---------------|
    # 10,            |  10*1=10
    #  9,            |   9*1=9 ...19
    #  8, 8,         |   8*2=16
    #  7, 7,         |   7*2=14...30
    #  6, 6, 6       |   6*3=18
    #  5, 5, 5       |   5*3=15...33
    #  4, 4, 4, 4    |   4*4=16
    #  3, 3,|3|,3    |   3*4=12
    #  2, 2, 2, 2  2 |   2*4=8 ...36
    #  1, 1, 1, 1, 1 |   1*5=5 ...5

    # 2 + 8-3 + 4 + 10-3 + 6-3

    # 2 -> 2
    # 8 7 6 5 4 3 -> 33
    # 4 -> 4
    # 10 9 8 7 6 5 4 3 -> 52
    # 6 5 4 3 -> 18s
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # [10, 8, 6, 4, 1 ]
        # [9000000000] -> sum -> too large -> 가우스 합
        # (10+1) = 11
        # (2+9) = 11
        # (3+8) = 11
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        # 11 * 5
        if len(inventory) < 2:
            if orders == inventory[0]:
                s = (inventory[0] + 1) * (orders // 2)
            else:
                s = sum(range(inventory[0], inventory[0] - orders, -1))

            return s % ((10 ** 9) + 7)

        # [10, 8, 6, 4, 1 ]
        # [10, 8, 6, 4, 1 ]
        s, ordered = 0, sorted(inventory, reverse=True)  # O(NlogN)
        diff = [i - j for i, j in zip(ordered, ordered[1:] + [0])]  # O(N)

        for idx, diff_val in enumerate(diff, 1):
            decrese_orders = idx * diff_val

            if orders - decrese_orders <= 0:
                for _ in range(diff_val):
                    if orders > idx:
                        s += idx * ordered[idx - 1]
                        ordered[idx - 1] -= 1
                        orders -= idx
                    else:
                        for _ in range(orders):
                            s += ordered[idx - 1]
                        return s % ((10 ** 9) + 7)

            incremental = sum(
                [idx * val for val in range(ordered[idx - 1], ordered[idx - 1] - diff_val, -1)]
            )
            s += incremental
            orders -= decrese_orders


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 5], 4, 14),
        ([3, 5], 6, 19),
        ([2, 8, 4, 10, 6], 20, 110),
        ([1000000000], 1000000000, 21),
        ([76], 22, 1441),
        ([773160767], 252264991, 70267492),
    ]

    for test_case in test_cases:
        inventory = test_case[0]
        orders = test_case[1]
        expected_value = test_case[2]
        answer = solution.maxProfit(inventory=inventory, orders=orders)
        print(f"answer: {answer},\texpected: {expected_value}")

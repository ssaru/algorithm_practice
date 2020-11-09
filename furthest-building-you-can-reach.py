"""
1642. Furthest Building You Can Reach
https://leetcode.com/contest/weekly-contest-213/problems/furthest-building-you-can-reach/
User Accepted:1064
User Tried:2843
Total Accepted:1104
Total Submissions:5236
Difficulty:Medium

Result:
Date: 2011-11-10
time consumption: 120m

12 / 73 test cases passed.
Status: Time Limit Exceeded


You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""
import time
from typing import List

# date : 2020-11-10 1:23 AM
# time consumption: 120m
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 빌딩 높이 간의 diff를 구함
        diff = heights[1:]
        diff.append(0)

        for idx in range(len(heights)):
            diff[idx] = diff[idx] - heights[idx]

        positive_diff_list = [diff_val for diff_val in diff if diff_val > 0]
        if ladders > len(positive_diff_list):
            return len(heights) - 1

        if bricks > sum(positive_diff_list):
            return len(heights) - 1

        # bricks와 ladder가 혼합해서 주어진 경우
        # ladder 수에 맞춰 diff의 max position(top-k)들을 구한다.
        # 구한 max position까지 갈 수 있는지 확인한다.
        # 갈 수 없다면 diff의 제일 마지막 k를 제외한다.
        # 구한 max position까지 갈 수 있는지 확인한다.
        # 반복
        # brick의 합과 ladder의 개수가 diff의 양수 합을 넘어버린 경우
        # (예외 케이스를 생각하지 못함)
        descending_diff = sorted(diff, reverse=True)
        tmp_ladders, tmp_bricks = 1, 1
        while True:
            tmp_ladders = ladders
            tmp_bricks = bricks
            max_diff_pointer = []
            for idx in range(tmp_ladders):
                max_val = descending_diff[idx]
                idx = diff.index(max_val)
                max_diff_pointer.append(idx)

            max_diff_pointer.sort()

            for idx, diff_val in enumerate(diff):
                if idx in max_diff_pointer:
                    tmp_ladders -= 1
                    continue

                if diff_val > 0:
                    if (tmp_bricks - diff_val) > 0:
                        tmp_bricks -= diff_val
                    else:
                        tmp_bricks = 0
                        break

            if idx == (len(heights) - 1):
                return len(heights) - 1

            if (tmp_bricks == 0) and (tmp_ladders == 0):
                return idx

            pop_idx = descending_diff.index(diff[max_diff_pointer[-1]])
            descending_diff.pop(pop_idx)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([14, 3, 19, 3], 17, 0, 3),
        ([14, 3, 19, 3], 0, 3, 3),
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([17, 16, 5, 10, 10, 14, 7], 74, 6, 6),
        ([1, 13, 1, 1, 13, 5, 11, 11], 10, 8, 7),
    ]

    for test_case in test_cases:
        heights = test_case[0]
        bricks = test_case[1]
        ladders = test_case[2]
        expected_value = test_case[3]
        # print(f"height : {heights}")
        # print(f"bricks : {bricks}")
        # print(f"ladders : {ladders}")
        answer = solution.furthestBuilding(heights=heights, bricks=bricks, ladders=ladders)
        print(f"answer: {answer},\texpected: {expected_value}")

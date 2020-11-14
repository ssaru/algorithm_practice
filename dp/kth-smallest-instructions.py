"""
1643. Kth Smallest Instructions
https://leetcode.com/contest/weekly-contest-213/problems/kth-smallest-instructions/
User Accepted:694
User Tried:1587
Total Accepted:754
Total Submissions:2881
Difficulty:Hard

Result:
Date: 2020-11-10
time consumption: 310m

Not Solved

Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down. You are going to help Bob by providing instructions for him to reach destination.

The instructions are represented as a string, where each character is either:

'H', meaning move horizontally (go right), or
'V', meaning move vertically (go down).
Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.

However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically smallest instructions that will lead him to destination. k is 1-indexed.

Given an integer array destination and an integer k, return the kth lexicographically smallest instructions that will take Bob to destination.

 

Example 1:



Input: destination = [2,3], k = 1
Output: "HHHVV"
Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
Example 2:



Input: destination = [2,3], k = 2
Output: "HHVHV"
Example 3:



Input: destination = [2,3], k = 3
Output: "HHVVH"
 

Constraints:

destination.length == 2
1 <= row, column <= 15
1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​.
"""

# Date: 2020-11-10 11:00 AM
#                   16:51 PM
# Consumtion of time: 310m

from typing import List


class Solution:
    # 최단경로
    # 최단경로로 이동하는 인스트럭션 생성
    # 인스트럭션 스트링 정렬

    # 아래 규칙을 파악하면 kth가 몇번째 구간에 들어가는지 알 수 있음
    # V가 incresemental을 결정 -> (V - 1) (v=2, incresement=1, v=3, incresement=2, v=4, incresement=3)
    # H가 step 수를 결정 -> (h + 1) (h=2, step= 3|h=3, step= 4 | h=4, step=5)1개 증가할 때 마다 step이 증가 (H)

    # 기본적으로 재귀기반의 생성방식을 사용
    # 1-step  1 ["HHHVV",
    #
    # 2-step  2  "HHVHV",
    # sub-step   "HHVVH",
    #
    # 3-step  3  "HVHHV",
    # sub-step   "HVHVH",
    # sub-step   "HVVHH",
    #
    # 4-step: 4  "VHHHV",
    # sub-step   "VHHVH",
    # sub-step   "VHVHH",
    # sub-step   "VVHHH"]

    def recursive(
        self,
        result: List[str],
        horizontal_candidate: List[str],
        vertical_candidate: List[str],
        k: int,
    ):
        print(f"\nrecursive")
        print(f"horizontal_candidate: {horizontal_candidate}")
        print(f"vertical_candidate: {vertical_candidate}")
        print(f"k: {k}")
        print(f"----------")

        if k == 1:
            result.append("".join(horizontal_candidate))
            result.append("".join(vertical_candidate))

            return "".join(result)

        # incresemental과 전체 step 개수를 구하기 위해서 각 candidate의 길이를 구한다.
        length_h = len(horizontal_candidate)
        length_v = len(vertical_candidate)

        # incresemental과 전체 step 개수를 구한다.
        incresemental = length_v - 1
        whole_step = length_h + 2

        # 각 step별로 경우의 수를 리스트 형태로 만든다.
        if incresemental == 0:
            rows = [1 for i in range(1, (whole_step))]
        else:
            rows = [i for i in range(1, (whole_step) * incresemental, incresemental)]
        print(f"whole_step : {whole_step}")
        print(f"incresemental : {incresemental}")
        print(f"rows: {rows}")
        # 먼저 step에 있는 경우의 수를 빼주면서 몇 번째 step에서 인스트럭션 조합을 자세히 봐야하는지 들어간다.
        for idx, row in enumerate(rows, 1):
            print(f"step: {idx}")

            k -= row
            print(f"k : {k}")

            # k가 0이라면 현재 스탭에서 마지막꺼를 뽑겠다는 의미.
            if k == 0:
                print(f"k==0")
                # 현재 step의 위치를 확인한다.
                # 현재 step의 위치는 첫번째 V의 위치를 의미한다.
                # 첫번재 V가 나타나기 전까지 "H"로 채워준다.
                step = idx  # 이전 스텝
                print(f"step : {step}")
                for i in range(len(horizontal_candidate) - (step - 1)):
                    result.append(horizontal_candidate.pop(0))

                result.append(vertical_candidate.pop(0))
                print(f"inter : {result}")
                # 마지막 위치를 swap
                result.append("".join(horizontal_candidate))
                swap = result.pop(-1)
                result.append("".join(vertical_candidate))
                result.append(swap)

                return "".join(result)

            # 누적한 인스트럭션의 개수가 k보다 커지면 검사한다.
            elif k < 0:
                print(f"k<0")
                # k가 0보다 작아졌을 경우, 이전의 row값을 이용하여
                # 다음 재귀에서 사용할 수 있게한다.
                k = rows[idx - 1] + k
                print(f"recon k : {k}")
                step = idx  # 이전 스텝의 결과로 이번 스텝에서 음수이므로,,
                print(f"step : {step}")

                for i in range(len(horizontal_candidate) - (step - 1)):
                    result.append(horizontal_candidate.pop(0))

                result.append(vertical_candidate.pop(0))

                print(f"horizontal_candidate: {horizontal_candidate}")
                print(f"vertical_candidate: {vertical_candidate}")
                print(f"k : {k}")
                # 첫 V이후에는 destination이 줄어든 같은 문제이므로 재귀로 풀 수 있다.
                return (
                    self.recursive(
                        result=result,
                        horizontal_candidate=horizontal_candidate,
                        vertical_candidate=vertical_candidate,
                        k=k,
                    )
                    if k > 0
                    else "".join(result)
                )

        # 모두 통과했을 때는 k의 값이 제일 큰 것이므로, 앞을 모두 V로 뒤를 모두 H로 채우는 예외처리
        result.append("".join(vertical_candidate))
        result.append("".join(horizontal_candidate))

        return "".join(result)

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        print(f"==============")
        print(f"destination: {destination}")
        print(f"k: {k}")
        print(f"horizontal_candidate: {['H' for _ in range(destination[-1])]}")
        print(f"vertical_candidate: {['V' for _ in range(destination[0])]}")
        return self.recursive(
            result=[],
            horizontal_candidate=["H" for _ in range(destination[-1])],
            vertical_candidate=["V" for _ in range(destination[0])],
            k=k,
        )


# [2, 3] 3번째
# 1 step ["HHHVV"
# 2 step  "HHVHV", "HHVVH"

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3], 1, "HHHVV"),
        ([2, 3], 2, "HHVHV"),
        ([2, 3], 3, "HHVVH"),
        ([1, 1], 2, "VH"),
        ([1, 2], 2, "HVH"),
        ([2, 3], 2, "HHVHV"),
        ([1, 3], 3, "HVHH"),
        ([2, 2], 4, "VHHV"),
        ([3, 2], 9, "VVHVH"),
    ]

    for test_case in test_cases:
        destination = test_case[0]
        k = test_case[1]
        expected_value = test_case[2]
        answer = solution.kthSmallestPath(destination=destination, k=k)
        print(f"answer: {answer},\texpected: {expected_value}")

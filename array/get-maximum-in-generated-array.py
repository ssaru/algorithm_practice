"""
1646. Get Maximum in Generated Array
https://leetcode.com/problems/get-maximum-in-generated-array/

User Accepted:3822
User Tried:4087
Total Accepted:3940
Total Submissions:8533
Difficulty:Easy

Result:
#1
Date: 2020-11-12
Duration: 19m

101 / 101 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 14.2 MB

#2
Date: 2020-11-13
Duration: 220m

101 / 101 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 14.3 MB

You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.

Example 1:

Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
Example 2:

Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.
Example 3:

Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2. 

Constraints:

0 <= n <= 100
"""


class Solution:

    # #1
    # 생성 가능한 모든 리스트를 탐색 후에, max를 취함
    """
    def getMaximumGenerated(self, n: int) -> int:
        '''O(N)/O(N)'''
        if n < 1:
            return 0            
        
        # 기본적으로 [0, 1]을 가지고 시작할테니 탐색해야하는 수는 (n + 1) - 2
        num_arr = n + 1
        
        # 미리 list를 순회해서 빈 배열을 만들어두는 것보다, append하는게 더 이득
        answer = [0, 1]
        
        for i in range(2, num_arr):            
            idx, is_odd = int(i/2), i%2
            answer.append(answer[idx] + answer[idx+1] if is_odd else answer[idx])
        
        return max(answer)
    """

    """
    #2    
    # index / value
    #             v     0  1  2  3  4  5  6     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
    # 0 1 1 2 1 3 2 3 1 4  3  5  2  5  3  4  1  5  4  7  3  8  5  7  2  7  5  8  3  7  4  5  1
    #     | 1 |   3   |          7           |                      15                       |
    #         2       4                      8
    # 1개수  2     3              4                                   5
    #
    #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
    # 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64
    #  6  5  9  4 11  7 10  3 11 8  13  5 12  7  9  2  9  7 12  5 13  8 11  3 10  7 11  4  9  5  6  1
    #     v     v           v                       v
    #  6, 5, N, 4, N, N, N, 3, N, N, N, N, N, N, N  2

    #
    #
    #
    # 1, 2, 4, 8, 형태로 개수가 늘어나며 반복되는 패턴을 보인다 (계차수열)
    # NOTE, 1의 개수=1 + index
    #
    # {a_{n}} = [1, 3, 7, 15, ...]
    # {b_{n}} = [2, 4, 8, 16, ...]
    # n > 2, a_{n} = a_{1} + (b_{1}, ... ,b_{n-1})
    #
    # virtual index / real index / value
    # x x | 1 2 3  4  5  6
    # 0 1 | 2 3 4  5  6  7
    # 0 1 | 1 3 7 15  31 ...
    #
    # 전체 길의의 중간값은 2로 시작한다. 그 이후 반을 나누고 또 중앙값을 찾으면 3,...형태로 늘어난다.
    """

    def get_half_pod(self, pod: int):
        # left, right로 쪼개질 때까지 나눠야함
        half = [None for _ in range(pod // 2 + 1)]
        half[pod // 2] = 2

        left_idx = pod // 2
        left_val = 2

        while True:
            right_idx = left_idx
            left_idx = left_idx // 2
            left_val += 1

            half[left_idx] = left_val

            if left_idx == 0:
                break

            center_idx = (right_idx + left_idx) // 2
            half[center_idx] = half[right_idx] + half[left_idx]

        prev_idx = 0
        prev_val = half[0]

        while not all(half):
            for i in range(1, len(half)):
                is_cur_val_none = half[i] is not None
                is_diff_gt_1 = i - prev_idx > 1
                is_center_val_none = half[prev_idx + (i - prev_idx) // 2] is None
                if is_cur_val_none and is_diff_gt_1 and is_center_val_none:
                    half[prev_idx + (i - prev_idx) // 2] = half[i] + half[prev_idx]

                if half[i] is not None:
                    prev_idx = i
                    prev_val = half[i]

        return half

    def getMaximumGenerated(self, n: int) -> int:
        len_of_array = n + 1
        if n <= 2:
            return 0 if n < 1 else 1

        # 계차수열을 통해서 전체 길이를 확인하여 n이 어디에 해당하는지 찾는다.
        # n = 6
        accum, a0, index = 0, 1, 1
        while True:
            # progression of differences(`pod`)
            # (a_{n} = a_{1} + (b_{1}, ... ,b_{n-1}))
            pod = a0 + sum([2 ** i for i in range(1, index)])
            accum += pod

            #  index에 해당하는 전체 array 길이
            # 누적된 `pod` + 빠진 [0, 1] + 1의 개수
            len_of_accum_array = accum + 2 + (index + 1)

            if len_of_array <= len_of_accum_array:
                break
            else:
                index += 1
                prev_accum, prev_pod = accum, pod

        if pod <= 3:
            return 2 if pod == 1 else 3

        # array가 `pod` 어느 구간에 걸치는지 확인해야함
        # 1의 개수, 이전까지 누적된 `pod`값들, 빠진 [0,1]개수를 빼주면 인덱스를 찾을 수 있음
        index_in_pod = len_of_array - (prev_accum + 2 + (index + 1))

        prev_max = None
        if index_in_pod <= pod // 2:
            prev_max = max(self.get_half_pod(pod=prev_pod))

        cur_half = self.get_half_pod(pod=pod)
        slice_half = cur_half[: index_in_pod + 1] if index_in_pod < pod // 2 else cur_half
        cur_max = max(slice_half)

        return cur_max if prev_max is None else max([cur_max, prev_max])


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 3),
        (8, 3),
        (9, 4),
        (10, 4),
        (30, 8),
        (60, 13),
        (90, 21),
        (100, 21),
    ]

    for test_case in test_cases:
        n = test_case[0]
        expected_value = test_case[1]
        answer = solution.getMaximumGenerated(n=n)
        print(f"answer: {answer},\texpected: {expected_value}")

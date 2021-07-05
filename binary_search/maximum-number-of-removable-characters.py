"""
1898. Maximum Number of Removable Characters
https://leetcode.com/contest/weekly-contest-245/problems/maximum-number-of-removable-characters/

User Accepted:1383
User Tried:3643
Total Accepted:1433
Total Submissions:9511
Difficulty:Medium

66 / 66 test cases passed.
Status: Accepted
Runtime: 4340 ms
Memory Usage: 32.1 MB
Submitted: 0 minutes ago

You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

 

Example 1:

Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.
Example 2:

Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
Output: 1
Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
"abcd" is a subsequence of "abcddddd".
Example 3:

Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
Output: 0
Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
 

Constraints:

1 <= p.length <= s.length <= 105
0 <= removable.length < s.length
0 <= removable[i] < s.length
p is a subsequence of s.
s and p both consist of lowercase English letters.
The elements in removable are distinct.
"""
# Start time: 21:23
# Holding time: 22:01 (~38m)

# string s, p
# p in s


# 감상
# string match 문제처럼 보인다.
#
# 문제
# p in s 조건이 removable을 몇번까지 버티는가?
# 집합의 조건은 string이 아닌 character
# s = "abcacb"에서 집합은 {"a", "b", "c"}

# 방법론
# string match의 구간을 파악하고, removable이 해당 구간에 포함되기 시작하는게 몇번째인가 카운트 하면 될 것 같다.
# 1. 정규식으로 풀어도 될 것 같다.
# 2. 단순 매치로 풀어도 될 것 같고...?
# 3. counter로 풀어도 될 것 같다
#    counter의 keys에 p가 속하는가? -> counter가 Nlog(N)인 것으로 아는데, 그러면 removable하는 탐색까지 해야할 듯...
#    time complexity: NMO(log(M)) 다만 Mlog(M)이 단조감소...
# 4. set으로 풀어도 될 것 같다. -> 매번 set operation을 해서, in operation에 포함되는가? 
#    set operation의 time complexity는 몇일까? 중복제거일테니까?....
#    set은 hash table로 구현됨 build time complexity는 O(N)
#    set하고 subset check는 O(N)
#    time complexity: N * (O(N) + O(N)) -> c NO(N)
#    The complexity of B.issubset(A) is O(len(B)), assuming that e in A
# 5. counter와 list의 혼합으로 풀어보면 어떨까?...
#    counter를 해놓고.. (Nlog(N)), removable에 해당하는 key값을 차감하고, 차감이 완료되면 pop operation
#    그랬을 때, subset을 판별...
#
# !! 순서가 보장되야하는구나...
# 너무 왜 안되는 것에 대해서만 집중하고, 차이가 무엇인지 잘 살펴보지 않음
#
# 솔루션 참고
# 1. 탐색자체가 중간부터 탐색하는 방식(binary search)
# 2. 매칭 자체는 index를 넘어가면서 하는 단순 비교매칭
#
# test case
# "abcacb"
# "ab"
# [3,1,0]
#
# "abcbddddd"
# "abcd"
# [3,2,1,4,5,6]
#
# "abcab"
# "abc"
# [0,1,2,3,4]
#
#
# 

from typing import List

class Solution:
    """https://leetcode.com/problems/maximum-number-of-removable-characters/discuss/1270574/Python-Binary-Search"""

    def is_subsequence(self, s, p, removed) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if i not in removed and s[i] == p[j]:
                j += 1
            i += 1
        
        return j == len(p)

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        low, high, removed = 0, len(removable) - 1, set()        
        
        while low <= high:
            mid = low + int((high - low) // 2)
            removed = set(removable[:mid + 1])
            if self.is_subsequence(s, p, removed):
                low = mid + 1
            else:
                removed = set()
                high = mid - 1            
        
        # hi will be the index of the last usable element in removable
        # hi = -1 if none of the elements in removable is usable
        return high + 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [(["abcacb","ab",[3,1,0]], 2), 
                  (["abcbddddd", "abcd", [3,2,1,4,5,6]], 1), 
                  (["abcab", "abc", [0,1,2,3,4]], 0),
                  (["qlevcvgzfpryiqlwy", "qlecfqlw", [12,5]], 2)]

    for test_case in test_cases:
        s = test_case[0][0]
        p = test_case[0][1]
        removable = test_case[0][2]
        expected_value = test_case[1]
        answer = solution.maximumRemovals(s=s, p=p, removable=removable)
        print(f"answer: {answer},\texpected: {expected_value}")
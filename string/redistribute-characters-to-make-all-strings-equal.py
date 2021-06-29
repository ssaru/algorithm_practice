"""
1897. Redistribute Characters to Make All Strings Equal
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/submissions/

User Accepted:5364
User Tried:5855
Total Accepted:5477
Total Submissions:10279
Difficulty:Easy

Result:
Date: 2021-06-29
time consumption: 22 minute

179 / 179 test cases passed.

Status: Accepted
Runtime: 52 ms
Memory Usage: 14.5 MB

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

 

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.


"""
# 2021.06.29 21:51 Start
# 2021.06.29 22:13 End

# 문제 : List[str]으로 주어지는 `words`에 어떤 operation을 했을 때, words의 원소들이 모두
# 같은 값을 갖게끔 만들 수 있는가? 가능하다면 True, 불가능하다면 False

# 전제: 원소들은 모두 string

# operation을 생각하면 어떻게 풀어야할지 감이 안와...
# 결과만 가지고 생각해보자...

# 가설1: 결과적으로 모든 원소들이 같다면, char들의 카운터가 같지 않을까?
# 반례1. ["abca", "abca", "abca"] -> a: 6, b: 3, c: 3

# 가설2: 그렇다면, `len(words)`의 배수이지 않을까?
# 반례2: ... 배수말고 다른 접근이 있을까?

# Test case
# ["abc","aabc","bc"]
# ["ab", "a"]
# ["abcaabc", "aaa", "bc"]

from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Counter객체에 `["Hello", "World"]`가 들어가면, 캐릭터 기반으로 counting이 안될 것 같은데...
        # >> Counter({'Hello': 1})
        # "".join()을 통해서 풀어보자
        
        num_words = len(words)
        
        text = "".join(words) # 시간 복잡도가 어떻게 될까?
        char_count = Counter(text) # 시간 복잡도가 어떻게 될까?
        
        # O(N)
        for value in char_count.values():
            can_make_equal = True if ((value % num_words) == 0) else False
            
            if not can_make_equal: # 이 부분에서 로직 미스를 해서 테스트 케이스를 한방에 통과 못함
                return False
        
        # O(`"".join()` + `Counter` + N)
        return True

if __name__ == "__main__":
    solution = Solution()

    test_cases = [(["abc","aabc","bc"], True), 
                  (["ab", "a"], False), 
                  (["abcaabc", "aaa", "bc"], True)]

    for test_case in test_cases:
        words = test_case[0]
        expected_value = test_case[1]
        answer = solution.makeEqual(words=words)
        print(f"answer: {answer},\texpected: {expected_value}")
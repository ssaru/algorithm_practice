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
# !! 순서가 보장되야하는구나...
# 너무 왜 안되는 것에 대해서만 집중하고, 차이가 무엇인지 잘 살펴보지 않음
#

from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        set_p = set(p)
        list_s = list(s)                
        
        for cnt, remove_idx in enumerate(removable, 1):
            list_s.pop(remove_idx)
            set_s = set(list_s)            
            if not set_p.issubset(set_s):
                return cnt

if __name__ == "__main__":
    solution = Solution()

    test_cases = [(["abcacb","ab",[3,1,0]], 2), 
                  (["abcbddddd", "abcd", [3,2,1,4,5,6]], 1), 
                  (["abcab", "abc", [0,1,2,3,4]], 0)]

    for test_case in test_cases:
        s = test_case[0][0]
        p = test_case[0][1]
        removable = test_case[0][2]
        expected_value = test_case[1]
        answer = solution.maximumRemovals(s=s, p=p, removable=removable)
        print(f"answer: {answer},\texpected: {expected_value}")
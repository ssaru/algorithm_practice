"""
1656. Design an Ordered Stream
https://leetcode.com/contest/weekly-contest-215/problems/design-an-ordered-stream/

User Accepted:3072
User Tried:3277
Total Accepted:3111
Total Submissions:4041
Difficulty:Easy

Result

#1
Date: 2020-11-22
Accepted
Duration: 51m

There is a stream of n (id, value) pairs arriving in an arbitrary order, where id is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int id, String value) Inserts the pair (id, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
 

Example:



Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.
 

Constraints:

1 <= n <= 1000
1 <= id <= n
value.length == 5
value consists only of lowercase letters.
Each call to insert will have a unique id.
Exactly n calls will be made to insert.
"""

# Start
# Date: 2020-11-22
# Time: 19:41

# End
# Date: 2020-11-22
# Time: 20:30

# Duration: 51m

# Policy
#
# 1. id가 ptr과 같은 경우
#   1.1 반환을 위한 빈 리스트를 만든다.
#   1.2 현재 value값을 반환을 위한 리스트에 추가한다.
#   1.3 ptr을 한칸 이동하고, val이 있는지 확인한다.(val이 있는 경우 / val이 없는 경우로 분기)
#
#       1.3.1 val이 없으면 list를 반환하고 종료한다.
#       1.3.2 val이 있으면 이를 반환을 위한 리스트에 추가하고 ptr을 증가시킨다.
#       1.3.3 (1.2)로 이동한다.
#
# 2. id가 ptr보다 큰 경우
#   2.1 해당 array에 값을 넣고, 빈 리스트를 반환한다.
#
#
# Guarantee
# 1. ptr의 이전의 value은 모두 채워져있음을 보장한다.
#    - ptr은 id가 현재와 같을 경우 혹은 후속값들이 모두 채워져있을 때만 이동한다.
# 2. ptr이 머무르는 곳은 확실히 value가 비어있다는 것을 보장한다.
#    - 그렇지 않다면, 건너띄면서 ptr을 이동시켰을 것이다.
#
# 복잡도
# Worst Case: 첫 ptr을 제외하고 뒷부분은 모두 채워져있는 경우
#
# Space Complexity: O(n)
# 기본적으로 가지고있는 array: O(n)
# 포인터 값: O(1)
# 반환을 위해 일시적으로 만드는 리스트: O(n-1)
#
# Time Complexity
# (2)의 경우: O(1)
# (1)의 경우: O(n)
#   뒤의 array 요소를 삽입하는 비용: O(1)
#   마지막 value를 삽입하고 반환하는 비용: O(n-1)
#   따라서 전체 입력을 처리하는 복잡도는 O(n-1) + O(n-1)

from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.arr = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        idx = id - 1  # id는 1부터 시작하므로, array의 index와 맞추기 위해서, 1을 빼준다.
        self.arr[idx] = value

        if idx == self.ptr:
            ans = [value]
            for idx, val in enumerate(
                self.arr[self.ptr + 1 :], 1
            ):  # while을 쓰지 말기. (탈출조건이 하나이며, 단순한 구조라 상관없지만,,, 연습..!)
                if val is None:  # val가 None인 경우 break
                    self.ptr += idx  # 이전에 누적된 값을 모두 더해준다.
                    break
                ans.append(val)  # val가 None이 아닌 경우

            return ans

        else:  # 제약사항으로 id는 ptr보다 무조건 크다.
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

if __name__ == "__main__":

    solution = OrderedStream(5)
    test_cases = [
        (3, "ccccc", []),
        (1, "aaaaa", ["aaaaa"]),
        (2, "bbbbb", ["bbbbb", "ccccc"]),
        (5, "eeeee", []),
        (4, "ddddd", ["ddddd", "eeeee"]),
    ]

    for test_case in test_cases:
        idx = test_case[0]
        val = test_case[1]
        expected_value = test_case[2]
        answer = solution.insert(id=idx, value=val)
        print(f"answer: {answer},\texpected: {expected_value}")

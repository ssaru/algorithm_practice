"""
1640. Check Array Formation Through Concatenation
User Accepted:3115
User Tried:4606
Total Accepted:3183
Total Submissions:6150
Difficulty:Easy

Result:
82 / 82 test cases passed.

Status: Accepted
Runtime: 36 ms
Memory Usage: 14 MB
Distribution: 14.47% / 100%

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 
Your goal is to form arr by concatenating the arrays in pieces in any order. 
However, you are not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false 

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""

from typing import Union, List
import math

class Solution:
    
    def find_piece_idx(self, initial_element, pieces)->Union[int, bool]:
        for idx, piece in enumerate(pieces):
            if piece[0] == initial_element:
                return idx
        return None
    
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        if len(pieces) == 1:
            if len(arr) == 1:                
                return pieces[0] == arr
            else:                                
                assending = sorted(pieces[0])
                desending = sorted(pieces[0], reverse=True)
                is_assending = (assending == arr)
                is_desending = (desending == arr)
                
                if is_assending or is_desending:                    
                    return False
                
                is_contain_all_elements = True
                for element in pieces[0]:
                    is_contain_all_elements = is_contain_all_elements and (element in arr)
                if not is_contain_all_elements:                    
                    return False
                        
        initial_element, seek = arr[0], 0
        reconstruction = []
        while initial_element:
            piece_idx = self.find_piece_idx(initial_element=initial_element, pieces=pieces)
            if piece_idx == None:
                return False
            
            piece = pieces.pop(piece_idx)
            reconstruction.extend(piece)            
            seek += len(piece)

            if seek < len(arr):
                initial_element = arr[seek]
            else:                
                initial_element = False
        
        return reconstruction == arr
        
if __name__ == "__main__":
    solution = Solution()


    test_cases = [([85], [[85]], True),
                 ([15, 88], [[88], [15]], True),
                 ([49, 18, 16], [[16, 18, 49]], False),
                 ([91, 4, 64, 78], [[78], [4, 64], [91]], True),
                 ([1, 3, 5, 7], [[2, 4, 6, 8]], False),
                 ([1, 2, 3], [[2], [1, 3]], False)]
                 
    for test_case in test_cases:
        arr = test_case[0]
        pieces = test_case[1]
        expected_value = test_case[2]
        answer = solution.canFormArray(arr=arr, pieces=pieces)
        print(f"answer: {answer},\texpected: {expected_value}")
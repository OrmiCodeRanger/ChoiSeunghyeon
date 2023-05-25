"""https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution1:
    """
    brute force
    result => 3855ms
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# we can assume each input would have exactly one solution
        return [0, 0]


class Solution2:
    """
    `in`을 이용한 탐색
    Solution1과 같은 시간복잡도를 갖지만, 파이썬 내부적으로 일일이 비교하는 것보다
    빨리 실행된다고 한다.
    583ms
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:]
                        .index(complement) + (i + 1)]
        return []


class Solution3:
    """
    dict를 사용한 풀이
    70ms
    문제는.. 메모리 사용량이 어마무시하게 많다는거.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        for i, num in enumerate(nums):
            my_dict[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_dict and my_dict[complement] != i:
                return [i, my_dict[complement]]
        return []


class Solution4:
    """
    two pointers
    인덱스를 저장한 채로 정렬(tuple)
    89ms
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_nums = [(i, num) for i, num in enumerate(nums)]
        idx_nums.sort(key=lambda tup: tup[1])

        left, right = 0, len(nums) - 1

        while left < right:
            add = idx_nums[left][1] + idx_nums[right][1]
            if add < target:
                left += 1
            elif add == target:
                return [idx_nums[left][0], idx_nums[right][0]]
            else:
                right -= 1
        return []


solver = Solution4()

print(solver.twoSum([2, 7, 11, 15], 9))
# cannot happen
print(solver.twoSum([2, 7, 11, 15], 4))
# can happen
print(solver.twoSum([2, 2, 11, 15], 4))

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mid_1 = -m
        from_end_1 = - 1
        ind_2 = - 1

        while abs(mid_1) <= len(nums1) and abs(ind_2) <= len(nums2):
            if nums1[mid_1] < nums2[ind_2]:
                nums1[from_end_1] = nums2[ind_2]
                from_end_1 -= 1
                ind_2 -= 1
            else:
                nums1[from_end_1] = nums1[mid_1]
                from_end_1 -= 1
                mid_1 -= 1
        return nums1


nums1 = [11, 12, 13, 0, 0]
m = 3
nums2 = [5, 6]
n = 2


if __name__ == "__main__":
    ss = Solution()
    print(ss.merge(nums1, m, nums2, n))

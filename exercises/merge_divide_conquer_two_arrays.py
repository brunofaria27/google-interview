class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == '__main__':
    solution = Solution()
    desorded_array1 = [20, 4, 67, 12, 0, 0, 0, 0, 0]
    desorded_array2 = [40, 1, 0, 190, 4]
    sorted_array = solution.merge(desorded_array1, 3, desorded_array2, 4)
    print(sorted_array)

def merge_count_inversions(len_left, left, len_right, right):
    split_inversions = i = j = 0
    sorted_list = []
    while i < len_left and j < len_right:
        l = left[i]
        r = right[j]
        if l <= r:
            sorted_list.append(l)
            i += 1
        else:
            sorted_list.append(r)
            j += 1
            split_inversions += len_left - i
    while i < len_left:
        sorted_list.append(left[i])
        i += 1
    while j < len_right:
        sorted_list.append(right[j])
        j += 1            

    return split_inversions, sorted_list

class Solution(object):
    
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        split_inversions, sorted_list = merge_count_inversions(m, nums1, n, nums2)
        for i, v in enumerate(sorted_list):
            nums1[i] = v
          

class Solution:
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted([*nums1, *nums2])
        merged_array_len = len(merged_array)

        if merged_array_len == 0: return 0

        if merged_array_len % 2 == 1:
            index = int(merged_array_len/2)
            return merged_array[index]

        index = int(merged_array_len / 2)
        return (merged_array[index] + merged_array[index - 1])/2
    
    
    
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted([*nums1, *nums2])
        merged_array_len = len(merged_array)

        if merged_array_len == 0: return 0

        if merged_array_len % 2 == 1:
            index = int(merged_array_len/2)
            return merged_array[index]

        index = int(merged_array_len / 2)
        return (merged_array[index] + merged_array[index - 1])/2
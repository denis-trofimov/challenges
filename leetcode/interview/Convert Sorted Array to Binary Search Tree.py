# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def middle_node(nums):
            n = len(nums)
            if not n:
                return
            elif n == 1:
                return TreeNode(nums.pop())
            node = TreeNode(nums[n // 2])
            node.left = middle_node(nums[:n // 2])
            node.right = middle_node(nums[n // 2 + 1:])
            return node
        
        return middle_node(nums)
            

sol = Solution()
case_input = [-10,-3,0,5,9]
answer = sol.sortedArrayToBST(case_input)
print(answer)
expected = [0,-3,9,-10, None,5]
# assert expected == answer
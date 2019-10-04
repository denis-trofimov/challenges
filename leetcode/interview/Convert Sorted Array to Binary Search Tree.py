# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.val) + ',' + str(self.left) + ',' +  str(self.right)        


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def middle_node(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = middle_node(l, mid - 1)
            node.right = middle_node(mid + 1, r)
            return node
        
        return middle_node(0, len(nums) - 1)
        
if __name__ == "__main__":
    sol = Solution()
    case_input = [-10,-3,0,5,9]
    answer = sol.sortedArrayToBST(case_input)
    print(answer)
    expected = [0,-3,9,-10, None,5]
    # assert expected == answer
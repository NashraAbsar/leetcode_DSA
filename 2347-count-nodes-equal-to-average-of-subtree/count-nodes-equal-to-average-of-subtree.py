# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes_count = 0
        
        def calculate_subtree(node):
            if not node:
                return 0, 0  # (sum, count)
            
            # Post-order traversal: process left and right subtrees first
            left_sum, left_count = calculate_subtree(node.left)
            right_sum, right_count = calculate_subtree(node.right)
            
            # Aggregate current subtree properties
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check condition (integer division handles rounding down)
            if node.val == current_sum // current_count:
                self.matching_nodes_count += 1
                
            return current_sum, current_count

        calculate_subtree(root)
        return self.matching_nodes_count

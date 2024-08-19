class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largest_bst_subtree(root):
    def post_order(node):
        if not node:
            # Base case: An empty subtree is a valid BST with sum 0
            return (float('inf'), float('-inf'), 0, True)
        
        # Recursively traverse the left and right subtrees
        left_min, left_max, left_sum, left_is_bst = post_order(node.left)
        right_min, right_max, right_sum, right_is_bst = post_order(node.right)
        
        # Check if current subtree rooted at `node` is a valid BST
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            # It's a valid BST, so calculate the current sum
            current_sum = node.val + left_sum + right_sum
            # Update the maximum sum found so far
            largest_bst_subtree.max_sum = max(largest_bst_subtree.max_sum, current_sum)
            # Return the range and sum for the current BST subtree
            return (min(left_min, node.val), max(right_max, node.val), current_sum, True)
        
        # If it's not a BST, return invalid values for range and BST status
        return (float('-inf'), float('inf'), 0, False)
    
    # Initialize max_sum to track the largest BST sum
    largest_bst_subtree.max_sum = 0
    post_order(root)
    return largest_bst_subtree.max_sum

# Example Usage:

# Tree construction for the example: [1, 4, 3, 2, 4, 2, 5, null, null, null, null, null, null, 4, 6]
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(6)

# Finding the largest magical grove (BST)
result = largest_bst_subtree(root)
print(result)  # Output should be 20

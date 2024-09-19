class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,traversal):
            if not root:
                return
            traversal.append(root.val)
            preorder(root.left,traversal)
            preorder(root.right,traversal)
            return traversal
            
        return preorder(root,[])
         

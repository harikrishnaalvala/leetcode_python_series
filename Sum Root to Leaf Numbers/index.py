# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global leftSide
        leftSide=[]
        def depthFirstSearch(root,current_tring):
            if(root is None):
                pass
            elif(root.left is None and root.right is None):
                current_tring+=str(root.val)
                leftSide.append(current_tring)
            else:
                current_tring+=str(root.val)
                all_current_tring=current_tring[::]
                depthFirstSearch(root.left,current_tring)
                depthFirstSearch(root.right,all_current_tring)
        depthFirstSearch(root,"")
        result=0
        for i in leftSide:
            result+=int(i)
        return result

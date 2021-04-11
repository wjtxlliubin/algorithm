class Solution:
    def preorder(self, root):
        result = []
        def pre_order(root):
            if root:
                result.append(root.val)
                for node in root.children:
                    pre_order(node)
        pre_order(root)
        return result





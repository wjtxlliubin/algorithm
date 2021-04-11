class Solution:
    def preorderTraversal(self, root) :
        def dfs(cur):
            if not cur:
                return
            # 前序递归
            # res.append(cur.val)
            # dfs(cur.left)
            # dfs(cur.right)
            # # 中序递归
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)
            # # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)
        res = []
        dfs(root)
        return res

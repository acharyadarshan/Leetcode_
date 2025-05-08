from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue: 
            queue_len = len(queue)
            level = []
            for i in range(queue_len): 
                node = queue.popleft()
                if node: 
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level: 
                result.append(level)
        return result     
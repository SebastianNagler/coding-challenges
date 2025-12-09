# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def recursiveSerialize(node):
            if node is None:
                vals.append('N')
            else:
                vals.append(str(node.val))
                recursiveSerialize(node.left)
                recursiveSerialize(node.right)
        
        recursiveSerialize(root)
        return ','.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = deque(data.split(','))
        
        def recursiveDeserialize():
            val = vals.popleft()
            if val == 'N':
                return None
            else:
                node = TreeNode(int(val))
                node.left = recursiveDeserialize()
                node.right = recursiveDeserialize()
                return node
            
        return recursiveDeserialize()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
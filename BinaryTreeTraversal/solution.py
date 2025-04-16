class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


# Pre-order traversal
def pre_order(node: Node):
    output = []
    if not isinstance(node, Node):
        return []
    _pre_order(node, output)
    return output

def _pre_order(node: Node, output: list):
    output.append(node.data)
    if node.left:
        _pre_order(node.left, output)
    if node.right:
        _pre_order(node.right, output)
    return output

# In-order traversal
def in_order(node):
    if not isinstance(node, Node):
        return []
    output = []
    _in_order(node, output)
    return output

def _in_order(node: Node, output: list):
    if node.left:
        _in_order(node.left, output)
    output.append(node.data)
    if node.right:
        _in_order(node.right, output)

# Post-order traversal
def post_order(node):
    if not isinstance(node, Node):
        return []
    output = []
    _in_order(node, output)
    return output

def _post_order(node: Node, output: list):
    if node.right:
        _in_order(node.right, output)
    if node.left:
        _in_order(node.left, output)
    output.append(node.data)

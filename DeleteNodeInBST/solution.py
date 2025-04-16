class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not isinstance(node, Node):
        return []
    output = []

    level = [node]
    while level:
        output.extend(map(lambda x: x.value, level))

        children = []
        for member in level:
            if member.left:
                children.append(member.left)
            if member.right:
                children.append(member.right)
        level = children

    return output

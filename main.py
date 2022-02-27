class Tree:
    def __init__(self, value: str, left, right):
        self.value = value
        self.l = left
        self.r = right


t = Tree('A', Tree('B', Tree('X', Tree('E', None, None), Tree('M', None, None)), Tree('S', None, None)),
            Tree('W', Tree('T', Tree('P', None, None), Tree('N', None, None)), Tree('C', Tree('H', None, None), None)))


def traverse(tree: Tree, path: list, paths: []):
    path.append(tree.value)
    paths.append(path.copy())
    if tree.l:
        traverse(tree.l, path, paths)
    if tree.r:
        traverse(tree.r, path, paths)
    path.pop()
    return paths


print(traverse(tree=t, path=[], paths=[]))

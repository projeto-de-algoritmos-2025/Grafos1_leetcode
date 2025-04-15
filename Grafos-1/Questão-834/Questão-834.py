from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        res = [0] * n
        count = [1] * n

        def postorder(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    postorder(neighbor, node)
                    count[node] += count[neighbor]
                    res[node] += res[neighbor] + count[neighbor]

        def preorder(node, parent):
            for neighbor in tree[node]:
                if neighbor != parent:
                    res[neighbor] = res[node] - count[neighbor] + (n - count[neighbor])
                    preorder(neighbor, node)

        postorder(0, -1)
        preorder(0, -1)
        return res

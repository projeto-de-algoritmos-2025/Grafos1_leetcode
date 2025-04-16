from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1 << n) - 1

        queue = deque()
        seen = set()

        for i in range(n):
            start_node = i
            start_mask = 1 << start_node
            start_dist = 0

            queue.append((start_node, start_mask, start_dist))
            seen.add((start_node, start_mask))

        while queue:
            node, visited, dist = queue.popleft()

            current_node = node
            current_mask = visited
            current_dist = dist

            if current_mask == all_visited:
                return current_dist

            for neighbor in graph[current_node]:
                next_bit = 1 << neighbor
                next_mask = current_mask | next_bit
                state = (neighbor, next_mask)

                was_seen = state in seen
                if not was_seen:
                    seen.add(state)
                    next_dist = current_dist + 1
                    queue.append((neighbor, next_mask, next_dist))

        return -1

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:

        minDegree = -1
        for node1 in range(1, n+1):
            neighbours = []
            for node2 in range(1, n+1):
                if node1 != node2:
                    if [node1, node2] in edges or [node2, node1] in edges:
                        neighbours.append(node2)

            for neighbour1 in neighbours:
                for neighbour2 in neighbours:
                    if neighbour1 != neighbour2:
                        if [neighbour1, neighbour2] in edges or [neighbour2, neighbour1] in edges:
                            # node1, neighbour1 aand neighbour2 are a trio
                            degree = 0
                            for node in range(1, n+1):
                                if node != node1 and node != neighbour1 and node != neighbour2:
                                    if [node, node1] in edges or [node1, node] in edges:
                                        degree++
                                    if [node, neighbour1] in edges or [neighbour1, node] in edges:
                                        degree++
                                    if [node, neighbour2] in edges or [neighbour2, node] in edges:
                                        degree++
                            if minDegree == -1 or degree < minDegree:
                                minDegree = degree

        return minDegree

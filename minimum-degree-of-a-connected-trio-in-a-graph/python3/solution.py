from typing import List

class Solution:
    
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:

        nodes = range(1, n+1)

        minDegree = -1

        # def (a, b: int) -> bool:

        def isEdge(a, b: int) -> bool:
            return [a, b] in edges or [b, a] in edges

        def edgesConnectedToTrio(a, b, c: int) -> List[List[int]]:
            edgesConnectedToTrio = []
            for edge in edges:
                if edge[0] in (a, b, c) and edge[1] not in (a, b, c):
                    edgesConnectedToTrio.append(edge)
                if edge[1] in (a, b, c) and edge[0] not in (a, b, c):
                    edgesConnectedToTrio.append(edge)
            return edgesConnectedToTrio

        def neighboursOf(node: int) -> List[int]:
            neighbours = []
            for edge in edges:
                if edge[0] == node:                    
                    neighbours.append(edge[1])
                if edge[1] == node:                    
                    neighbours.append(edge[0])
            return neighbours
        
        for node in nodes:
            neighbours = neighboursOf(node)
            for neighbour1 in neighbours:
                for neighbour2 in neighbours:
                    if neighbour1 != neighbour2 and isEdge(neighbour1, neighbour2):
                        degree = len(edgesConnectedToTrio(node, neighbour1, neighbour2))
                        if minDegree == -1 or degree < minDegree:
                            minDegree = degree
                        
                
                
                
            
            
            
        
        return minDegree
        
        # for node1 in range(1, n+1):
        #     neighbours = []
        #     for node2 in range(1, n+1):
        #         if node1 != node2:
        #             if [node1, node2] in edges or [node2, node1] in edges:
        #                 neighbours.append(node2)

        #     for neighbour1 in neighbours:
        #         for neighbour2 in neighbours:
        #             if neighbour1 != neighbour2:
        #                 if [neighbour1, neighbour2] in edges or [neighbour2, neighbour1] in edges:
        #                     # node1, neighbour1 aand neighbour2 are a trio
        #                     degree = 0
        #                     for node in range(1, n+1):
        #                         if node != node1 and node != neighbour1 and node != neighbour2:
        #                             if [node, node1] in edges or [node1, node] in edges:
        #                                 degree += 1
        #                             if [node, neighbour1] in edges or [neighbour1, node] in edges:
        #                                 degree += 1
        #                             if [node, neighbour2] in edges or [neighbour2, node] in edges:
        #                                 degree += 1
        #                     if minDegree == -1 or degree < minDegree:
        #                         minDegree = degree

        # return minDegree

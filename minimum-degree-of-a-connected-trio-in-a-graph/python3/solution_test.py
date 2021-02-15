import pytest
from solution import Solution

def test_asd():
    solution = Solution()
    assert solution.minTrioDegree(0, []) == -1
    assert solution.minTrioDegree(1, []) == -1
    assert solution.minTrioDegree(1, []) == -1

    assert solution.minTrioDegree(6, [[1,2],[2,3],[3,4],[4,5],[5,6]]) == -1
    assert solution.minTrioDegree(6, [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]) == 3
    assert solution.minTrioDegree(6, [[1,2],[1,3],[2,3],[4,1],[5,2],[3,6]]) == 3
    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2],[4,1],[5,2],[3,6]]) == 3

    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2]]) == 0
    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2],[3,4]]) == 1
    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2],[2,4]]) == 1

    for i in range(0, 10):
        edges = [[2,1],[3,1],[3,2],[2,4],[2,6]]
        for edge in edges:
            edge[0] += i
            edge[1] += i
        assert solution.minTrioDegree(6 + i, edges) == 2    
    
    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2],[2,4],[1,5]]) == 2
    assert solution.minTrioDegree(6, [[2,1],[3,1],[3,2],[2,4],[1,5],[2,6]]) == 3

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if a != b and b != c and c != a:
                    edges = []
                    edges.append([a, b])
                    edges.append([b, c])
                    edges.append([c, a])
                    assert solution.minTrioDegree(20, edges) == 0

    for a in range(10, 20):
        for b in range(10, 20):
            for c in range(10, 20):
                if a != b and b != c and c != a:
                    edges = []
                    edges.append([1, 2])
                    edges.append([2, 3])
                    edges.append([3, 1])
                    for i in range(20, 100):
                        edges.append([1, i])
                    edges.append([a, b])
                    edges.append([b, c])
                    edges.append([c, a])
                    edges.append([c, 25])
                    edges.append([c, 26])
                    edges.append([c, 45])
                    edges.append([c, 99])                    
                    assert solution.minTrioDegree(100, edges) == 4
        
                                

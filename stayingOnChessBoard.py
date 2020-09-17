class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dirs = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
        m = [[1 for _ in range(N)] for _ in range(N)]
        while K != 0:
            next = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        next[i][j] += m[x][y]
                    next[i][j] /= 8
            m = next
            K -= 1
        return m[r][c]
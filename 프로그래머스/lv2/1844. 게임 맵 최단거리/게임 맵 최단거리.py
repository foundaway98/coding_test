from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append([x,y])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                xIdx = x + dx[i]
                yIdx = y + dy[i]
                if xIdx < 0 or xIdx >= n or yIdx < 0 or yIdx >= m:
                    continue
                if maps[xIdx][yIdx] == 0:
                    continue
                if maps[xIdx][yIdx] == 1:
                    maps[xIdx][yIdx] = maps[x][y] + 1
                    queue.append([xIdx,yIdx])
        

    bfs(0,0)
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
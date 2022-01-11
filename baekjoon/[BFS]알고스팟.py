
from collections import deque

gx, gy = map(int, input().split())  # x: 가로크기 /  y: 세로크기
graph = []
for i in range(gy):
    graph.append(list(map(int, input())))

x_move = [0, 0, -1, 1]  # 상하좌우
y_move = [1, -1, 0, 0]

start_queue = deque([[0, 0]])


def check(cy, cx):
    if 0 <= cy <= gy-1 and 0 <= cx <= gx - 1 and not visit[cy][cx]:
        return True
    return False


visit = [[False] * gx for _ in range(gy)]
answer = 0

while start_queue:
    pop_y, pop_x = start_queue.popleft()
    for i in range(4):
        next_y = pop_y + y_move[i]
        next_x = pop_x + x_move[i]
        if not check(next_y, next_x):
            continue

        visit[next_y][next_x] = True

        if graph[next_y][next_x] == 0:
            start_queue.appendleft([next_y, next_x])
        elif graph[next_y][next_x] == 1:
            start_queue.append([next_y, next_x])
        graph[next_y][next_x] = graph[pop_y][pop_x] + graph[next_y][next_x]

        if next_y == gy - 1 and next_x == gx - 1:
            answer = graph[next_y][next_x]
            break

print(answer)

if __name__ == "__main__":
    pass

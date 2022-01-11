from collections import deque

N, M = map(int, input().split())
Max = 100001

move_arry = [-1 for _ in range(Max)]
move_arry[N] = 0

path_queue = deque()
path_queue.append(N)

while path_queue:
    path = path_queue.popleft()

    if path == M:
        print(move_arry[M])
        break

    # -1 걷기 : +1
    if 0 <= path - 1 < Max and move_arry[path - 1] == -1:
        path_queue.append(path - 1)
        move_arry[path - 1] = move_arry[path] + 1

    # +1 걷기 : +1
    if 0 <= path + 1 < Max and move_arry[path + 1] == -1:
        path_queue.append(path + 1)
        move_arry[path + 1] = move_arry[path] + 1

    # 순간이동 : +0
    if 0 <= path * 2 < Max and move_arry[path * 2] == -1:
        path_queue.appendleft(path * 2)
        move_arry[path * 2] = move_arry[path]


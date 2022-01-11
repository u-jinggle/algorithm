from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


def solution(N, M, graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    start_queue = deque([[0, 0]])
    answer = 0

    while start_queue:
        y, x = start_queue.popleft()

        print(f"start y x : {y} {x}")
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if tx < 0 or tx > M - 1 or ty < 0 or ty > N - 1:
                continue

            if graph[ty][tx] == 1:
                graph[ty][tx] = graph[y][x] + 1
                print(f"ty tx  = {ty} {tx} / gragh[y][x]= {graph[y][x]}")
                start_queue.append([ty, tx])

                if [ty, tx] == [N - 1, M - 1]:
                    answer = graph[ty][tx]
                    break
    print("-------------------")

    return answer



# if __name__ == "__main__":
print(solution(N, M, graph))


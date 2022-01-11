from collections import deque

N, M = map(int, input().split())
Max = 100000

move_arry = [0 for _ in range(Max)]


def solution(start, dest):
    answer = 0

    path_queue = deque([start])
    done_list = []
    cnt = 0

    while 1:

        path = path_queue.popleft()
        print(f"path move : {move_arry[path]}")

        if path == dest:
            answer = move_arry[dest]
            break

        done_list.append(path)

        # -1 걷기 : +1
        if 0 <= path - 1 <= 100000 and move_arry[path-1] == 0:
            path_queue.append(path - 1)
            move_arry[path - 1] = move_arry[path] + 1

        # +1 걷기 : +1
        if 0 <= path + 1 <= 100000 and move_arry[path+1] == 0:
            path_queue.append(path + 1)
            move_arry[path + 1] = move_arry[path] + 1

        # 순간이동 : +0
        if 0 <= path * 2 <= 100000 and move_arry[path*2] == 0:
            path_queue.appendleft(path * 2)
            move_arry[path * 2] = move_arry[path]

        cnt = cnt+1
        print(f"done_list : {done_list}")
        print(f"path_queue : {path_queue}")
        print("-" * 20)
        print(cnt)

    return answer


if __name__ == "__main__":
    print(solution(N, M))

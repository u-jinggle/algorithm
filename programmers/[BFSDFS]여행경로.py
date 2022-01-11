from collections import deque


def find_end(tickets, start_queue):
    for idx, [s, e] in enumerate(tickets):
        if s == start_queue:
            return idx


def solution(tickets):
    # 각 티켓의 두번째 원소 기준으로 정렬
    # tickets.sort(key=lambda x: x[1])
    # 각 티켓을 출발지 기준 1차 정렬, 도착지 기준 2차 정렬 한다.
    tickets.sort(key=lambda x: (x[0], x[1]))


    # 출발지는 ICN으로 고정
    start_queue = deque(['ICN'])
    result_list = []

    while len(tickets) > 1:
        start = start_queue.pop()
        find_idx = find_end(tickets, start)
        start_queue.append(tickets[find_idx][1])
        result_list.append(tickets[find_idx][0])
        del tickets[find_idx]

    # 마지막 남은 티켓은 for문에서 돌지 못하고 빠져 나왔기 떄문에 출발지와 목적지를 모두 result list에 넣어준다
    result_list.append(tickets[0][0])
    result_list.append(tickets[0][1])

    answer = result_list
    return answer


if __name__ == "__main__":
    sample_data = []
    # sample_data.append([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    # sample_data.append([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    sample_data.append([["ICN", "BBB"], ["BBB", "CCC"], ["BBB", "DDD"], ["DDD", "BBB"]])

    for i in sample_data:
        s = solution(i)
        print(f"result: {s}")

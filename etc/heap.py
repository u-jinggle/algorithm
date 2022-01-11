import heapq


def heapsort_asc(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
        # heapq.heappush(h, (a, b)) ->  튜플 또는 리스트 (a, b)가 주어졌을때 순서는 무조건 a자리로 인해 정렬된다

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


def heapsort_desc(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


if __name__ == "__main__":
    result = heapsort_desc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)

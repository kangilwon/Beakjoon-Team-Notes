import heapq


def solution(scoville, k):
    hot = []
    for i in scoville:
        heapq.heappush(hot, i)

    cnt = 0
    while hot[0] < k:
        try:
            heapq.heappush(hot, heapq.heappop(hot) + (heapq.heappop(hot) * 2))
        except IndexError:
            return -1
        cnt += 1
    return cnt
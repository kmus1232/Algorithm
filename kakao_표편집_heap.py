import heapq

def solution(n, k, cmd):
    in_list = ['O' for _ in range(n)]
    min_heap = [i for i in range(k, n)]
    max_heap = [-i for i in range(k)]
    del_stack = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for c in cmd:
        if len(c) > 1:
            c, n = c.split()
            n = int(n)
            if c == 'U':
                for _ in range(n):
                    heapq.heappush(min_heap, -max_heap[0])
                    heapq.heappop(max_heap)
            else:
                for _ in range(n):
                    heapq.heappush(max_heap, -min_heap[0])
                    heapq.heappop(min_heap)
        else:
            if c == 'C':
                in_list[min_heap[0]] = 'X'
                del_stack.append(min_heap[0])
                heapq.heappop(min_heap)
                if not min_heap:
                    heapq.heappush(min_heap, -max_heap[0])
                    heapq.heappop(max_heap)
            else:
                e = del_stack.pop()
                in_list[e] = 'O'
                if e > min_heap[0]:
                    heapq.heappush(min_heap, e)
                else:
                    heapq.heappush(max_heap, -e)

    ans = ''.join(in_list)
    return ans
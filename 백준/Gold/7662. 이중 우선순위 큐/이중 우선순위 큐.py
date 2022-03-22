import sys
import heapq
input = sys.stdin.readline

T = int(input())
for tc in range(T) :
    k = int(input())
    ans = {}
    min_heap=[]
    max_heap=[]
    for j in range(k) :
        com,num = input().split()
        num = int(num)
        if com == 'I' :
            heapq.heappush(min_heap,num)
            heapq.heappush(max_heap,-num)
            if ans.get(num) == None :
                ans[num] = 1
            else :
                ans[num] += 1
        else :
            if num == -1 :
                while min_heap and not ans.get(min_heap[0]) :
                    heapq.heappop(min_heap)
                if min_heap :
                    ans[min_heap[0]] -= 1
                    if ans[min_heap[0]] == 0 :
                        del ans[min_heap[0]]
                    heapq.heappop(min_heap)
            else :
                while max_heap and not ans.get(-max_heap[0]) :
                    heapq.heappop(max_heap)
                if max_heap :
                    ans[-max_heap[0]] -= 1
                    if ans[-max_heap[0]] == 0 :
                        del ans[-max_heap[0]]
                    heapq.heappop(max_heap)
    while min_heap and not ans.get(min_heap[0]) :
        heapq.heappop(min_heap)
    while max_heap and not ans.get(-max_heap[0]) :
        heapq.heappop(max_heap)
    lst = list(ans.keys())
    if min_heap and max_heap :
        print(max(lst), end=' ')
        print(min(lst))
    else :
        print("EMPTY")
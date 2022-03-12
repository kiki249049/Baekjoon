import sys
input = sys.stdin.readline

def insert(num) :
    max_heap.append(num)
    idx = len(max_heap)-1
    while idx != 1 and max_heap[idx] > max_heap[idx//2] :
        max_heap[idx], max_heap[idx//2] = max_heap[idx//2], max_heap[idx]
        idx = idx // 2
    return
def delete(heap) :
    heap[1], heap[-1] = heap[-1], heap[1]
    print(heap.pop())
    parent = 1
    while True :
        child = parent * 2
        if child+1 < len(heap) and heap[child] < heap[child+1] :
            child += 1
        if child >= len(heap) or heap[child] < heap[parent] :
            break
        heap[child],heap[parent] = heap[parent], heap[child]
        parent = child




N=int(input())
max_heap=[0]

for i in range(N) :
    val = int(input())
    if val != 0 :
        insert(val)
    else :
        if len(max_heap) == 1 :
            print(0)
        else :
            delete(max_heap)
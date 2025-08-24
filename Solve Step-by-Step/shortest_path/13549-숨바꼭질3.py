import heapq

def dijkstra(start,end):
    time = [float('inf')] * (100001)
    time[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:

        now_time, now_node = heapq.heappop(heap)
        if now_node == end:
            return time[end]
                
        for cost,next_node in [(0,now_node*2),(1,now_node+1),(1,now_node-1)]:
            if 0 <= next_node <= 100000:
                if time[next_node] > now_time + cost:
                    time[next_node] = now_time + cost
                    heapq.heappush(heap,(time[next_node],next_node))



N,K = map(int,input().split())
result = dijkstra(N,K)
print(result)


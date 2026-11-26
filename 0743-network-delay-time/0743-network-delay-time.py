class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1,n+1)}

        for u,v,w in times:
            graph[u].append((v,w))

        dist = [float('inf')]*(n+1)
        dist[k] = 0

        heap = [(0,k)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if curr_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

                    heapq.heappush(heap, (new_dist, neighbor))

        ans = max(dist[1:])

        if ans == float('inf'):
            return -1
        
        return ans
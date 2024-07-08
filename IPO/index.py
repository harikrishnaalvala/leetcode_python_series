class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projectIndex = 0
        totalProjects = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        maxProfitHeap = []
        for currentProject in range(k):
            while projectIndex < totalProjects and projects[projectIndex][0] <= w:
                heapq.heappush(maxProfitHeap, -projects[projectIndex][1])
                projectIndex += 1
            if not maxProfitHeap:
                return w            
            w -= heapq.heappop(maxProfitHeap)
        return w

class Solution(object):
    def maxEvents(self, events):
        events.sort()
        n=len(events)
        time =1
        attended=0
        pos=0
        minheap=[]

        while pos<n or minheap:

            if not minheap:
                time=max(time, events[pos][0])
            
            while pos<n and events[pos][0]==time:
                heapq.heappush(minheap, events[pos][1])
                pos+=1
            
            while minheap and minheap[0]<time:
                heapq.heappop(minheap)
            
            if minheap:
                heapq.heappop(minheap)
                attended+=1
            time+=1

        return attended
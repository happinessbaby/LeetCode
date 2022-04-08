class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
#         #[100, 50, 25]
#         h = []
#         i = 0
#         j = len(stones)-1
#         while len(h)>1:
#             if i<len(stones)-1:
#                 heapq.heappush(h, stones[i]-stones[i+1])
#                 i==2
#             else:
#                 heapq.heappush(h, h[j]-h[j-1])
#                 j+=1
#             return h
        while len(stones)>1:
            diff = stones[0]-stones[1]
            print(len(stones))
            if diff!=0:
                stones.append(diff)
            stones.pop(0)
            stones.pop(0)
            stones.sort(reverse=True)
        return stones[0] if len(stones)==1 else 0
            
            
        # def recurse(h, stones, idx):
        #     if idx == len(stones)-1
        #         return
        #     diff = stones[idx]-stones[idx+1]
        #     heapq.heappush(h, diff)
        #     #stones.append(diff)
        #     recurse(h, stones, idx+2)
        # recurse([], stones, 0)
            
            
                           
                
    
            
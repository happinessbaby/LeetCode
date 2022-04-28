class Solution:
    
    def __init__(self):
        self.visited = {}
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        all_idx = range(len(s))
        adj_memo = defaultdict(list)
        substring_idx = []
        # make an adjacency graph
        for pair in pairs:
            adj_memo[pair[0]].append(pair[1])
            adj_memo[pair[1]].append(pair[0])
        start = 0
        leftover_idx = all_idx
        # dfs to get all connected components
        while len(leftover_idx)>0:
            start = leftover_idx[0]
            self.dfs(start, adj_memo)
            substring_idx.append(sorted(list(self.visited.keys())))
            leftover_idx = [x for x in all_idx if x not in self.visited]
            all_idx = leftover_idx
            self.visited = {}
        # sorted_substring_idx = sorted(substring_idx, key=lambda x:x[0])
        # print(sorted_substring_idx)
        result = [" " for i in range(len(s))]
        for idx_list in substring_idx:
            substring_list = sorted([s[x] for x in idx_list])
            i=0
            for idx in idx_list:
                result[idx]=substring_list[i]
                i+=1
        return "".join(result)
            
            
            
    def dfs(self, idx, adj_memo):
        self.visited[idx]=True
        for n in adj_memo[idx]:
            if n not in self.visited:
                self.dfs(n, adj_memo)
        
        
        
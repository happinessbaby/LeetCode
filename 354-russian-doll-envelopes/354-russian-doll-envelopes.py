class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=lambda x: (-x[0], x[1]))
        # LIS = [1]*len(sorted_envelopes)
        # for i in range(len(sorted_envelopes)-1, -1, -1):
        #     for j in range(i+1, len(sorted_envelopes)):
        #         if sorted_envelopes[i][1]>sorted_envelopes[j][1]:
        #             LIS[i] = max(LIS[i], 1+LIS[j])
        # return max(LIS)
        LDS = []
        size = 0
        for (w, h) in sorted_envelopes:
            if not LDS or h<LDS[-1]:
                LDS.append(h)
                size+=1
            else:
                l, r = 0, size
                #binary search for where to insert the replacing element
                while l<r:
                    m = l+(r-l)//2
                    if LDS[m]>h:
                        l = m+1
                    else:
                        r = m
                LDS[l]=h
        return size
                
            
                
                

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # masks = set()
        # for i in range(2**k):
        #     submask = ""
        #     for j in range(k):
        #         if (i&1<<j):
        #             submask+="1"
        #         else:
        #             submask+="0"
        #     masks.add(submask)
        # string_set = set()
        # for i in range(len(s)-k+1):
        #     string_set.add(s[i:k+i])
        # return True if len(masks.difference(string_set))==0 else False
        return len(set([s[i:i+k] for i in range(len(s)-k+1)]))==pow(2, k)
            
            
                
            
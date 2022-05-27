class Solution:
    def numberOfSteps(self, num: int) -> int:
        #every bit-wise right shift of 1 divides number by 2
        count = 0
        while num!=0:
            if (num&1)==0:
                #divide num by 2
                num = num>>1
                count+=1
            else:
                num-=1
                count+=1
        return count

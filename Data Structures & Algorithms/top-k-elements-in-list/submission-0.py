class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=list(Counter(nums).items())
        out=sorted(counter,key=lambda x:-x[1])
        return [x[0] for x in out[:k]]
        
        
        

        
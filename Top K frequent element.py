class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in range(leng(nums)):
            freq[i]=freq.get(i,0)+1
        
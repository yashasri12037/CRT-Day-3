class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k=k%n
        b=[0]*n
        for i in range(n):
            b[(i+k)%n]=nums[i]
        for i in range(n):
            nums[i]=b[i]
        return nums
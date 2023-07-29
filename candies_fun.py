"""Date: July 29 2023
Author : Neha Jalan
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies."""
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        arr = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= self.returnMax(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr
    @staticmethod
    def returnMax(candies):
        max = candies[0]
        for i in range(len(candies)):
            if max < candies[i]:
                max = candies[i]
        return max
def main():
    li =[2,3,5,1,3]
    d = Solution()
    print(d.kidsWithCandies(li,3))

if __name__ == '__main__':
    main()
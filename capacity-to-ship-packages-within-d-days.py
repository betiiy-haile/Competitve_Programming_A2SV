class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity = max(weights)
        maxCapacity = sum(weights)
        ans = maxCapacity

        def checkCapacity(mid):
            ships ,currCap = 1, mid
            for weight in weights:
                if currCap - weight < 0:
                    ships += 1
                    currCap = mid
                currCap -= weight
            return ships <= days

        while minCapacity <= maxCapacity:
            mid = minCapacity + (maxCapacity-minCapacity)//2
            if checkCapacity(mid):
                ans = min(ans, mid)
                maxCapacity = mid - 1
            else:
                minCapacity = mid + 1

        return ans
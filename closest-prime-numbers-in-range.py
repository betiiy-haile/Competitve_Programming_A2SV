class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        primes = []
        for num in range(left, right + 1):
            if num != 1 and self.isPrime(num):
                primes.append(num)
            if len(primes) >= 2 and primes[-1] -  primes[-2] <= 2:
                return primes[-2] , primes[-1]

        if len(primes) > 1:
            ans[0] = primes[0]
            ans[1] = primes[1]
        for i in range(len(primes) - 1):
            if ans[1] - ans[0] <= 2:
                break
            if ans[1] - ans[0] > primes[i + 1] - primes[i]:
                ans[0] = primes[i]
                ans[1] = primes[i + 1]
            
        return ans

    def isPrime(self, num):
        d = 2
        while d * d <= num:
            if num % d == 0:
                return False 
            d += 1
        return True
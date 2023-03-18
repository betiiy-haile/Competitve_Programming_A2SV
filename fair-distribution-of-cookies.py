class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0]*k
        cookies.sort(reverse=True)
        unfairness = float("inf")
        def backtrack(i):
            nonlocal unfairness
            if i == len(cookies):
                unfairness = min(unfairness, max(arr))
                return
            if unfairness < max(arr):
                return
            for j in range(k):
                arr[j] += cookies[i]
                backtrack(i+1)
                arr[j] -= cookies[i] 

        backtrack(0)
        return unfairness
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)  # Count the frequency of each character

        ans = 0
        seen = set()

        for freq in count.values():
            while freq in seen and freq > 0:
                freq -= 1
                ans += 1

            seen.add(freq)

        return ans
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = defaultdict(list)
        for idx, group in enumerate(groupSizes):
            count[group].append(idx)

        count = dict(sorted(count.items()))

        ans = []
        for key, value in count.items():
            for i in range(0, len(value), key):
                ans.append(value[i:i+key])

        return ans
        
n = int(input())
sources = set()
sinks = set()
for i in range(n):
    nums = list(map(int, input().split(" ")))
    for j in range(n):
        if nums[j] == 1:
            sources.add(j+1)
            sinks.add(i+1)

source = []
sink = []
for i in range(n):
    if i+1 not in sources:
        source.append(i+1)
    if i+1 not in sinks:
        sink.append(i+1)

print(len(source), *source)
print(len(sink), *sink)
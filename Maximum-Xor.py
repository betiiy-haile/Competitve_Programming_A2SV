L, R = map(int, input().split(" "))
XOR = L ^ R
 
setBit = 0
while XOR:
    setBit += 1
    XOR >>= 1
 
maxXor = 0
X = 1
while setBit:
    maxXor += X
    X <<= 1
    setBit -= 1
 
print(maxXor)
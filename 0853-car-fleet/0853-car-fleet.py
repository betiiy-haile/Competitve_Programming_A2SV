class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []                
        positionSpeed = [[p,s] for p,s in zip(position, speed)]
        positionSpeed.sort(reverse=True)
        
        for p,s in positionSpeed:
            time = (target - p) / s
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
                            
        return len(stack)
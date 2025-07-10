class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                sTemp, sIdx = stack.pop()
                res[sIdx] = (i - sIdx)
            stack.append([t, i])
        return res 

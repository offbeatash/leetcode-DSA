class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        indices = []

        for i, temp in enumerate(temperatures):
            while indices and temperatures[i] > temperatures[indices[-1]]:
                prev_index = indices.pop()
                answer[prev_index] = i - prev_index
            indices.append(i)

        return answer
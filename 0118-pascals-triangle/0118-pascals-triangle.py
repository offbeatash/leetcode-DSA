class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1]

            if result:
                prev = result[-1]

                for j in range(len(prev)-1):
                    row.append(prev[j] + prev[j+1])

                row.append(1)

            result.append(row)

        return result
class Grid:
    def __init__(self, n, occupancies):
        self._n = n
        self._occupancies = occupancies
        self._rows = [[False]*self._n for _ in range(self._n)]
        for row, col in self._occupancies:
            self._rows[row][col] = True

    
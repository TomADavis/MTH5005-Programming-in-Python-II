class Grid:
    def __init__(self, n, occupancies):
        self._n = n
        self._occupancies = occupancies
        self._rows = [[False]*self._n for _ in range(self._n)]
        for row, col in self._occupancies:
            self._rows[row][col] = True
    
    def __repr__(self):
        return f"Grid(n={self._n}, occupancies={self._occupancies})"
    
    def __str__(self):
        occupied = "⬛"
        vacant = "⬜"
        lines = []

        for row in self._rows:           
            lines.append(" ".join(occupied if cell else vacant for cell in row))
        return "\n".join(lines)
    
    def get_occupancies(self):
        return self._occupancies.copy()
    
    def get_row(self, i):
        return self._rows[i].copy()
    
    def add_occupancy(self, coords:tuple[int, int]):
        row, col = coords
        if coords in self.get_occupancies():
            pass
        else:
            self._rows[row][col] = True

    def del_occupancy(self, coords):
        row, col = coords
        if coords in self.get_occupancies():
            self._rows[row][col] = False
        
        

    

x = Grid(n = 3, occupancies = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)])

print(x.__repr__())  
print(x.__str__())

x.del_occupancy([0, 1])

print("\n")
print(x.__str__())
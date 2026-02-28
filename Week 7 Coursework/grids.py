class Grid:
    """
    A class to represent an n x n grid with occupied / vacant cells.

    To construct an instance, call the constructor Grid with parameters
    n and occupancies, e.g.

    Grid(n=..., occupancies=[(r1, c1), (r2, c2), ...])
    """

    def __init__(self, n, occupancies):
        """
        This method initialises instances of Grid

        Attributes include:
            _n (int): Grid Dimension.
            _occupancies (list[tuple[int, int]]): List of occupied coordinates (row, col).
            _rows (list[list[bool]]): Boolean grid representation
        """
        self._n = n
        self._occupancies = occupancies
        self._rows = [[False]*self._n for _ in range(self._n)]
        for row, col in self._occupancies:
            self._rows[row][col] = True
    
    def __repr__(self):
        """
        This method returns a string representation suitable for debugging.
        
        The returned string includes the grid size and the list of occupancies and its read-out can be 
        copied-and-pasted into a new cell that upon execution, will create a copy of it.
        """
        return f"Grid(n={self._n}, occupancies={self._occupancies})"
    
    def __str__(self):
        """
        This method returns a human readable drawing of the grid.

        The grid is drawn row-by-row, with cells separated by a single space.

        Key:
            Vacant  = "□"
            Occupied = "■"
        """
        vacant = "□"
        occupied = "■"
        lines = []

        for row in self._rows:           
            lines.append(" ".join(occupied if cell else vacant for cell in row))
        return "\n".join(lines)
    
    def get_occupancies(self):
        """
        This method returns a copy of the occupancy list.

        The copy is returned so that external code cannot directly modify the
        internal occupancy list.
        """
        return self._occupancies.copy()
    
    def get_row(self, i):
        """
        This method returns a copy of row i of the grid.

        The returned value is a list of booleans of length n.
        """
        return self._rows[i].copy()
    
    def add_occupancy(self, coords:tuple[int, int]):
        """
        This method marks a cell as occupied.

            If the cell is currently vacant, it is set to True in _rows and the
            coordinate is appended to _occupancies.  
            
            If the cell is already occupied, no changes are made.
        """
        row, col = coords
        if not self._rows[row][col]:
            self._rows[row][col] = True
            self._occupancies.append(coords)

    def del_occupancy(self, coords):
        """
        This method marks a cell as vacant.

            If the cell is currently occupied, it is set to False in _rows and the
            coordinate is removed from _occupancies.  
            
            If the cell is already vacant, no changes are made.
        """
        row, col = coords
        if self._rows[row][col]:
            self._rows[row][col] = False
            self._occupancies.remove(coords)

    def copy(self):
        """
        This method returns a new Grid with the same size and occupancies.

        The occupancy list is copied so that the new Grid has its own list object.
        """
        return Grid(self._n, self._occupancies.copy())
    
    def v_reflected(self):
        """
        This method returns the vertical reflection of the grid.

        A vertical reflection flips the grid top-to-bottom.
        """
        n = self._n
        new_occupancies = []

        for r, row in enumerate(self._rows):
            for c, cell in enumerate(row):
                if cell:
                    new_occupancies.append((n - 1 - r, c))

        return Grid(n, new_occupancies)
    
    def h_reflected(self):
        """
        This method returns the horizontal reflection of the grid.

        A horizontal reflection flips the grid left-to-right.
        """
        n = self._n
        new_occupancies = []

        for r, row in enumerate(self._rows):
            for c, cell in enumerate(row):
                if cell:
                    new_occupancies.append((r, n - 1 - c))
        
        return Grid(n, new_occupancies)
    
    def rotated(self):
        """
        This method returns the 90 degree clockwise rotation of the grid.
        """
        n = self._n
        new_occupancies = []

        for r, row in enumerate(self._rows):
            for c, cell in enumerate(row):
                if cell:
                    new_occupancies.append((c, n - 1 - r))
        
        return Grid(n, new_occupancies)
    
    def __add__(self, h):
        """
        This method adds two grids of the same size using XOR logic.

        A cell is occupied in the output if it is occupied in exactly one of the
        input grids.

        If the two grids have different sizes, an error message is printed and
        None is returned.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None
        
        n = self._n
        new_occupancies = []

        for r in range(n):
            for c in range(n):
                if self._rows[r][c] ^ h._rows[r][c]:
                    new_occupancies.append((r, c))

        return Grid(n, new_occupancies)
        
    def __eq__(self, h):
        """
        This method checks whether two grids are equal.

        Two grids are equal if they have the same size and the same occupied
        coordinates (order does not matter).

        If the two grids have different sizes, an error message is printed and
        None is returned.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if sorted(self._occupancies) == sorted(h._occupancies):      ##### UNCLEAR? what should be returned from this function if anything, would you like a print statement or a Bool
            return True
        else:
            return False

    def __le__(self, h):
        """
        This method checks whether the occupancies of this grid are a subset of h.

        If every occupied coordinate in this grid also appears in h, this method
        returns True, otherwise False.

        If the two grids have different sizes, an error message is printed and
        None is returned.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if set(self._occupancies).issubset(h._occupancies):         ##### UNCLEAR? what should be returned from this function if anything, would you like a print statement or a Bool
            return True
        
        else:
            return False
        
    def __ge__(self, h):
        """
        This method checks whether the occupancies of this grid are a superset of h.

        If every occupied coordinate in h also appears in this grid, this method
        returns True, otherwise False.

        If the two grids have different sizes, an error message is printed and
        None is returned.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if set(h._occupancies).issubset(self._occupancies):         ##### UNCLEAR? what should be returned from this function if anything, would you like a print statement or a Bool
            return True
        
        else:
            return False


    
if __name__ == "__main__":
    x = Grid(n = 3, occupancies = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)])

    print("\nInstance:")
    print(x.__str__())
    print("\nVertical Reflection:")
    print(x.v_reflected())
    print("\nRotation 90 degrees Clockwise: ")
    print(x.rotated())
"""
Core grid classes and helper functions for the until package.

This module provides classes for representing square occupancy grids and for enforcing additional 
structural conditions on them.

The base class, Grid, stores an n x n grid whose cells are either occupied or vacant. It supports 
string representation, copying, reflections, rotation, comparison operations, and XOR-style addition.

Additional Specialised Subclasses
-------------------------------------

UniformGrid
    A grid in which every row and every column contains exactly two occupied cells.

NTiL
    A grid satisfying the No Three in Line [NTiL] condition.

UNTiL
    A grid satisfying the NTiL and the uniformity condition.

The helper function til is used to test whether three points lie on a single straight line.
"""

from itertools import combinations
from .exceptions import OccupancyError, OperatorError

class Grid:
    """
    A class to represent an n x n grid with occupied and vacant cells.

    Parameters
    -------------
    n: int
        Side length of the grid.

    occupancies: list[tuple[int, int]]
        Coordinates of the occupied cells given as (row, column) pairs.

    To construct an instance, call the constructor Grid with parameters
    n and occupancies, for example

    Grid(n=..., occupancies=[(r1, c1), (r2, c2), ...])

    Attributes
    -------------
    occupancies: list[tuple[int, int]]
        A copy of the occupied coordinates of the grid.

    Methods
    ----------
    get_row(i)
        Return a copy of row i.

    add_occupancy(coords)
        Occupy a vacant cell at the given coordinates.

    del_occupancy(coords)
        Vacate an occupied cell at the given coordinates.

    copy()
        Return a copy of the grid.

    v_reflected()
        Return the vertical reflection of the grid.

    h_reflected()
        Return the horizontal reflection of the grid.

    rotated()
        Return the clockwise rotation of the grid.

    __str__()
        Return a human-readable string representation of the grid.

    __repr__()
        Return a constructor-style representation of the grid.

    __add__(h)
        Return the XOR-style sum of this grid and h.

    __eq__(h)
        Test whether this grid is equal to h.

    __le__(h)
        Test whether this grid is a subset of h.

    __ge__(h)
        Test whether this grid is a superset of h.
    """

    def __init__(self, n, occupancies):
        """
        This method initialises instances of Grid

        Parameters
        -------------
        n: int
            Side length of the grid.

        occupancies: list[tuple[int, int]]
            Coordinates of the occupied cells given as (row, column) pairs.

        Attributes
        -------------
            _n: int
                Grid Dimension.

            _occupancies: list[tuple[int, int]]
                List of occupied coordinates (row, col).

            _rows: list[list[bool]]
                Boolean grid representation.

        Notes
        --------
        The occupancy information is stored both as a coordinate list and as a Boolean matrix
        for convenient access.
        """
        self._n = n
        self._occupancies = occupancies.copy()
        self._rows = [[False]*self._n for _ in range(self._n)]
        for row, col in self._occupancies:
            self._rows[row][col] = True
    
    def __repr__(self):
        """
        This method returns a string representation suitable for debugging.
        
        The returned string includes the grid size and the list of occupancies and its read-out can be 
        copied-and-pasted into a new cell that upon execution, will create a copy of it.
        """
        class_name = self.__class__.__name__

        return f"{class_name}(n={self._n}, occupancies={self._occupancies})"
    
    def __str__(self):
        """
        This method returns a human readable drawing of the grid.

        The grid is drawn row-by-row, with cells separated by a single space.

        Key
        ------
            Vacant  = "□"
            Occupied = "■"
        """
        vacant = "□"
        occupied = "■"
        lines = []

        for row in self._rows:           
            lines.append(" ".join(occupied if cell else vacant for cell in row))
        return "\n".join(lines)
    
    @property
    def occupancies(self):
        """
        This method returns a copy of the occupancy list.

        Returns
        ----------
        list[tuple[int, int]]
            Copy of the occupied coordinates.

        Notes
        --------
        The copy is returned so that external code cannot directly modify the
        internal occupancy list.
        """
        return self._occupancies.copy()
    
    def get_row(self, i):
        """
        This method returns a copy of row i of the grid.

        Parameters
        -------------
        i: int
            Row index.
        
        Returns
        ----------
        list[bool]
            Copy of row i, where True indicates an occupied cell and False a vacant cell.
        """
        return self._rows[i].copy()
    
    def add_occupancy(self, coords:tuple[int, int]):
        """
        This method marks a cell as occupied.

        Parameters
        -------------
        coords: tuple[int, int]
            Coordinate of the cell to occupy.

        Raises
        ---------
        OccupancyError
            If the specified cell is already occupied.
        
        Notes
        --------
            If the cell is currently vacant, it is set to True in _rows and the
            coordinate is appended to _occupancies.  
                
            If the cell is already occupied, raises an OccupancyError.
        """
        row, col = coords

        if not self._rows[row][col]:
            self._rows[row][col] = True
            self._occupancies.append(coords)

        else:
            raise OccupancyError('Box at given coordinates already occupied.')

    def del_occupancy(self, coords:tuple[int, int]):
        """
        This method marks a cell as vacant.

        Parameters
        -------------
        coords: tuple[int, int]
            Coordinate of the cell to vacate.

        Raises
        ---------
        OccupancyError
            If the specified cell is already vacant.
        
        Notes
        --------
            If the cell is currently occupied, it is set to False in _rows and the
            coordinate is removed from _occupancies.  
            
            If the cell is already vacant, raises an OccupancyError.
        """
        row, col = coords
        if self._rows[row][col]:
            self._rows[row][col] = False
            self._occupancies.remove(coords)
        
        else:
            raise OccupancyError('Box at given coordinates already vacant.')

    def copy(self):
        """
        This method returns a new Grid with the same size and occupancies.

        Returns
        ----------
        Grid
            A new Grid instance with the same size and occupied coordinates.

        Notes
        --------
        The occupancy list is copied so that the new Grid has its own list object.
        """
        return Grid(self._n, self._occupancies.copy())
    
    def v_reflected(self):
        """
        This method returns the vertical reflection of the grid.

        Returns
        ----------
        Grid
            New grid obtained by reflecting the current grid top to bottom.
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

        Returns
        ----------
        Grid
            New grid obtained by reflecting the current grid left to right.
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

        Returns
        ----------
        Grid
            New grid obtained by rotating the current grid clockwise.
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
        Return the XOR-style sum of two grids of the same size.

        A cell is occupied in the result if and only if it is occupied in exactly 
        one of the two input grids.

        Parameters
        -------------
        h: Grid
            Grid to combine with this grid.

        Returns
        ----------
        Grid
            New grid representing the cellwise exclusive-or of the two inputs.
        
        Raises
        ---------
        OperatorError
            If the two grids do not have the same side length.
        """
        if self._n != h._n:
            raise OperatorError('Error: Grids must be of matching size.')
        
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

        Parameters
        -------------
        h: Grid
            Grid to compare with this grid.

        Returns
        ----------
        bool: None
            True if the grids have the same size and the same occupied coordinates.
            
            False if the sizes match but the occupancies differ.

            None if the grid sizes do not match.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if sorted(self._occupancies) == sorted(h._occupancies):      
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

        Parameters
        -------------
        h: Grid
            Grid to compare with this grid.

        Returns
        ----------
        bool: None
            True if every occupied cell in this grid is also occupied in h.

            False if not.

            None if the grid sizes do not match.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if set(self._occupancies).issubset(h._occupancies):         
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

        Parameters
        -------------
        h: Grid
            Grid to compare with this grid.

        Returns
        ----------
        bool: None
            True if every occupied cell in h is also occupied in this grid.

            False if not.

            None if the grid sizes do not match.
        """
        if self._n != h._n:
            print('Error: Grids must be of matching size.')
            return None

        if set(h._occupancies).issubset(self._occupancies):         
            return True
        
        else:
            return False
        
class UniformGrid(Grid):
    """
    Represent a uniform occupancy grid.
    
    A UniformGrid is a Grid in which every row and every column contains 
    exactly two occupied cells.
    
    Instances are validated when they are created, and occupancies cannot 
    later be added or removed directly.

    Parameters
    -------------
        n: int
            Side length of the grid.
            
        occupancies: list[tuple[int, int]]
            Coordinates of occupied cells.

    Attributes
    -------------
    occupancies : list[tuple[int, int]]
        A copy of the occupied coordinates of the grid.

    Methods
    ----------
    add_occupancy(coords)
        Raise an error, since direct occupancy changes may break uniformity.

    del_occupancy(coords)
        Raise an error, since direct occupancy changes may break uniformity.

    commutator(coords1, coords2)
        Perform a commutator move on two occupied cells.

    Notes
    --------
    UniformGrid inherits the remaining public methods of Grid.
    """

    def __init__(self, n, occupancies):
        """
        Initialises a uniform grid and validates its row and column counts
        
        Parameters
        -------------
        n: int
            Side length of the grid.
            
        occupancies: list[tuple[int, int]]
            Coordinates of occupied cells.
        
        Raises
        ---------
        OccupancyError
            If any row or any column does not contain exactly two occupied cells.
        """
        Grid.__init__(self, n, occupancies)  

        for row in self._rows:
            if row.count(True) != 2:
                raise OccupancyError('Each row and column must have exactly two occupancies.')

        for c in range(self._n):
            col_count = 0
            for r in range(self._n):
                if self._rows[r][c]:
                    col_count += 1
            
            if col_count != 2:
                raise OccupancyError('Each row and column must have exactly two occupancies.')

    def add_occupancy(self, coords):
        """
        Disallow direct addition of occupancies.

        Raises
        ---------
        OperatorError
            Always, because adding a single occupancy could break the uniformity condition.
        """
        raise OperatorError('Cannot add/delete occupancies to instances of UniformGrid.')
    
    def del_occupancy(self, coords):
        """
        Disallow direct deletion of occupancies.
        
        Raises
        ---------
        OperatorError
            Always, because deleting a single occupancy could break the uniformity condition.
        """
        raise OperatorError('Cannot add/delete occupancies to instances of UniformGrid.')

    def commutator(self, coords1: tuple[int, int], coords2: tuple[int, int]):
        """
        Perform a commutator move on two occupied cells.
        
        Given two occupied coordinates (x1, y1) and (x2, y2), this method removes those occupancies
        and places occupancies at the opposite corners (x1, y2) and (x2, y1).

        Parameters
        -------------
        coords1: tuple[int, int]
            First occupied coordinate.
        
        coords2: tuple[int, int]
            Second occupied coordinate.

        Raises
        ---------
        OccupancyError
            If either input coordinate is not occupied, or if either target coordinate is already occupied.

        Notes
        --------
        The operation is performed in place. It preserves the property that
        each affected row and column still contains the same number of
        occupancies as before.
        """
        x1, y1 = coords1
        x2, y2 = coords2

        if (not self._rows[x1][y1]) or (not self._rows[x2][y2]):
            raise OccupancyError('Both input coordinates must be occupied.')
        
        if self._rows[x1][y2] or self._rows[x2][y1]:
            raise OccupancyError('Both target coordinates must be vacant.')

        self._rows[x1][y1] = False
        self._rows[x2][y2] = False
        self._rows[x1][y2] = True
        self._rows[x2][y1] = True

        self._occupancies.remove((x1, y1))
        self._occupancies.remove((x2, y2))
        self._occupancies.append((x1, y2))
        self._occupancies.append((x2, y1))

def til(pt1, pt2, pt3):
    """
    Accept three points (as tuples of length 2) and 
    return True if they lie in a straight line,
    False otherwise.
    """
    if (pt1 == pt2) or (pt2 == pt3) or (pt3 == pt1):
        return False
    return (pt1[0] - pt2[0]) * (pt2[1] - pt3[1]) == (pt2[0] - pt3[0]) * (pt1[1] - pt2[1])

class NTiL(Grid):
    """
    Represent a No Three in Line (NTiL) occupancy grid.

    An NTiL grid is a Grid in which no three occupied cells lie on the 
    same straight line. The condition is checked on construction and also
    when a new occupancy is added.

    Parameters
    -------------
    n : int
        Side length of the grid.

    occupancies : list[tuple[int, int]]
        Coordinates of the occupied cells.

    Attributes
    -------------
    occupancies : list[tuple[int, int]]
        A copy of the occupied coordinates of the grid.

    Methods
    ----------
    add_occupancy(coords)
        Add an occupancy only if doing so preserves the NTiL condition.

    Notes
    --------
    NTiL inherits the remaining public methods of Grid.
    """
    def __init__(self, n, occupancies):
        """
        Initialise a No Three in Line grid and validate its occupancies.
        
        Parameters
        -------------
        n: int
            Side length of the grid.

        occupancies: list[tuple[int, int]]
            Coordinates of occupied cells.

        Raises
        ---------
        OccupancyError
            If any three occupied cells lie on a straight line.
        """
        Grid.__init__(self, n, occupancies)

        for pt1, pt2, pt3 in combinations(self._occupancies, 3):
            if til(pt1, pt2, pt3):
                raise OccupancyError('Cannot have three occupancies in a straight line.')
    
    def add_occupancy(self, coords: tuple[int, int]):
        """
        Add an occupancy while preserving the NTiL property

        Parameters
        -------------
        coords: tuple[int, int]
            Coordinate of the cell to occupy
        
        Raises
        ---------
        OccupancyError
            If the cell is already occupied, or if adding it would create
            three occupied cells in a straight line.

        """
        row, col = coords

        if self._rows[row][col]:
            raise OccupancyError('Box at given coordinates already occupied.')
        
        for pt1, pt2 in combinations(self._occupancies, 2):
            if til(pt1, pt2, coords):
                raise OccupancyError('Cannot have three occupancies in a straight line.')

        self._rows[row][col] = True
        self._occupancies.append(coords)

class UNTiL(UniformGrid, NTiL):
    """
    Represent a grid satisfying both uniformity and NTiL.

    A UNTiL grid inherits the row and column uniformity condition from UniformGrid and the NTiL
    condition from NTiL. Validation is delegated through the inherited initialiser chain.

    Parameters
    -------------
    n : int
        Side length of the grid.

    occupancies : list[tuple[int, int]]
        Coordinates of the occupied cells.

    Attributes
    -------------
    occupancies : list[tuple[int, int]]
        A copy of the occupied coordinates of the grid.

    Notes
    --------
    UNTiL inherits its public methods from UniformGrid and NTiL.
    """
    def __init__(self, n, occupancies):
        """
        Initialise a grid satisfying both specialised conditions

        Parameters
        -------------
        n: int
            Side length of grid.

        occupancies: list[tuple[int, int]]
            Coordinates of occupied cells.
        """
        UniformGrid.__init__(self, n, occupancies)
        NTiL.__init__(self, n, occupancies)



"""
Custom Error Exception Classes for the package until.

This module defines the exceptions raised uniquely by the grid classes when either...

    1. Occupancy change is invalid.

    2. Grid operation cannot be carried out.

Classes
----------
OccupancyError
    Raised when an attempted change to cell occupancies is invalid.

OperatorError
    Raised when an operation on one or more grids is not permitted.
"""

class OccupancyError(Exception):
    """
    Exception raised for invalid occupancy updates.
    
    This exception is used when a method tries to...
    
        1. Occupy an already occupied cell.

        2. Vacate an already vacant cell.

        3. Construct an invalid specialised grid.

        4. Break another occupancy-based rule.
    """
    def __init__(self, msg):
        """
        Initialise the exception with a descriptive error message.

        Parameters
        -------------
        msg: str
            Explanation of the error
        """
        super().__init__(msg)

class OperatorError(Exception):
    """
    Exception raised for invalid or unsupported grid operations.

    This exception is used when...
    
        1. An operation is not allowed for a particular grid type.
         
        2. Two grids cannot be combined because their sizes do not match.
    """
    def __init__(self, msg):
        """
        Initialise the exception with a descriptive error message.

        Parameters
        -------------
        msg: str
            Explanation of the error
        """
        super().__init__(msg)


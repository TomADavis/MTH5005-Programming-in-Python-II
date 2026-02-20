"""
Define a class Point that can be used to model points in a two-dimensional space,
and use this class to derive structures modelling shapes in this space.

The following objects are defined here:

    Classes
    -------
    Point:
        A class to represent points in two-dimensional space.

    Circle:
        A class to represent circles in two-dimensional space.

    Rectangle:
        A class to represent rectangles in two-dimensional space.

    Modules
    -------
    math:
        The math module of the Python Standard Library.
"""

import math

class Point:
    """
    A class to represent points in two-dimensional space.
    
    Attributes
    ----------
    x: int/float
        The point's x coordinate.

    y: int/float
        The point's y coordinate.

    Methods
    -------
    distance(pt)
        Return the distance between the instance and some
        other point, pt.

    rotated(centre=(0, 0), angle=0)
        Return point given by rotating instance anticlockwise 
        about given centre through specified angle.
    """
    def __init__(self, x = 0, y = 0):
        """
        Parameters
        ----------
        x: int/float, optional
            The point's x coordinate.

        y: int/float, optional
            The point's y coordinate.
        """
        if isinstance(x, (int, float)):
            self.x = x
            self.y = y
        elif isinstance(x, (list, tuple, range, Point)):
            self.x = x[0]
            self.y = x[1]
    def __repr__(self):
        """
        Returns
        -------
        str
            Read-out of the point data.
        """
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        """
        Returns
        -------
        str
            Print-out of the point data.
        """
        return f'({self.x}, {self.y})'
    def __getitem__(self, i):
        """
        Parameters
        ----------
        i: int
            Index of requested element.
            
        Returns
        -------
        int/float
            Value of coordinate at corresponding index.
        """
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
    def __add__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        Point
            Point given by element-wise sum of instance and pt.
        """
        return Point(self.x + pt.x, self.y + pt.y)
    def __neg__(self):
        """
        Returns
        -------
        Point
            Point given by element-wise negation of instance.
        """
        return Point(-self.x, -self.y)
    def __sub__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        Point
            Point given by element-wise difference of instance and pt.
        """
        return self + (-pt)
    def __eq__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            True, if both coordinates of instance and pt match in value.
            False, otherwise.
        """
        return (self.x == pt.x) and (self.y == pt.y)
    def __neq__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            False, if both coordinates of instance and pt match in value.
            True, otherwise.
        """
        return not self == pt
    def __lt__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            True, if both coordinates of instance are less-than 
            respective coordinates of pt.  False, otherwise.
        """
        return (self.x < pt.x) and (self.y < pt.y)
    def __le__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            True, if both coordinates of instance are less-than-or-equal-to
            respective coordinates of pt.  False, otherwise.
        """
        return (self.x <= pt.x) and (self.y <= pt.y)
    def __gt__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            True, if both coordinates of instance are greater-than 
            respective coordinates of pt.  False, otherwise.
        """
        return (self.x > pt.x) and (self.y > pt.y)
    def __ge__(self, pt):
        """
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        bool
            True, if both coordinates of instance are greater-than-or-equal-to
            respective coordinates of pt.  False, otherwise.
        """
        return (self.x >= pt.x) and (self.y >= pt.y)
    def distance(self, pt):
        """Return the Euclidean distance between instance and pt.
        
        Parameters
        ----------
        pt: Point
            
        Returns
        -------
        float
            Distance between instance and pt.
        """
        return ((self.x - pt.x)**2 + (self.y - pt.y)**2)**0.5
    def rotated(self, centre = (0, 0), angle = 0):
        """Return the point obtained by rotating instance anticlockwise
        about given centre through specified angle.
        
        Parameters
        ----------
        centre: Point
            Centre about which instance should be rotated.
        angle: int/float
            Angle through which instance should be rotated (in radians).
            
        Returns
        -------
        Point
            Point obtained through anticlockwise rotation.
        """
        t = self - Point(centre)
        r = Point(math.cos(angle)*t.x - math.sin(angle)*t.y,
                  math.sin(angle)*t.x + math.cos(angle)*t.y)
        return r + Point(centre)

class Circle:
    """
    A class to represent circles in two-dimensional space.
    
    Attributes
    ----------
    centre: Point

    radius: int/float

    Methods
    -------
    circumference()
        Return the length of the perimeter of the instance.

    area()
        Return the area bounded by the instance.

    includes(pt)
        Return a boolean corresponding to whether the point
        pt lies inside the region defined by the instance.

    intersects(circ)
        Return a boolean corresponding to whether a circle
        has a non-empty intersection with the instance.
    """
    def __init__(self, centre = Point(0, 0), radius = 1):
        """
        Parameters
        ----------
        centre: list/range/tuple/Point, optional

        radius: int/float, optional
        """
        self.centre = Point(centre)
        self.radius = radius
    def __repr__(self):
        """
        Returns
        -------
        str
            Read-out of the circle data.
        """
        return f'Circle(centre = {self.centre}, radius = {self.radius})'
    def __str__(self):
        """
        Returns
        -------
        str
            Print-out of the circle data.
        """
        return f'Circle:\tCentre: {self.centre}\n        Radius: {self.radius}'
    def circumference(self):
        """
        Returns
        -------
        float
            Value of the length of the perimeter of the instance.
        """
        return 2*math.pi*self.radius
    def area(self):
        """
        Returns
        -------
        float
            Value of the area of the region defined by the instance.
        """
        return math.pi*(self.radius)**2
    def includes(self, pt):
        """
        Parameters
        ----------
        pt: Point
            Point to be tested for inclusion within the region
            defined by the instance.
            
        Returns
        -------
        bool
            True, if point pt lies within the region defined by the instance.
            False, otherwise.
        """
        return self.centre.distance(pt) <= self.radius
    def intersects(self, circ):
        """
        Parameters
        ----------
        circ: Circle
            Circle to be tested for intersection with instance.
            
        Returns
        -------
        bool
            True, if circ has non-empty intersection with instance.
            False, otherwise.
        """
        return self.centre.distance(circ.centre) <= self.radius + circ.radius

class Rectangle:
    """
    A class to represent rectangles in two-dimensional space.
    
    Attributes
    ----------
    centre: Point
        Coordinates of centre point.

    length: int/float
        Length of horizontal dimension of rectangle.

    width: int/float
        Length of vertical dimension of rectangle.

    corners: dict
        Dictionary with keys labelling the corner points
        relative to the rectangle's centre (e.g. 'top-right',
        'bottom-left'), with matching values given by the
        Point instances corresponding to the corner described
        by each label.

    Methods
    -------
    get_centre()
        Getter method for centre attribute.
        
    get_length()
        Getter method for length attribute.
        
    get_width()
        Setter method for width attribute.
        
    get_corners()
        Getter method for corners attribute.
        
    set_centre()
        Setter method for centre attribute.
        
    set_length()
        Setter method for length attribute.
        
    set_width()
        Getter method for width attribute.
        
    perimeter()
        Return the length of the perimeter of the instance.

    area()
        Return the area bounded by the instance.

    includes(pt)
        Return a boolean corresponding to whether the point
        pt lies inside the region defined by the instance.

    intersects(rctg)
        Return a boolean corresponding to whether a rectangle
        has a non-empty intersection with the instance.
    """
    def __init__(self, centre = Point(0, 0), length = 1, width = 1):
        """
        Parameters
        ----------
        centre: list/range/tuple/Point, optional

        radius: int/float, optional

        width: int/float, optional
        """
        self._centre = Point(centre)
        self._length = length
        self._width = width
        self._corners = {'top-right'    : self._centre + Point( self._length/2,  self._width/2),
                         'top-left'     : self._centre + Point(-self._length/2,  self._width/2),
                         'bottom-right' : self._centre + Point( self._length/2, -self._width/2),
                         'bottom-left'  : self._centre + Point(-self._length/2, -self._width/2)}
    def __repr__(self):
        """
        Returns
        -------
        str
            Read-out of the rectangle data.
        """
        return f'Rectangle(centre = {self._centre}, length = {self._length}, width = {self._width})'
    def __str__(self):
        """
        Returns
        -------
        str
            Print-out of the circle data.
        """
        return f'Rectangle:\tCentre Point:\t{self._centre}\n\t\tLength:\t{self._length}\n\t\tWidth:\t{self._width}'
    def get_centre(self):
        """
        Returns
        -------
        Point
            Point instance of the centre of the instance.
        """
        return Point(self._centre.x, self._centre.y)
    def get_length(self):
        """
        Returns
        -------
        int/float
            Length of the horizontal dimension of the instance.
        """
        return self._length
    def get_width(self):
        """
        Returns
        -------
        int/float
            Length of the vertical dimension of the instance.
        """
        return self._width
    def get_corners(self):
        """
        Returns
        -------
        dict
            Dictionary of labelled corner points.
        """
        return self._corners.copy()
    def set_centre(self, centre):
        """
        Parameters
        ----------
        centre (Point)
            Point describing the location to which the instance should be moved.
        """
        self._centre = Point(centre)
        self._corners = {'top-right'    : self._centre + Point( self._length/2,  self._width/2),
                         'top-left'     : self._centre + Point(-self._length/2,  self._width/2),
                         'bottom-right' : self._centre + Point( self._length/2, -self._width/2),
                         'bottom-left'  : self._centre + Point(-self._length/2, -self._width/2)}
    def set_length(self, length):
        """
        Parameters
        ----------
        length (int/float)
            Value of the desired length of horizontal dimension of instance.
        """
        self._length = length
        self._corners = {'top-right'    : self._centre + Point( self._length/2,  self._width/2),
                         'top-left'     : self._centre + Point(-self._length/2,  self._width/2),
                         'bottom-right' : self._centre + Point( self._length/2, -self._width/2),
                         'bottom-left'  : self._centre + Point(-self._length/2, -self._width/2)}
    def set_width(self, width):
        """
        Parameters
        ----------
        width (int/float)
            Value of the desired length of vertical dimension of instance.
        """
        self._width = width
        self._corners = {'top-right'    : self._centre + Point( self._length/2,  self._width/2),
                         'top-left'     : self._centre + Point(-self._length/2,  self._width/2),
                         'bottom-right' : self._centre + Point( self._length/2, -self._width/2),
                         'bottom-left'  : self._centre + Point(-self._length/2, -self._width/2)}
    def perimeter(self):
        """
        Returns
        -------
        int/float
            Value of the length of the perimter of the instance.
        """
        return 2*(self._length + self._width)
    def area(self):
        """
        Returns
        -------
        int/float
            Value of the area of the region defined by the instance.
        """
        return self._length*self._width
    def includes(self, pt):
        """
        Parameters
        ----------
        pt: Point
            Point to be tested for inclusion within the region
            defined by the instance.
            
        Returns
        -------
        bool
            True, if point pt lies within the region defined by the instance.
            False, otherwise.
        """
        return self._corners['bottom-left'] <= pt <= self._corners['top-right']
    def intersects(self, rctg):
        """
        Parameters
        ----------
        rctg: Rectangle
            Rectangle to be tested for intersection with instance.
            
        Returns
        -------
        bool
            True, if rctg has non-empty intersection with instance.
            False, otherwise.
        """
        return any([rctg.includes(corner) for corner in self._corners.values()])
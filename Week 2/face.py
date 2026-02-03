from PIL import Image
from IPython.display import display
import math

class Smile:
    
    """
    Class to render images of smiley faces.

    Attributes
    ----------

    width: int/float
           The width of the face's smile.

    angle: int/float
           The angle about which the face is rotated (in radians).

    background: tuple
                Tuple corresponding to the RGB colour-code for the background.

    face: tuple
          Tuple corresponding to the RBG colour-code for the face.
    ----------

    To construct an instance, call the constructor Smile, with parameters
    width (default argument equal to one) and angle (default argument equal
    to zero).  e.g.

    Smile(width = ..., angle = ...)
    """
    
    def __init__(self, width = 1, angle = 0):
        """
        This method initialises instances of Smile.

        Attributes assigned by this method include width and angle,
        both of which are provided directly by the arguments given to
        the constructor.

        Other attributes assigned here are background and face.
        """
        self.width = width
        self.angle = angle
        self.background = (0, 0, 0)
        self.face = (255, 255, 0)

    def __repr__(self):
        """
        This methods constructs and displays an image of size 256 x 256, with
        the colour of each pixel dependent on some boolean value.

        If the boolean attached to a point is True, the background colour
        is assigned to that point. If the boolean is False, the face colour
        is assigned.

        All points outside the radius 96 are True, as are any values inside
        this radius that are returned True by the features method.
        """
        img = Image.new('RGB', (256, 256))  # Create blank image of size 256 x 256.

        for x in range(256):
            for y in range(256):
                # Define center coordinates.
                cx = x - 128
                cy = 128 - y

                # Rotate point by -angle.
                rx =  cx * math.cos(self.angle) + cy * math.sin(self.angle)
                ry = -cx * math.sin(self.angle) + cy * math.cos(self.angle)

                # Set background and facial features to appropriate colours.
                if (rx**2 + ry**2 > 96**2) or self.features(rx, ry):
                    img.putpixel((x, y), self.background)
                else:
                    img.putpixel((x, y), self.face)

        display(img)
        return f'Smile(width = {self.width}, angle = {self.angle})'

    def features(self, x, y):
        """
        This method returns a boolean according to whether the point (x, y) lies
        inside a facial feature or not.  Returned value is True if point (x, y)
        lies inside mouth or eyes, and False otherwise.

        Note that these coordinates are defined so that the centre of the image is
        (0, 0), and the x and y axes rotate with the face.  When the angle of
        the face is zero, the x-axis points right, and the y-axis points up.
        """
        r2 = x**2 + y**2

        # Mouth
        if 46**2 < r2 < 50**2:
            theta = math.atan2(y, x)
            if -3*math.pi/4 - (self.width - 1)/2 < theta < -math.pi/4 + (self.width - 1)/2:
                return True

        # Eyes
        right_eye = (-34, 34)
        left_eye  = ( 34, 34)

        if (x - right_eye[0])**2 + (y - right_eye[1])**2 < 6**2:
            return True
        if (x - left_eye[0])**2 + (y - left_eye[1])**2 < 6**2:
            return True
            
        return False
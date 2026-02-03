# Make the necessary imports.
from PIL import Image
from IPython.display import display
import math

# Define a function that maps each pixel in the array to a matching
# complex number in the square  bounded by -1.5, 1.5, -1.5i and 1.5i.
def z(x, y, l):
    """Return a complex number in the square of side-length three, centred at the origin of the complex plane,
    with relative position matching the pixel (x, y) in a square array of side-length l."""
    return (-1.5 + 3*x/l) + (1.5 - 3*y/l)*1j

# Define the mapping g, for complex values z and c.
g = lambda z, c: z**2 + c

# Define a function that counts the number of iterations required
# for a complex value z to surpass the bound of two in its modulus
# (up to some maximal cut-off point).
def count(z, c, N):
    """Return the number of times a complex value z must be run through
    the mapping g(z) = z^2 + c until its absolute value exceeds two.
    If such a value has not been obtained before N iterations, then N is returned."""
    n = 0
    while (abs(z) <= 2) and (n < N):
        z = g(z, c)
        n += 1
    return n


def julia(c, l, N):
    img = Image.new('RGB', (l,l))

    two_pi_on_N = 2*math.pi/N

    for x in range(l):
        for y in range(l):
            n = count(z(x,y,l),c,N)

            r = round(N/2 * (1 + math.sin(two_pi_on_N * n)))
            gch = round(N/2 * (1 + math.cos(two_pi_on_N * n)))
            b = round(N/2 * (1 - math.sin(two_pi_on_N * n)))

            img.putpixel((x, y), (r, gch, b))
    
    img.save("julia.png")

    if __name__ != "__main__":
        display(img)

    return img

real = float(input("Real part:\t"))
imag = float(input("Imaginary part:"))
julia(c = real + imag*1j, l = 701, N = 255)

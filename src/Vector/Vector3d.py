import math

class Vector3d:
    """
    A mathematical vector in 3 dimensions.

    ...

    Attributes
    ----------
    x : float
        Its composant x.
    y : float
        Its composant y.
    z : float
        Its composant z.
    st : float
        Its standard.

    Methodes
    --------
    __add__(v)
        Operator +
        Adds the vector v and this vector.
        
    __sub__(v)
        Operator -
        Subtracts the vector v to this vector.

    __mul__(k)
        Operator *
        Multiplies the number k to this vector.

    __iadd__(v)
        Operator +=
        Adds the vector v to this vector.

    __isub__(v)
        Operator -=
        Subtracts the vector v to this vector.

    __imul__(k)
        Operator *=
        Multiplies the number k to this vector.

    __pow__(v)
        Operator **
        Returns the scalar product of this vector and v.

    __mod__(v)
        Operator %
        Returns the angle between this vector and v.

    """
    
    def __init__(self, x, y, z):
        """
        Parameters
        ----------
        x : float
            Its composant x.
        y : float
            Its composant y.
        z : float
            Its composant z.
        """
        
        self.x = x
        self.y = y
        self.z = z
        self.st = math.sqrt(x**2+y**2+z**2) #standard

    def __add__(self, v):
        """
        Operator +
        Adds the vector v and this vector.

        Parameters
        ----------
        v : Vector3d
            The vector which is added.
        """
        return Vector3d(self.x+v.x, self.y+v.y, self.z+v.z)

    def __sub__(self, v):
        """
        Operator -
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector3d
            The vector which is subtracted.
        """
        return Vector3d(self.x-v.x, self.y-v.y, self.z+v.z)

    def __mul__(self, k):
        """
        Operator *
        Multiplies the number k to this vector.

        Parameters
        ----------
        k : float
            The number which multiplied this vector.
        """
        return Vector2d(self.x*k, self.y*k, self.z*k)

    def __iadd__(self, v):
        """
        Operator +=
        Adds the vector v to this vector.

        Parameters
        ----------
        v : Vector3d
            The vector which is added.
        """
        self.x += v.x
        self.y += v.y
        self.z += v.z
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2)
        return self

    def __isub__(self, v):
        """
        Operator -=
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector3d
            The vector which is substracted.
        """
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2)
        return self

    def __imul__(self, k):
        """
        Operator *=
        Multiplies the number k to this vector.

        Parameters
        ----------
        k : float
            The number which multiplies this vector.
        """
        self.x *= k
        self.y *= k
        self.z *= k
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2)
        return self

    def __pow__(self, v):
        """
        Operator **
        Returns the scalar product of this vector and v.

        Parameters
        ----------
        v : Vector3d
            The vector with which the scalar product is calculated.
        """
        return self.x*v.x+self.y*v.y+self.z*v.z

    def __mod__(self, v):
        """
        Operator %
        Returns the angle in degrees between this vector and v.

        Parameters
        ----------
        v : Vector3d
            The vector with which the angle which is calculated is formed.
        """
        return math.degrees(math.acos(self**v/(self.st*v.st)))

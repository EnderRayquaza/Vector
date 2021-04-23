import math

class Vector3d:
    """
    A mathematical vector in 3 dimensions.

    ...

    v1.3
    by EnderRayquaza

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
    dir : tuple
        Its direction. It's a vector that its standars is equal to 1.


    Methodes
    --------
    calculate_param()
        Calculates its standard and its direction.
    
    __add__(v)
        Operator +
        Adds the vector v and this vector.
        
    __sub__(v)
        Operator -
        Subtracts the vector v to this vector.

    __mul__(k)
        Operator *
        Multiplies the number k and this vector.

    __truediv__(k)
        Operator /
        Divides the number k to this vector.

    __iadd__(v)
        Operator +=
        Adds the vector v to this vector.

    __isub__(v)
        Operator -=
        Subtracts the vector v to this vector.

    __imul__(k)
        Operator *=
        Multiplies the number k to this vector.

    __itruediv__(k)
        Operator /=
        Divides the number k to this vector.

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
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2)
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st, self.z/self.st)
        else:
            self.dir = (0, 0, 0)

    def calculate_param(self):
        """
        Calculates its standard and its direction.
        """
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st, self.z/self.st)
        else:
            self.dir = (0, 0, 0)

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

    def __truediv__(self, k):
        """
        Operator /
        Divides the number k to this vector.

        Parameters
        ----------
        k : float
            The number which divided this vector.
        """
        return Vector2d(self.x/k, self.y/k, self.z/k)

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
        self.calculate_param()
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
        self.calculate_param()
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
        self.calculate_param()
        return self

    def __itruediv__(self, k):
        """
        Operator /
        Divides the number k to this vector.

        Parameters
        ----------
        k : float
            The number which divided this vector.
        """
        self.x /= k
        self.y /= k
        self.z /= k
        self.calculate_param()
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

    def show(self, name="v"):
        """
        Prints its composants and its standard.

        Parameters
        ----------
        name : str
            The name of the Vector.
        """
        print(name, "(", self.x, "/", self.y, ")")
        print("||", name, "|| = ", self.st, sep="")

V0 = Vector3d(0, 0, 0)

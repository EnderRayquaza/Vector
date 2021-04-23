import math

class Vector2d:
    """
    A mathematical vector in 2 dimensions.

    ...

    v1.3
    by EnderRayquaza
    
    Attributes
    ----------
    x : float
        Its composant x.
    y : float
        Its composant y.
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

    __complex__()
        Operator complex()
        Makes a complex number such as x+yj.

    """
    
    def __init__(self, x, y):
        """
        Parameters
        ----------
        x : float
            Its composant x.
        y : float
            Its composant y.
        """
        
        self.x = x
        self.y = y
        self.st = math.sqrt(self.x**2+self.y**2)
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st)
        else:
            self.dir = (0, 0)

    def calculate_param(self):
        """
        Calculates its standard and its direction.
        """
        self.st = math.sqrt(self.x**2+self.y**2)
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st)
        else:
            self.dir(0, 0)

    def __add__(self, v):
        """
        Operator +
        Adds the vector v and this vector.

        Parameters
        ----------
        v : Vector2d
            The vector which is added.
        """
        return Vector2d(self.x+v.x, self.y+v.y)

    def __sub__(self, v):
        """
        Operator -
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector2d
            The vector which is subtracted.
        """
        return Vector2d(self.x-v.x, self.y-v.y)

    def __mul__(self, k):
        """
        Operator *
        Multiplies the number k to this vector.

        Parameters
        ----------
        k : float
            The number which multiplied this vector.
        """
        return Vector2d(self.x*k, self.y*k)

    def __truediv__(self, k):
        """
        Operator /
        Divides the number k to this vector.

        Parameters
        ----------
        k : float
            The number which divided this vector.
        """
        return Vector2d(self.x/k, self.y/k)

    def __iadd__(self, v):
        """
        Operator +=
        Adds the vector v to this vector.

        Parameters
        ----------
        v : Vector2d
            The vector which is added.
        """
        self.x += v.x
        self.y += v.y
        self.calculate_param()
        return self

    def __isub__(self, v):
        """
        Operator -=
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector2d
            The vector which is substracted.
        """
        self.x -= v.x
        self.y -= v.y
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
        self.calculate_param()
        return self

    def __pow__(self, v):
        """
        Operator **
        Returns the scalar product of this vector and v.

        Parameters
        ----------
        v : Vector2d
            The vector with which the scalar product is calculated.
        """
        return self.x*v.x+self.y*v.y

    def __mod__(self, v):
        """
        Operator %
        Returns the angle in degrees between this vector and v.

        Parameters
        ----------
        v : Vector2d
            The vector with which the angle which is calculated is formed.
        """
        return math.degrees(math.acos(self**v/(self.st*v.st)))

    def __complex__(self):
        """
        Operator complex()
        Makes a complex number such as x+yj.
        """
        return complex(self.x, self.y)

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

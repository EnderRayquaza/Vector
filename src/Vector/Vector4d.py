import math

class Vector4d:
    """
    A mathematical vector in 4 dimensions.

    ...

    v2.0.5
    by EnderRayquaza

    Attributes
    ----------
    x : float
        Its composant x.
    y : float
        Its composant y.
    z : float
        Its composant z.
    t : float
        Its composant t. t is for time like in the 4d-spacetime.
    st : float
        Its standard.
    dir : tuple
        Its direction. It's a vector that its standars is equal to 1.
    name : str
        Its name.


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
    
    def __init__(self, x, y, z, t, name="None"):
        """
        Parameters
        ----------
        x : float
            Its composant x.
        y : float
            Its composant y.
        z : float
            Its composant z.
        name : str
            Its name.
        """
        
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2+self.t**2)
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st, self.z/self.st, self.t/self.st)
        else:
            self.dir = (0, 0, 0, 0)

        self.name = name

    def calculate_param(self):
        """
        Calculates its standard and its direction.
        """
        self.st = math.sqrt(self.x**2+self.y**2+self.z**2+self.t**2)
        if(self.st != 0):
            self.dir = (self.x/self.st, self.y/self.st, self.z/self.st, self.t/self.st)
        else:
            self.dir = (0, 0, 0, 0)

    def __add__(self, v):
        """
        Operator +
        Adds the vector v and this vector.

        Parameters
        ----------
        v : Vector4d
            The vector which is added.
        """
        return Vector4d(self.x+v.x, self.y+v.y, self.z+v.z, self.t+v.t, self.name + " + " + v.name)

    def __sub__(self, v):
        """
        Operator -
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector4d
            The vector which is subtracted.
        """
        return Vector4d(self.x-v.x, self.y-v.y, self.z+v.z, self.t+v.t, self.name + " - " + v.name)

    def __mul__(self, k):
        """
        Operator *
        Multiplies the number k to this vector.

        Parameters
        ----------
        k : float
            The number which multiplied this vector.
        """
        return Vector2d(self.x*k, self.y*k, self.z*k, self.t*k, self.name + " * " + str(k))

    def __truediv__(self, k):
        """
        Operator /
        Divides the number k to this vector.

        Parameters
        ----------
        k : float
            The number which divided this vector.
        """
        return Vector2d(self.x/k, self.y/k, self.z/k, self.t/k, self.name + " / " + str(k))

    def __iadd__(self, v):
        """
        Operator +=
        Adds the vector v to this vector.

        Parameters
        ----------
        v : Vector4d
            The vector which is added.
        """
        self.x += v.x
        self.y += v.y
        self.z += v.z
        self.t += v.t
        self.calculate_param()
        return self

    def __isub__(self, v):
        """
        Operator -=
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : Vector4d
            The vector which is substracted.
        """
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        self.t -= v.t
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
        self.t *= k
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
        self.t /= k
        self.calculate_param()
        return self

    def __pow__(self, v):
        """
        Operator **
        Returns the scalar product of this vector and v.

        Parameters
        ----------
        v : Vector4d
            The vector with which the scalar product is calculated.
        """
        return self.x*v.x+self.y*v.y+self.z*v.z+self.t*v

    def __mod__(self, v):
        """
        Operator %
        Returns the angle in degrees between this vector and v.

        Parameters
        ----------
        v : Vector4d
            The vector with which the angle which is calculated is formed.
        """
        return math.degrees(math.acos(self**v/(self.st*v.st)))

    def show(self, name="v"):
        """
        Prints its composants, its standard and its direction.

        Parameters
        ----------
        name : str
            The name of the Vector.
        """
        if(name is None):
            if(self.name == "None"):
                name = "v"
            else:
                name = self.name
        print(name, "(", self.x, "/", self.y, "/", self.z, "/", self.t ")")
        print("||", name, "|| = ", self.st, sep="")
        print("dir(", self.dir[0], "/", self.dir[1], "/",
              self.dir[2], "/", self.dir[3], ")")

def V0_():
    return Vector4d(0, 0, 0, 0, "0_")

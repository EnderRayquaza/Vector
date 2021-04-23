import math

class VectorNd:
    """
    A mathematical vector in n dimensions.

    ...

    v2.0
    by EnderRayquaza

    Attributes
    ----------
    l : list
        A list with its composants.
    st : float
        Its standard.
    dir : list
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
    
    def __init__(self, l, name="None"):
        """
        Parameters
        ----------
        l : list
            A list with its composants.
        name : str
            Its name.
        """
        
        self.l = l
        total = 0
        for comp in self.l:
            total += comp**2
        self.st = math.sqrt(total)
        if(self.st != 0):
            self.dir = list()
            for comp in self.l:
                self.dir.append(comp/self.st)
        else:
            self.dir = [0]*len(self.l)

        self.name = name

    def calculate_param(self):
        """
        Calculates its standard and its direction.
        """
        total = 0
        for comp in self.l:
            total += comp**2
        self.st = math.sqrt(total)
        if(self.st != 0):
            self.dir = list()
            for comp in self.l:
                self.dir.append(comp/self.st)
        else:
            self.dir = [0]*len(self.l)


    def __add__(self, v):
        """
        Operator +
        Adds the vector v and this vector.

        Parameters
        ----------
        v : VectorNd
            The vector which is added.
        """
        new_l = list()
        for i in range(len(self.l)):
            new_l.append(self.l[i]+v.l[i])
        return VectorNd(new_l, self.name + " + " + v.name)

    def __sub__(self, v):
        """
        Operator -
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : VectorNd
            The vector which is subtracted.
        """
        new_l = list()
        for i in range(len(self.l)):
            new_l.append(self.l[i]-v.l[i])
        return VectorNd(new_l, self.name + " - " + v.name)

    def __mul__(self, k):
        """
        Operator *
        Multiplies the number k to this vector.

        Parameters
        ----------
        k : float
            The number which multiplied this vector.
        """
        new_l = list()
        for i in range(len(self.l)):
            new_l.append(self.l[i]*k)
        return VectorNd(new_l, self.name + " * " + k)

    def __truediv__(self, k):
        """
        Operator /
        Divides the number k to this vector.

        Parameters
        ----------
        k : float
            The number which divided this vector.
        """
        new_l = list()
        for i in range(len(self.l)):
            new_l.append(self.l[i]/k)
        return VectorNd(new_l, self.name + " / " + k)

    def __iadd__(self, v):
        """
        Operator +=
        Adds the vector v to this vector.

        Parameters
        ----------
        v : VectorNd
            The vector which is added.
        """
        for i in range(len(self.l)):
            self.l[i] += v.l[i]
        self.calculate_param()
        return self

    def __isub__(self, v):
        """
        Operator -=
        Subtracts the vector v to this vector.

        Parameters
        ----------
        v : VectorNd
            The vector which is substracted.
        """
        for i in range(len(self.l)):
            self.l[i] -= v.l[i]
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
        for i in range(len(self.l)):
            self.l[i] *= k
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
        for i in range(len(self.l)):
            self.l[i] /= k
        self.calculate_param()
        return self

    def __pow__(self, v):
        """
        Operator **
        Returns the scalar product of this vector and v.

        Parameters
        ----------
        v : VectorNd
            The vector with which the scalar product is calculated.
        """
        sc_prod = 0
        for i in range(len(self.l)):
            sc_prod += self.l[i]*v.l[i])
        return self.x*v.x+self.y*v.y+self.z*v.z

    def __mod__(self, v):
        """
        Operator %
        Returns the angle in degrees between this vector and v.

        Parameters
        ----------
        v : VectorNd
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
            if(self.name is None):
                name = "v"
            else:
                name = self.name
        print(name, "(", end="")
        for comp in self.l:
            print(comp, "/", end="")
        print(")")
        print("||", name, "|| = ", self.st, sep="")
        print("dir(",
        for comp in self.dir:
            print(comp, "/", end="")
        print(")")

def V0_():
    return VectorNd([0], "0_")

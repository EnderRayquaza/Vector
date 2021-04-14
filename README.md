# Vector pkg

### How to install
- Windows
 ```shell
 py -m pip install --index-url https://test.pypi.org/simple/ --no-deps vector-pkg-ENDERRAYQUAZA
 ```
- Unix/macOS
 ```shell
 python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps vector-pkg-ENDERRAYQUAZA
 ```
### How to use
```Python
import Vector as vec
v = vec.Vector(5, 7.5) #Creates a instance of Vector
print(v.x) #Shows his composant x >>> 5
print(v.y) #Idem                  >>> 7.5
print(v.st) #Shows his standard   >>> 9.013878188659973

u = vec.Vector(-8, 0.25) #Creates an other instance of Vector
w = v+u #Makes a instance of Vector with composants (v.x + u.x; v.y + u.y)
print(w.x, w.y) # >>> -3 7.75
w = v-u #Idem but with a subtraction
print(w.x, w.y) # >>> 13 7.25

k = 5
w = v*k
print(w.x, w.y) # >>> 25, 37.5

#You can do this too
v += u
v -= u
v *= k

p = v**u #Calculates the scalar product of v and u          
print(p) # >>> -38.125
a = v%u  #Calculates the angle (in degrees) between v and u
print(a) # >>> 121.90015691773374
z = complex(v) #Makes a complex number equal at x+yi
print(z) # >>> (5+7.5j)
```

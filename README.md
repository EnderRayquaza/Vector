# Vector pkg
## Actual version : 1.2
### How to install
 ```shell
 pip install vector-pkg-enderrayquaza
 ```
### How to use
##### Vector2d
```Python
import Vector.Vector2d as vec2
v = vec2.Vector2d(5, 7.5) #Creates a instance of Vector2d
print(v.x) #Shows his composant x >>> 5
print(v.y) #Idem                  >>> 7.5
print(v.st) #Shows his standard   >>> 9.013878188659973

u = vec2.Vector2d(-8, 0.25) #Creates an other instance of Vector2d
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

##### Vector3d
```Python
import Vector.Vector3d as vec3
v = vec3.Vector3d(5, 7.5, 0) #Creates a instance of Vector3d
print(v.x) #Shows his composant x >>> 5
print(v.y) #Idem                  >>> 7.5
print(v.z) #Idem                  >>> 0
print(v.st) #Shows his standard   >>> 9.013878188659973

u = vec3.Vector3d(-8, 0.25, 2) #Creates an other instance of Vector3d
w = v+u #Makes a instance of Vector with composants (v.x + u.x; v.y + u.y; v.z + u.z)
print(w.x, w.y, w.z) # >>> -3 7.75 2
w = v-u #Idem but with a subtraction
print(w.x, w.y, w.z) # >>> 13 7.25 -2

k = 5
w = v*k
print(w.x, w.y, w.z) # >>> 25, 37.5 0

#You can do this too
v += u
v -= u
v *= k

p = v**u #Calculates the scalar product of v and u          
print(p) # >>> -38.125
a = v%u  #Calculates the angle (in degrees) between v and u
print(a) # >>> 121.90015691773374
```

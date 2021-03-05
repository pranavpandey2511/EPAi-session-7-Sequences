### Assignment 7B

A regular strictly convex polygon is a polygon that has the following characteristics:
all interior angles are less than 180
all sides have equal length
 
For a regular strictly convex polygon with:
$interiorAngle\:=\:\left(n\:-\:2\right)\cdot\frac{180}{n}$
<br>
$edgeLength,\:s\:=\:2\cdot R\cdot\sin\left(\frac{\pi}{n}\right)$

$apothem,\:a\:=\:R\cdot\cos\left(\frac{\pi}{n}\right)$

$area\:=\:\frac{1}{2}\cdot n\cdot s\cdot a$

$ perimeter\:=\:n\cdot s$


### Objective 1 [pts:400]:

Create a Polygon Class:
where initializer takes in:
number of edges/vertices
circumradius
that can provide these properties:
* edges
* vertices
* interior angle
* edge length
* apothem
* area
* perimeter

that has these functionalities:

* a proper __repr__ function
* implements equality (==) based on # vertices and circumradius (__eq__)
* implements > based on number of vertices only (__gt__)

### Objective 2 [pts:600]:
Implement a Custom Polygon sequence type:
where initializer takes in:
* number of vertices for largest polygon in the sequence
* common circumradius for all polygons

that can provide these properties:
* max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
that has these functionalities:

* functions as a sequence type (__getitem__)
* supports the len() function (__len__)
* has a proper representation (__repr__)


```python
from polygon import Polygon
```


```python
help(Polygon)
```

    Help on class Polygon in module polygon:
    
    class Polygon(builtins.object)
     |  This class is used for creating regular strict polygons.
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, poly)
     |      Provides ability to compare two objects for euality (==).
     |  
     |  __gt__(self, poly)
     |      Provide ability to compare two objects for greater than '>' test.
     |  
     |  __init__(self, n_edges:int, circumradius:float)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  apothem
     |      Apothem length for the polygon
     |  
     |  area
     |      Area of the polygon
     |  
     |  circumradius
     |      Circumradius of the polygon
     |  
     |  edge_length
     |      Edge length of individual edge in the polygon
     |  
     |  interior_angle
     |      Interior angle value of each angle in the polygon
     |  
     |  n_edges
     |      Number of edges in the polygon
     |  
     |  perimeter
     |      Perimeter of the polygon
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    



```python
Polygon(n_edges=4, circumradius=4)
```




    Polygon class to create polygons which are regular strictly convex.
            Regular strict polygons have two properties: 
     1- All interior angles are less than 180.         
     2- All sides have equal length



<h3> Objective 1 </h3>


```python
poly1 = Polygon(4, 4)
poly2 = Polygon(5, 3)
poly3 = Polygon(4, 6)
```


```python
poly1.n_edges
```




    4




```python
poly1.interior_angle
```




    90.0




```python
poly1.edge_length
```




    5.65685424949238




```python
poly1.apothem
```




    2.8284271247461903




```python
poly1.area
```




    32.0




```python
poly1.perimeter
```




    22.62741699796952



**\_\_repr\_\_**


```python
Polygon(n_edges=4, circumradius=4)
```




    Polygon class to create polygons which are regular strictly convex.
            Regular strict polygons have two properties: 
     1- All interior angles are less than 180.         
     2- All sides have equal length



**EQUAL TO '=='**


```python
poly1 == poly2
```




    False




```python
poly1 == poly3
```




    False




```python
poly1 == Polygon(n_edges=4, circumradius=4) # Same vertices and circumradius
```




    True



**GREATER THAN '>'**


```python
poly1 > poly2
```




    False




```python
poly2 > poly1
```




    True




```python
poly1 > poly3
```




    False






```python

```


```python

```

### Objective 2

### Custom polygon sequence


```python
from poly_list import PolyList
```


```python
help(PolyList)
```

    Help on class PolyList in module poly_list:
    
    class PolyList(builtins.object)
     |  Methods defined here:
     |  
     |  __getitem__(self, index)
     |  
     |  __init__(self, n_edges_max:int, circumradius:float)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __len__(self)
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  most_efficient
     |      Most efficient polygon in terms of area:perimeter ratio.
     |      This will always be the max vertices polygon.
    



```python
my_poly = PolyList(5,4)
```


```python
my_poly[1]
```




    Number of Edges: 3, Circumradius: 4




```python
my_poly.most_efficient
```




    Number of Edges: 5, Circumradius: 4



For n=25, most efficient polygon:


```python
new_list = PolyList(25, 7)
```


```python
new_list.most_efficient
```




    Number of Edges: 25, Circumradius: 7




```python

```

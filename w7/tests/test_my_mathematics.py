import math
from my_mathematics.math import MyMath, MyComplexMath
from my_mathematics.linear_algebra import Vector
import cmath
import pytest
import numpy as np


@pytest.mark.parametrize('num',[(4),(0),(-1)])
def test_sin(num):
    assert MyMath.sin(num) == math.sin(num)


def test_pi():
    assert MyMath.pi() == 3.14


@pytest.mark.parametrize("num",[(2),(9),(0)])
def test_sqrt(num):
    assert MyMath.sqrt(num) == math.sqrt(num)


@pytest.mark.parametrize("num",[(-2),(-9),(0),(-1)])
def test_sqrt_complex(num):
    assert str(MyComplexMath.sqrt(num)) == str(cmath.sqrt(num))


@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-1,0,0],[0,1,0]),([0,0,0],[0,0,0])])
def test_Vector_add(v1,v2):

    numpy_array_1 = np.array(v1)
    numpy_array_2 = np.array(v2)
    vect1=Vector(','.join(map(str,v1)))
    vect2=Vector(','.join(map(str,v2)))

    a=str(numpy_array_1+numpy_array_2)
    a=list(a[1:-1].split(' '))
    a=list(el for el in a if el!='')
    assert str(vect1+vect2) == ','.join(a)


@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-1,0,0],[0,1,0]),([0,0,0],[0,0,0])])
def test_Vector_sub(v1,v2):

    numpy_array_1 = np.array(v1)
    numpy_array_2 = np.array(v2)
    vect1=Vector(','.join(map(str,v1)))
    vect2=Vector(','.join(map(str,v2)))

    a=str(numpy_array_1-numpy_array_2)
    a=list(a[1:-1].split(' '))
    a=list(el for el in a if el!='')
    assert str(vect1-vect2) == ','.join(a)


@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-1,0,0],[0,1,0]),([0,0,0],[0,0,0])])
def test_Vector_mul(v1,v2):

    numpy_array_1 = np.array(v1)
    numpy_array_2 = np.array(v2)
    vect1=Vector(','.join(map(str,v1)))
    vect2=Vector(','.join(map(str,v2)))

    assert vect1*vect2 == np.sum(numpy_array_1*numpy_array_2)

@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-1,0,0],[0,1,0]),([0,0,0],[0,0,0])])
def test_Vector_and(v1,v2):

    numpy_array_1 = np.array(v1)
    numpy_array_2 = np.array(v2)
    vect1=Vector(','.join(map(str,v1)))
    vect2=Vector(','.join(map(str,v2)))

    a=str(np.cross(numpy_array_1,numpy_array_2))
    a=list(a[1:-1].split(' '))
    a=list(el for el in a if el!='')
    assert str(vect1&vect2) == ','.join(a)

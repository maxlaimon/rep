import math
from my_mathematics.math import MyMath, MyComplexMath
from my_mathematics.linear_algebra import Vector
import cmath
import pytest

#math tests
@pytest.mark.parametrize('num',[(4),(0),(-1)])
def test_sin(num):
    assert MyMath.sin(num) == math.sin(num)


def test_pi():
    assert MyMath.pi() == 3.14


@pytest.mark.parametrize("num",[(2),(9),(0)])
def test_sqrt(num):
    assert MyMath.sqrt(num) == math.sqrt(num)

#cmath tests
@pytest.mark.parametrize("num",[(-2),(-9),(0),(-1)])
def test_sqrt_complex(num):
    assert str(MyComplexMath.sqrt(num)) == str(cmath.sqrt(num))

#vector tests
#inp - input, exp - expected
@pytest.mark.parametrize('inp, exp',[(Vector(1, 2, 3) + Vector(3, 4, 5), Vector(4, 6, 8)), (Vector(0, 0, 1) + Vector(1, 1, 0), Vector(1, 1, 1))])
def test_vector_add(inp, exp):
    assert inp == exp


@pytest.mark.parametrize('inp, exp',[(Vector(1, 2, 3) - Vector(3, 4, 5), Vector(-2, -2, -2)), (Vector(0, 0, 1) - Vector(1, 1, 0), Vector(-1, -1, 1))])
def test_vector_sub(inp, exp):
    assert inp == exp


@pytest.mark.parametrize('inp, exp',[(Vector(1, 2, 3)&Vector(3, 2, 1), Vector(-4, 8, -4)), (Vector(0, 0, 1)&Vector(1, 1, 0), Vector(-1, 1, 0))])
def test_vector_and(inp, exp):
    assert inp == exp


@pytest.mark.parametrize('inp, exp',[(Vector(0, 12, 5).distance(), 13), (Vector(0, 0, 1).distance(), 1), (Vector(3, 4, 0).distance(), 5)])
def test_vector_distance(inp, exp):
    assert inp == exp

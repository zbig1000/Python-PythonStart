import pytest  # pip install pytest

from functotest import div  

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1,0)

def test_is_working_normally():
    expected = div(4,2)
    got = 2
    assert got == expected

def test_icorrect_input():
    with pytest.raises(TypeError):
        div('a',2)

def test_dividing_two_integers():
    expected = div(3,2)
    got = 1.5
    assert got == expected        
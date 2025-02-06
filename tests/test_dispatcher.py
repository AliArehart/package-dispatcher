import pytest

from package import sort_package


def test_standard_package():
    assert sort_package(100, 50, 30, 10) == "Standard"


def test_bulky_package():
    assert sort_package(200, 50, 30, 10) == "Special"


def test_heavy_package():
    assert sort_package(100, 50, 30, 25) == "Special"


def test_bulky_and_heavy_package():
    assert sort_package(200, 200, 200, 25) == "Rejected"

def test_negative_dimensions():
    with pytest.raises(ValueError):
        sort_package(-100, 50, 30, 10)
    with pytest.raises(ValueError):
        sort_package(100, 50, 30, -10)

def test_float_dimensions():
    with pytest.raises(ValueError):
        sort_package(100.5, 50, 30, 10)
    with pytest.raises(ValueError):
        sort_package(100, 50, 30, 10.5)
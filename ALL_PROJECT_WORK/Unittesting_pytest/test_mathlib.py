#i also add Python unit testing - skip/selectively run tests in pytest----please check

#use skip or skipif for skipping certain things---  import sys ,skipif,sys.version_info<(3,9)
import mathlib
import pytest


def test_cal_total():
    total=mathlib.cal_total(4,5)
    assert total==9

def test_cal_multiple():
    result=mathlib.cal_multiple(4,5)
    assert result==20

def test_dummy():           #for testing if name test is cal---but this func not so,
    assert True

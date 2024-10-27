import mathlib1
import pytest


@pytest.mark.parametrize('test_input,excepted_output',
                         [
                             (5,25),
                             (2,4),
                             (9,81)
                         ]
                         )
def test_cal_square(test_input,excepted_output):
    result=mathlib1.cal_square(test_input)
    assert result==excepted_output


import pytest
from easyutils.timeutils import is_holiday

def test_is_holiday():
    cases = [('20161001', True), ('20161008', False), ('20161118', False), ('20161119', True)]
    for day, result in cases:
        assert is_holiday(day) == result

from solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
    def test_inclusive_exclusive_range_value(self):
        assert sum_solution.compute(0, 99) == 99
    def test_invalid_range_value(self):
        with pytest.raises()

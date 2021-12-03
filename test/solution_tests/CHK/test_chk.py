from solutions.CHK import checkout_solution
import pytest

class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout("AAABCBAD") == 260
    def test_non_string(self):
        assert checkout_solution.checkout(1) == -1
    def test_unpermitted_value(self):
        assert checkout_solution.checkout("AAADE") == -1

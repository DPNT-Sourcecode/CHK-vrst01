from solutions.HLO import hello_solution
import pytest

class TestHLO():
    def test_hlo(self):
        assert hello_solution.hello("clive") == "Hello clive"

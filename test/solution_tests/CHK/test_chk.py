from solutions.CHK import checkout
import pytest

class TestCHK():
    def test_hlo(self):
        assert hello_solution.hello("clive") == "Hello, clive!"
    def test_non_string(self):
        with pytest.raises(TypeError):
            assert hello_solution.hello(1)
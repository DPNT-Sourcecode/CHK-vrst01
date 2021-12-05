from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution
import pytest

class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout("AAABCBAD") == 260
    def test_non_string(self):
        assert checkout_solution.checkout(1) == -1
    def test_unpermitted_value(self):
        assert checkout_solution.checkout("AAADq") == -1
    def test_E_offer(self):
        assert checkout_solution.checkout("ABBEE") == 160
    def test_7_As(self):
        assert checkout_solution.checkout("AAAAA") == 200
    def test_basic_F_offer(self):
        assert checkout_solution.checkout("AFFF") == 70
    def test_5_Fs_offer(self):
        assert checkout_solution.checkout("AFFFFF") == 90
    def test_6_Fs_offer(self):
        assert checkout_solution.checkout("AFFFFFF") == 90
    def test_6_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUU") == 250
    def test_7_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUUU") == 290
    def test_8_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUUUU") == 290
    def test_R_Q_offer(self):
        assert checkout_solution.checkout("ARRRQQQ") == 260
    def test_R_offer_Q_offer(self):
        assert checkout_solution.checkout("ARRRQQQQ") == 280
